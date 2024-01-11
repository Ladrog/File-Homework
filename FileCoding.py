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


files = ['1.txt', '2.txt', '3.txt']


def creating_dict_files(list_files):
    dict_files = []
    for file_name in list_files:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            file = {'name': file_name,
                    'lines': num_lines
                    }
            dict_files.append(file)
    sorted_files = sorted(dict_files, key=lambda f: f['lines'])
    return sorted_files


def create_result_file(sorted_files):
    with open('result.txt', 'w') as result_file:
        for file in sorted_files:
            file_name = file['name']
            file_lines = file['lines']

            result_file.write(f'{file_name}\n')
            result_file.write(f' {file_lines}\n')

            with open(file_name, 'r') as source_file:
                result_file.write(source_file.read())
            result_file.write('\n')
    return result_file


create_result_file(creating_dict_files(files))
