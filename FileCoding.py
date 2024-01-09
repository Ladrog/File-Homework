def read_file(file_name):
    cook_book = {}
    with open(file_name, 'r', encoding='UTF-8') as file:
        dish_name = ''
        for line in file:
            line = line.strip()
            if len(line) == 0:
                continue
            if '|' not in line:
                if line.isdigit():
                    continue
                dish_name = line
                cook_book[dish_name] = []
            else:
                ingredient = line.split('|')
                ingredient_name = ingredient[0].strip()
                ingredient_quantity = int(ingredient[1].strip())
                ingredient_measure = ingredient[2].strip()
                ingredient_dict = {
                    'ingredient_name': ingredient_name,
                    'quantity': ingredient_quantity,
                    'measure': ingredient_measure
                }
                cook_book[dish_name].append(ingredient_dict)
    return cook_book

# print(read_file('dishes.txt'))

def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for food in dishes:
        for food_name in cook_book.keys():
            if food == food_name:
                for ingredient in cook_book[food_name]:
                    key = ingredient['ingredient_name']
                    ingredient_quantity = ingredient['quantity'] * person_count
                    ingredient_measure = ingredient['measure']
                    shop_list[key] = {'measure': ingredient_measure,
                                      'quantity': ingredient_quantity
                                      }
    return shop_list


result = read_file('dishes.txt')
print(get_shop_list_by_dishes(result, ['Омлет', 'Запеченный картофель'], 2))











