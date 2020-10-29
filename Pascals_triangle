def triangle(rows):
    for rownum in range(rows):
        newValue = 1
        PrintingList = list()
        for iteration in range(rownum):
            newValue = newValue * (rownum - iteration) * 1 / (iteration + 1)
            PrintingList.append(int(newValue))
        print('---------------------')
        print(PrintingList)
        last=PrintingList
    d=int(input(f'Какое порядковое число из последнего ряда вам нужно (отсчёт начинается с 0) : '))
    print(last[d])


d = int(input('Введите ряд : '))
triangle(d+1)
