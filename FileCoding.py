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

print(read_file('dishes.txt'))










