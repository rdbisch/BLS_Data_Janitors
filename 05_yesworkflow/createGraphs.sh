yw () {
    command java -jar yesworkflow-0.2.0-jar-with-dependencies.jar graph "$@" -c graph.layout=tb
}

yw master_workflow.py | dot -Tpng -o master_workflow.png
yw f04_cleanMenu_yw.py | dot -Tpng -o py_cleanMenu.png
yw ../03_python/f04_cleanDish.py | dot -Tpng -o py_cleanDish1.png
yw ../03_python/f05_cleanDish.py | dot -Tpng -o py_cleanDish2.png

# This is broken presently
# Not sure why
#yw or_dish.py | dot -Tpng -o or_dish.png
#yw or_menu.py | dot -Tpng -o or_menu.png
#yw or_menuitem.py | dot -Tpng -o or_menuitem.png
#yw or_menupage.py | dot -Tpng -o or_menupage.png

or2yw -i ../01_openrefine/Dish.json.old -o or_dish.png     -ot png -title CleanDish
or2yw -i ../01_openrefine/Menu.json     -o or_menu.png     -ot png -title CleanMenu
or2yw -i ../01_openrefine/MenuItem.json -o or_menuitem.png -ot png -title CleanMenuItem
or2yw -i ../01_openrefine/MenuPage.json -o or_menupage.png -ot png -title CleanMenuPage