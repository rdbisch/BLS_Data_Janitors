# Dummy Pyhon to encapsulate overall workflow.
#@begin CS513 BLS Data Janitors
#@desc Clean NYPL Menus Datasets
#@in Menu @URI file:../raw_data/Menu.csv.gz
#@in Dish @URI file:../raw_data/Dish.csv.gz
#@in MenuItem @URI file:../raw_data/MenuItem.csv.gz
#@in MenuPage @URI file:../raw_data/MenuPage.csv.gz

#@begin CleanMenu
#@desc OpenRefine.  Need brief Explanation from Stanely.  See detail {TBD LINK}.
#@in Menu
#@out Menu_clean @URI file:../01_openrefine/Menu_clean.csv.gz
#@end CleanMenu

#@begin CleanDish
#@desc OpenRefine. Need brief Explanation from Stanely.  See detail {TBD LINK}.
#@in Dish
#@out Dish_clean @URI file:../01_openrefine/Dish_clean.csv.gz
#@end CleanDish

#@begin CleanMenuItem
#@desc OpenRefine.  Need brief Explanation from Stanely.  See detail {TBD LINK}.
#@in MenuItem
#@out MenuItem_clean @URI file:../01_openrefine/MenuItem_clean.csv.gz
#@end CleanMenuItem

#@begin CleanMenuPage
#@desc OpenRefine.  Need brief Explanation from Stanely.  See detail {TBD LINK}.
#@in MenuPage
#@out MenuPage_clean @URI file:../01_openrefine/MenuPage_clean.csv.gz
#@end CleanMenuPage

#@begin CleanDish_python1
#@desc Python.  Deduplicates dish names after cleaning.   See detail {TBD LINK}.
#@in Dish_clean
#@in MenuItem_clean
#@out tokens @URI file:../03_pyhton/tokens.csv
#@out Dish_clean_dedup
#@out MenuItem_clean2 @URI file:../03_python/p02_MenuItem_cleaned.csv.gz
#@end CleanDish_python1

#@begin CleanMenu_python1
#@desc Python.  Deeper cleaning and information extract of Menu.  See detail {TBD LINK}.
#@in Menu_clean
#@out Menu_clean2 @URI file:../03_pyhton/p02_menu_cleaned.csv.gz
#@end CleanMenu_python1

#@begin CleanDish_Manual
#@desc Manual step of data cleaning. Extracted tokens from dish and manually labelled.
#@in tokens
#@out tokens_cleaned @URI file:../03_python/tokens_cleaned.csv
#@end CleanDish_Manual

#@begin CleanDish_python2
#@desc Python.  Extracting cuisine information from dish name.  See detail {TBD LINK}.
#@in Dish_clean_dedup
#@in tokens_cleaned @URI file:../03_python/tokens_cleaned.csv
#@out Dish_clean2 @URI file:../03_python/p03_disch_cleaned.csv.gz
#@end CleanDish_Manual

#@begin Import_Dish
#@desc SQLite.  Import csv file into SQL database.
#@in Dish_clean2
#@out dish_table
#@end Import_Dish

#@begin Import_Menu
#@desc SQLite.  Import csv file into SQL database.
#@in Menu_clean2
#@out menu_table
#@end Import_Menu

#@begin Import_MenuItem
#@desc SQLite.  Import csv file into SQL database.
#@in MenuItem_clean2
#@out menuitem_table
#@end Import_MenuItem

#@out dish_table
#@out menu_table
#@out menuitem_table
#@end CS513 BLS Data Janitors