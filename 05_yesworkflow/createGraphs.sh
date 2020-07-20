yw () {
    command java -jar yesworkflow-0.2.0-jar-with-dependencies.jar "$@"
}

yw extract Overall_Workflow.py -c extract.listfile > Overall_Workflow.yw
yw graph   Overall_Workflow.py -c graph.layout=tb -c graph.dotfile=Overall_Workflow.gv
cat Overall_Workflow.gv | dot -Tpng -o Overall_Workflow.png

or2yw -i ../01_openrefine/Dish.json.old -ot yw -o or_dish.yw
or2yw -i ../01_openrefine/Dish.json.old -ot gv -o or_dish.gv
or2yw -i ../01_openrefine/Dish.json.old -ot png -o or_dish.png

or2yw -i ../01_openrefine/Menu.json -ot yw -o or_menu.yw
or2yw -i ../01_openrefine/Menu.json -ot gv -o or_menu.gv
or2yw -i ../01_openrefine/Menu.json -ot png -o or_menu.png

or2yw -i ../01_openrefine/MenuPage.json -ot yw -o or_menupage.yw
or2yw -i ../01_openrefine/MenuPage.json -ot gv -o or_menupage.gv
or2yw -i ../01_openrefine/MenuPage.json -ot png -o or_menupage.png

or2yw -i ../01_openrefine/MenuItem.json -ot yw -o or_menuitem.yw
or2yw -i ../01_openrefine/MenuItem.json -ot gv -o or_menuitem.gv
or2yw -i ../01_openrefine/MenuItem.json -ot png -o or_menuitem.png

yw extract ../03_python/f04_cleanDish.py -c extract.listfile > f04_cleanDish.yw
yw graph   ../03_python/f04_cleanDish.py -c graph.layout=tb -c graph.dotfile=f04_cleanDish.gv
cat f04_cleanDish.gv | dot -Tpng -o f04_cleanDish.png

yw extract ../03_python/f05_cleanDish.py -c extract.listfile > f05_cleanDish.yw
yw graph   ../03_python/f05_cleanDish.py -c graph.layout=tb -c graph.dotfile=f05_cleanDish.gv
cat f05_cleanDish.gv | dot -Tpng -o f05_cleanDish.png

yw extract f04_cleanMenu_yw.py -c extract.listfile > f04_cleanMenu.yw
yw graph   f04_cleanMenu_yw.py -c graph.layout=tb -c graph.dotfile=f04_cleanMenu.gv
cat f04_cleanMenu.gv | dot -Tpng -o f04_cleanMenu.png
