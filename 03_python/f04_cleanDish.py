import pandas as pd
import numpy as np
import re
import helper

#@begin CleanDish_python1
#@desc Deduplicates dish names after cleaning.   See detail {TBD LINK}.

#@in Dish_clean @URI file:../01_openrefine/Dish_clean.csv.gz
#@in MenuItem_clean @URI file:../01_openrefine/MenuItem_clean.csv.gz

dish = pd.read_csv("../01_openrefine/Dish_clean.csv.gz", compression='gzip')

#@begin replaceNA
#@desc Replace empty strings with NA for easier pandas compute
#@in Dish_clean
#@out dish_1
dish.fillna('', inplace=True)
#@end replaceNA

#@begin caseFix
#@desc Convert to title case
#@in dish_1
#@out dish_2
words = { "a la": re.compile(r'\bA La\b'),
          "of": re.compile(r'\bOf\b'),
         "in": re.compile(r'\bIn\b'),
         "every": re.compile(r'\bEvery\b'),
         "with": re.compile(r'\bWith\b'),
        "or": re.compile(r'\bOr\b'),
         "on": re.compile(r'\bOn\b'),
         "per": re.compile(r'\bPer\b'),
         "and": re.compile(r'\bAnd\b'),
        }

def cleanDish(x):
    # Convert to title case
    x = x.title()
    
    # Replace & with and
    x = x.replace("&", "And")
    
    # Title is a little too greedy so correct
    for (k,v) in words.items():
        # Apply the pattern stored in the values of the dictionary,
        # replacing it by the corresponding key.
        # e.g. "A La" gets replaced by "a la" because "a la" => r'\bA La\b'
        x = v.sub(k, x)
   
    return x
dish['name'] = dish['name'].apply(cleanDish)
#@end caseFix

#@begin dedupDish
#@desc Identify duplicate entries in the _name_ field, and consolidate rows
#@in dish_2
#@out dish_3
def dedupDish():
    new_dish = dish.copy()
    
    freqs = helper.freq(new_dish['name'], printThis = False)

    nextID = max(new_dish['id']) + 1

    menus_appeared = {}
    times_appeared = {}
    first_appeared = {}
    last_appeared = {}
    lowest_price = {}
    highest_price = {}
    replacedKey = {}
    freqs2 = {}
    for (k, v) in freqs.items():
        if v > 1:
            freqs2[k] = v
            menus_appeared[k] = 0
            times_appeared[k] = 0
            first_appeared[k] = None
            last_appeared[k] = None
            lowest_price[k] = None
            highest_price[k] = None
            replacedKey[k] = nextID
            nextID = nextID + 1
    freqs = freqs2
    del(freqs2)
    
    # Sometimes these fields are blank. Change to NaN so that aggregates work better
    new_dish['first_appeared'].replace(0, np.nan, inplace=True)
    new_dish['last_appeared'].replace(0, np.nan, inplace=True)
    new_dish['lowest_price'].replace(r'^\s*$', np.nan, regex=True, inplace=True)
    new_dish['highest_price'].replace(r'^\s*$', np.nan, regex=True, inplace=True)
    
    # These are used for logistics--which foreign keys do we need to update
    # and which rows do we need to delete
    new_rows = []
    delete_me = []
    replaceKeys = {}
    
    # Helper function with aggregate
    def rolling_min(m, x):
        if m is None: return x
        elif x < m: return x
        else: return m
    
    def rolling_max(m, x):
        if m is None: return x
        elif x > m: return x
        else: return m
    
    counter = 0
    for (index, row) in new_dish.iterrows():
        counter = counter + 1
        if counter % 10000 == 0: print(counter)
        if row['name'] in freqs:
            N = row['name']
            menus_appeared[N] += row['menus_appeared']
            times_appeared[N] += row['times_appeared']
            first_appeared[N] = rolling_min(first_appeared[N], row['first_appeared'])
            last_appeared[N] = rolling_max(last_appeared[N], row['last_appeared'])
            lowest_price[N] = rolling_min(lowest_price[N], row['lowest_price'])
            highest_price[N] = rolling_max(highest_price[N], row['highest_price'])
            delete_me.append(index)
            replaceKeys[row['id']] = replacedKey[N]

    new_dish.drop(delete_me, inplace=True)

    new_rows = pd.DataFrame({
        "id": [replacedKey[k] for k in freqs.keys()],
        "name": [k for k in freqs.keys()],
        "name_cluster": [k for k in freqs.keys()],
        "menus_appeared": [menus_appeared[k] for k in freqs.keys()],
        "times_appeared": [times_appeared[k] for k in freqs.keys()],
        "first_appeared": [first_appeared[k] for k in freqs.keys()],
        "last_appeared": [last_appeared[k] for k in freqs.keys()],
        "lowest_price": [lowest_price[k] for k in freqs.keys()],
        "highest_price": [highest_price[k] for k in freqs.keys()]})
    
    # Hack to force new_rows to have same types as original data frame
    new_rows = new_rows.astype(new_dish.dtypes.to_dict())
    new_dish = new_dish.append(new_rows, ignore_index = True)        
    new_dish['first_appeared'] = new_dish['first_appeared'].astype('Int64')
    new_dish['last_appeared'] = new_dish['last_appeared'].astype('Int64')

    return (new_dish, replaceKeys)

(dish, replaceKeys) = dedupDish()
#@end dedupDish

#@begin exportData
#@desc Write out results back to CSV
#@in dish_3
#@out Dish_clean_dedup @URI file:p02_dish_cleaned.csv.gz
dish.to_csv("p02_dish_cleaned.csv.gz", compression='gzip', index = False)
#@end exportData

#@begin importMenuItem
#@desc Read in MenuItem
#@in MenuItem_clean @URI file:../01_openrefine/MenuItem_clean.csv.gz
#@out menuitem_1 
menuItem = pd.read_csv("../01_openrefine/MenuItem_clean.csv.gz", compression='gzip')
menuItem['dish_id'] = menuItem['dish_id'].astype('Int64')
#@end importMenuItem

#@begin replaceForeignKeys
#@desc Replace the duplicate entries' Foreign Keys with the new IDs 
#@in menuitem_1
#@out menuitem_2
def replaceDishID(x):
    if x in replaceKeys: return replaceKeys[x]
    else: return x

temp = menuItem['dish_id'].apply(replaceDishID).astype('Int64')
print("{0} rows changed, {1} not changed.".format(sum(temp != menuItem['dish_id']), sum(temp == menuItem['dish_id'])))
menuItem['dish_id'] = temp
#@end replaceForeignKeys

#@begin exportMenuItem
#@in menuitem_2
#@out MenuItem_clean2 @URI file:../03_python/p02_MenuItem_cleaned.csv.gz
menuItem.to_csv("p02_MenuItem_cleaned.csv.gz", compression='gzip', index = False)
#@end exportMenuItem

#@begin exportTokens
#@in dish_3
#@out tokens @URI file:tokens.csv
# This breaks up dish into tokens and collects them in a single placce.
# No need to rerun this unless you need to recrate tokens.csv
results = {}
for (index, row) in dish.iterrows():
    el = row['name'].split()
    for em in el:
        if em in results: results[em] += 1
        else: results[em] = 1

results_df = pd.DataFrame({"token": list(results.keys()),
                        "frequency": list(results.values())})
results_df.to_csv("tokens.csv", index = False)
#@end exportTokens

#@out tokens
#@out Dish_clean_dedup
#@out MenuItem_clean2
#@end CleanDish_python1