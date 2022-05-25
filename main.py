import os
# Создание словаря рецептов
def recording_recipes(file_recip):
    result = {}
    with open(file_recip, encoding='utf-8')as f:
        for line in f:
            dish = line.strip()
            quantity = int(f.readline().strip())
            structure = []
            for item in range(quantity):
                ingredients = {}
                data = f.readline().strip().split(' | ')
                ingredients['ingredient_name'] = data[0]
                ingredients['quantity'] = int(data[1])
                ingredients['measure'] = data[2]
                structure.append(ingredients)
            result[dish] = structure
            f.readline()
    return result
#
#
# # Создание списка покупок
def get_shop_list_by_dishes(dishes, person_count, recipes):
    result = {}
    for dish in dishes:
        if dish in recipes:
            for structure in recipes[dish]:
                if structure['ingredient_name']  not in result:
                    product = structure['ingredient_name']
                    quantity_product = {}
                    quantity_product['measure'] = structure['measure']
                    quantity_product['quantity'] = person_count * structure['quantity']
                    result[product] = quantity_product
                else:
                    result[structure['ingredient_name']]['quantity'] += structure['quantity'] * person_count
    return result


cook_book = recording_recipes('recipes.txt')
my_shop_list = get_shop_list_by_dishes(["Омлет", "Омлет"], 2, cook_book)


# 3 задание
file_direct = os.path.join(os.getcwd(), 'folder')    # папка с файлами
files_list = os.listdir(file_direct)     # файлы для склеивания


def combining_files(files_list):
    sorted_list = []
    for i in files_list:
        with open(os.path.join(file_direct, i), encoding='utf-8') as f:
            sorted_list.append((i, len(f.readlines())))
    sorted_list.sort(key=lambda x: x[1])
    f = open('result.txt', 'w', encoding='utf-8')
    for name_lenght in sorted_list:
        with open(os.path.join(file_direct, name_lenght[0]), encoding='utf-8') as current_file:
            print(name_lenght[0] + '\n' + str(name_lenght[1]), file=f)
            for line in current_file:
                print(line.rstrip(), file=f)
    f.close()
# combining_files(files_list) вызов склеивания