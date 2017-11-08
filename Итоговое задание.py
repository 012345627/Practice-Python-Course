'''1.Дан файл с пунктами меню (id, название, id родителя). Если id родителя равно 0, то родителя не существует. Показать полное меню с отступами. Пользователь вводит id пункта. Показать цепочку из пунктов меню до этого пункта. Уровней вложенности в меню может быть любое количество. '''
menus=[]; id_elem_list=[]; id_parent_list=[]; otstup_list=[]; path_to_elem=[];
try:
	with open("c:/file-1.txt") as file_1:
		lst = file_1.read().splitlines()
except IOError:
  print("Проверьте существует ли файл и верно ли указан путь к нему!")
"""Преобразуем полученый список строк в список со списками"""
for line in lst:
    menus.append( line.split(',') )
for menu in menus:
    id_elem, name, id_parent = menu
    id_elem_list.append(int(id_elem))
    id_parent_list.append(int(id_parent))
    otstup_list.append(0)
"""Запускаем цикл поиска дочерних элементов у каджого элемента начиная с
корневых и рассчитываем отступ для каждого элемента"""
for index, menu in enumerate(menus):
    id_elem, name, id_parent = menu
    if int(id_parent)==0:
        for child_index, id_parent in enumerate(id_parent_list):
            if id_parent==int(id_elem):
                id_elem=id_elem_list[child_index]
                otstup_list[child_index]=otstup_list[index]+1
try:
	with open("c:/file-2.txt", 'w') as file:
		for index, item in enumerate(lst):
			print(otstup_list[index]*" "+item, file=file)
except IOError:
  print("Проверьте существует ли файл и верно ли указан путь к нему!")

print("Полжалуйста,введите id элемента,чтобы получить цепочку элементов до него:")
id_find=int(input())
"""Получаем от юзера id и добавляем все родительские элементы в список path_to_elem"""
for index, menu in enumerate(menus):
    id_elem, name, id_parent = menu
    if int(id_elem)==id_find:
        path_to_elem.append(menu)
        for child_index, id_elem in reversed(list(enumerate(id_elem_list))):
            if id_elem==int(id_parent):
                path_to_elem.append(menus[child_index])
                id_parent=id_parent_list[child_index]
for item  in reversed(path_to_elem):
    print(item)
