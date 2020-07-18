import pandas as pd
import numpy as np
import re

#@begin CleanDish_python2
#@desc Python.  Extracting cuisine information from dish name.  See detail {TBD LINK}.
#@in Dish_clean_dedup @URI file:p02_dish_cleaned.csv.gz
#@in tokens_cleaned @URI file:../03_python/tokens_cleaned.csv
#@out Dish_clean2 @URI file:../03_python/p03_disch_cleaned.csv.gz

#@begin importData
#@desc Import data from CSV into pandas
#@in Dish_clean_dedup
#@out dish_1
dish = pd.read_csv("p02_dish_cleaned.csv.gz", compression='gzip')
#@end importData

#@begin importTokens
#@desc Import tokens from CSV into pandas
#@in tokens_cleaned
#@out tokens_cleaned_1
# I imported tokens.csv into excel and manually labelled the first 50% of the tokens
tokens = pd.read_csv("tokens_cleaned.csv")
labels = {}
for (index, row) in tokens.iterrows():
    if pd.notna(row['action']):
        labels[row['token']] = (row['action'], row['value'])
#@end importTokens

#@begin convertDishToCuisine
#@desc Extract information from dish name
#@in dish_1
#@in tokens_cleaned_1
#@out dish_2
# Each of the tokens comes with an action
#  del => "delete this word it is unimportant"
#  prep => "describes how the meal was prepared"
#  ing => "describes an ingredient used in the meal"
#  trans => "likely a foreign word that needs translation"
#  adj => "this is a generic adjective"
#  region => "this is a place that describes local cuisine"
#  quant => "something that describes the quantity of food items or size"

def applyTranslations(row):
    tok = row['name'].split()
    new_tok = []
    for t in tok:
        if t in labels and labels[t][0] == "trans": t = labels[t][1]
        new_tok.append(t)
    row['name_translated'] = " ".join(new_tok)
    return row

def applyManualLabels(row):
    tok = row['name_translated'].split()
    ing = []
    prep = []
    adj = []
    region = []
    quant = []
    brand = []
    unmatched_tokens = []
    for t in tok:
        if t in labels:
            a = labels[t][0]
            if a == "del": pass
            elif a == "ing": ing.append(t)
            elif a == "trans": pass
            elif a == "prep": prep.append(t)
            elif a == "adj": adj.append(t)
            elif a == "region": region.append(t)
            elif a == "quant": quant.append(t)
            elif a == "brand": brand.append(t)
            elif a == "?" or a == "extra":
                print(tok)
                pass
            else:
                print("Unkown action {0}".format(a))
                raise Exception()
        else: unmatched_tokens.append(t)
    row['unmatched_tokens'] = " ".join(unmatched_tokens)
    row['ingredients'] = " ".join(ing)
    row['preparation'] = " ".join(prep)
    row['adjectives'] = " ".join(adj)
    row['region'] = " ".join(region)
    row['quantity'] = " ".join(quant)
    row['brand'] = " ".join(brand)
    return row

dish2 = dish.apply(applyTranslations, axis = 1)
dish3 = dish2.apply(applyManualLabels, axis = 1)
#@end convertDishToCuisine

#@begin exportData
#@desc COnvert Pandas back into CSV
#@in dish_2
#@out Dish_clean2 @URI file:../03_python/p03_disch_cleaned.csv.gz
dish3.to_csv("p03_dish_cleaned.csv.gz", compression='gzip', index = False)
#@end exportData
#@end CleanDish_python2