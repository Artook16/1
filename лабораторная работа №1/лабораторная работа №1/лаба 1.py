def f():

    massive = []
    for a in range(100, 10000):
        a_str = str(a)
        kolichestvo_a = len(a_str)

        # Проверка
        if ( kolichestvo_a > 3 and a_str[1]== '0' and a_str[-2] == '0' and a % 2 != 0):
            massive.append(a)

    # Вывод результатов
    if massive:
        print("Найденные числа:")
        for a in massive:
            print(a)

        # Получение списка цифр
        isp_cifra = set()
        for a in massive:
            for cifra in str(a):
                isp_cifra.add(cifra)

        # Вывод цифр прописью
        print("Использованные цифры:")
        cifra_propis = {
            '0': 'ноль',
            '1': 'один',
            '2': 'два',
            '3': 'три',
            '4': 'четыре',
            '5': 'пять',
            '6': 'шесть',
            '7': 'семь',
            '8': 'восемь',
            '9': 'девять',
        }

        propis = [propis[cifra] for cifra in sorted(isp_cifra)] # Сортировка для детерминированного порядка
        print(", ".join(cifra_propis))
    else:
        print("Числа, не найдены.")


f()