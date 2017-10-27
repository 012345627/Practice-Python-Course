'''2. В одном файле в каждой строке записаны координаты пар точек. Каждая координата отделена от другой пробелом.
 Например, строка вида 3 6 -2 4 означает, что координаты первой точки (3;6), второй - (-2;4).
 Во второй файл требуется построчно записать наибольшее и наименьшее расстояние между точками.'''

coordinates = []
distance = 0
distance_list = []
'''если не сможем открыть файл, то обрабатываем соответсвтующее исключение.
если в файле не строки с цифрами, то получим ValueError и обработаем его'''
try:
    with open("/media/sergio/file-1.txt") as file_1:
        for line in file_1.readlines():
            coordinates = line.split();
            try:
                x1, y1, x2, y2 = coordinates
                distance = ((int(x2)-int(x1))**2 + (int(y2)-int(y1))**2)**.5
            except ValueError:
                print("Содержание файла не соответствует заданию, измените содержание!")
            distance_list.append(distance)
except IOError:
    print("Проверьте существует ли файл и верно ли указан путь к нему!")
else:
    max_distance = max(distance_list)
    min_distance = min(distance_list)
    try:
        with open("/media/sergio/file-2.txt", 'w') as file_2:
            file_2.writelines(str(max_distance)+"\n")
            file_2.writelines(str(min_distance))
    except IOError:
        print("Укажите верный путь ко второму файлу!")
