    #1. p = weź liczbę osób na dzień
    # 2. d = weź liczbę dni

    # dla każdego dnia
    # - podaj liczbę uczników
    #     dla każdego ucznia w dniu podaj id i średnią

    # złącz pary w jedną tablicę

    # znajdź max średnią
    #size = max / len(tab)
    # size = ustal ilość koszyków max średnia / ilość wszystkich uczniów

    # stwórz tablice koszyków

    # dla każdej pary (id, średnia):
    #     index = int(para[1]/size)
    #     if index != ilość uczniów:
    #         koszyki[index].append(para)
    #     else
    #         koszyki[ilość uczniów - 1].append(para)
        

    # dla każdego koszyka wykonać sortowanie po średniej

    # złączyć koszyki w jedną listę

    # wydrukować dla każdego dnia p uczniów


def bucketSort(tab, k):
    #znajdź max średnią
    top = 0
    for i in range(len(tab)):
        if(float(top) < float(tab[i][1])):
            top = tab[i][1]
    size = (max(tab) - min(tab)) / k
    koszyki = ""
    for x in range(1):
        index = (tab[x] - min(tab)) / size
        if index != len(tab):
            koszyki = tab
        else:
            koszyki[len(tab) - 1] = arr
    koszyki = tab
    posortowane = []
    for j in range(len(koszyki)):
        koszyki[j][1].sort()
        for x in tab[j]:
            posortowane.append(x)
    return posortowane

a = input().split()
p = int(a[0])
d = int(a[1])
posort = []
for i in range(d):
    arr = []
    n = int(input())
    for j in range(n):
        b = input().split()
        id = b[0]
        srednia = b[1]
        arr.append([int(id), float(srednia)])
    arr = bucketSort(arr, 3)
    for z in range(p):
        print(arr[z][0])
