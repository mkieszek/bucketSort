from operator import itemgetter


def bucketSort(tab):
    #znajdź max średnią
    min = 100
    for i in range(len(tab)):
        if(min >= tab[i][1]):
            min = tab[i][1]

    size = int(len(tab) / min)

    koszyki = []

    for i in range(size):
        koszyki.append([])

    for element in tab:
        index = int((element[1])/ size)

        if index != size:
            koszyki[index].append(element)
        else:
            koszyki[size - 1].append(element)
    
    posortowane = []
    
    for koszyk in koszyki:
        posortowanyKoszyk = sorted(koszyk, key=itemgetter(1))
        for element in posortowanyKoszyk:
            posortowane.append(element)

    return posortowane

a = input().split()
p = int(a[0])
d = int(a[1])
posort = []

arr = []
    
for i in range(d):
    n = int(input())
    for j in range(n):
        b = input().split()
        id = b[0]
        srednia = b[1]
        arr.append([int(id), float(srednia)])

posort = bucketSort(arr)

i = 0
for dzien in range(d):
    for uczen in range(p):
        print(posort[i], end= ' ')
        i = i + 1
    print()
