# Create yw scripts for each of the openrefine datasets
or2yw -i ../01_openrefine/menu.json -o or_menu.yw -title "Menu.csv" -desc "or2yw conversion"
output=$(python renameTables.py or_menu.yw or_menu.1.yw 0)

or2yw -i ../01_openrefine/Dish.json.old -o or_dish.yw -title "Dish.csv" -desc "or2yw conversion"
output=$((output + 1))
output=$(python renameTables.py or_dish.yw or_dish.1.yw $output)

or2yw -i ../01_openrefine/MenuItem.json -o or_menuitem.yw -title "MenuItem.csv" -desc "or2yw conversion"
output=$((output + 1))
output=$(python renameTables.py or_menuitem.yw or_menuitem.1.yw $output)

or2yw -i ../01_openrefine/MenuPage.json -o or_menupage.yw -title "MenuPage.csv" -desc "or2yw conversion"
output=$((output + 1))
output=$(python renameTables.py or_menupage.yw or_menupage.1.yw $output)

cp or_menu.1.yw or_menu.2.yw
cp or_dish.1.yw or_dish.2.yw
cp or_menuitem.1.yw or_menuitem.2.yw
cp or_menupage.1.yw or_menupage.2.yw

