# def sort(ids, avgs):
#     a = []
#     for i in range(3):
#         ks = []
#         a.append(ks)
#     for i in range(len(avgs)):
#         if arr[i] == max(arr):
#             a[k-1].append(max(arr))
#         else:
#             b = (arr[i] - min(arr)) // (max(arr)/k)
#             a[int(b)].append(arr[i])
#     tab = []
#     for i in range(k):
#         a[i].sort()
#         for n in range(len(a[i])):
#             tab.append(a[i][n])

def bucketSort(tab):
    #znajdź max średnią
    max = 0
    for i in range(len(tab)):
        if(str(max) < float(tab[i][1])):
            max = tab[i][1]
    size = int(len(tab) / max)
    tablica = []
    for i in range(3):
        koszyki = []
        tablica.append(koszyki)
    for x in range(len(tab)):
        index = int(tab[1]/size)
        if index != len(tab):
            koszyki[index].append(tab)
        else:
            koszyki[len(tab) - 1].append(c)
    for j in range(len(koszyki)):
        koszyki.sort()
    tab.append(koszyki)

    
    


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

a = input().split()
p = int(a[0])
d = int(a[1])
posort = []
for i in range(d):
    tab = []
    n = int(input())
    for j in range(n):
        b = input()
        tab.append(b)
    c = []
    for x in range(len(tab)):
        c.append(tab[x].split())
    bucketSort(c)
    for z in range(p):
        print(c[z])
