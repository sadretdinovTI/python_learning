count_food = int(input('Кол-во еды: '))
holodilnik = set()

for i in range(count_food):
    food_name = input('Еда: ')
    holodilnik.add(food_name)

count_recipes = int(input('Кол-во рецептов'))
for i in range(count_recipes):
    recipe_name = input('Рецепт: ')
    ingredients = int(input('Кол-во ингрединетов: '))
    set_ingredients = set()
    for j in range(ingredients):
        ingredient_name = input('Имя продукта: ')
        set_ingredients.add(ingredient_name)
    if set_ingredients <= holodilnik:
        print(recipe_name)

