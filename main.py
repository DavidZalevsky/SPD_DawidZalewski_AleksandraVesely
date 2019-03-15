K2MIN = 9999999
K1 = 0
K2 = 0

""" Dane dla dwoch maszyn"""
#M1 = [5, 6, 4, 2, 1]
#M2 = [1, 2, 3, 6, 7]



#pobieranie danych z pliku
file_handle = open('data.txt', 'r')

lines_list = file_handle.readlines()

pakiet, maszyna = (int(val) for val in lines_list[0].split())

dane = [[int(val) for val in line.split()] for line in lines_list[1:]]



for i in range(1, maszyna+1):
    globals()['M%s' % i] = [None]*pakiet
    j=i
    for i in range(0, pakiet):
        globals()['M%s' % j][i]=dane[i][j-1]


johnson = [None]*len(M1)
koniec=(len(M1)-1)
poczatek=0


########### Permutacje ##############

# definicja funkcji permutacji
def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for M1 in permute(xs, low + 1):
            yield M1
        for i in range(low + 1, len(xs)):
            xs[low], xs[i] = xs[i], xs[low]
            for M1 in permute(xs, low + 1):
                yield M1
            xs[low], xs[i] = xs[i], xs[low]
# koniec definicji funkcji permutacji


for p in permute([0, 1, 2, 3, 4]):
    K2 = 0
    K1 = 0
    M11 = [M1[p[0]], M1[p[1]], M1[p[2]], M1[p[3]], M1[p[4]]]
    M21 = [M2[p[0]], M2[p[1]], M2[p[2]], M2[p[3]], M2[p[4]]]

    for i in range(0, 5):
        K1 = M11[i] + K1
        if K1 >= K2:
            K2 = K1 + M21[i]
        else:
            K2 = K2 + M21[i]
    if K2MIN > K2:
        K2MIN = K2
        #print("UWAGA NOWE NAJMNIEJSZE K2:", K2 )
        #print(p)
    print("Dla permutacji ",p, "czas calkowity to ", K2)
print("Najkrotszy czas ", K2MIN)

"""

"""
########### Algorytm Johnsona ##############


for i in range(0,5):
    min1 = min(M1)
    min2 = min(M2)

    minA=min(min1,min2)

    for i in range(0,len(M1)):
        if M1[i] == minA:
            johnson[poczatek]=i
            poczatek+=1
            break

        elif M2[i] == minA and min1 != min2:
            johnson[koniec]=i
            koniec-=1
            break

    M1[i] = 999999
    M2[i] = 999999

    print(M1)
    print(M2)
    print("-----------")

print("Tabela dla algorytmu Johnsona ", johnson)

M1 = [5, 6, 4, 2, 1]
M2 = [1, 2, 3, 6, 7]

M1k = [M1[johnson[0]], M1[johnson[1]], M1[johnson[2]], M1[johnson[3]], M1[johnson[4]]]
M2k = [M2[johnson[0]], M2[johnson[1]], M2[johnson[2]], M2[johnson[3]], M2[johnson[4]]]

for i in range(0, 5):
    K1 = M1k[i] + K1
    if K1 >= K2:
        K2 = K1 + M2k[i]
    else:
        K2 = K2 + M2k[i]
if K2MIN > K2:
    K2MIN = K2

print("-------------------------------------")
print("Czas rozwiazania optymalnego", K2MIN)



########## Algorytm Johnsona dla 3 maszyn ##########

K3MIN = 9999999
K1 = 0
K2 = 0
K3 = 0


johnson = [None]*len(M1)
koniec=(len(M1)-1)
poczatek=0

M12 = [None]*len(M1)
M23 = [None]*len(M1)

for i in range(0, len(M1)):
    M12[i] = M1[i]+M2[i]
    M23[i] =  M2[i]+M3[i]
print(M12)
print(M23)


for i in range(0,len(M1)):
    min1 = min(M12)
    min2 = min(M23)

    minA=min(min1,min2)

    for i in range(0,len(M12)):
        if M12[i] == minA:
            johnson[poczatek]=i
            poczatek+=1
            break

        elif M23[i] == minA and min1 != min2:
            johnson[koniec]=i
            koniec-=1
            break

    M12[i] = 999998
    M23[i] = 999998
    print(M12)
    print(M23)
    print("---------------------")


file_handle = open('data.txt', 'r')
lines_list = file_handle.readlines()
pakiet, maszyna = (int(val) for val in lines_list[0].split())
dane = [[int(val) for val in line.split()] for line in lines_list[1:]]


for i in range(1, maszyna+1):
    globals()['M%s' % i] = [None]*pakiet
    j=i
    for i in range(0, pakiet):
        globals()['M%s' % j][i]=dane[i][j-1]


print("Tabela dla algorytmu Johnsona ", johnson)

M1k = [M1[johnson[0]], M1[johnson[1]], M1[johnson[2]], M1[johnson[3]]]
M2k = [M2[johnson[0]], M2[johnson[1]], M2[johnson[2]], M2[johnson[3]]]
M3k = [M3[johnson[0]], M3[johnson[1]], M3[johnson[2]], M3[johnson[3]]]

for i in range(0, len(M1)):
    K1 = M1k[i] + K1
    if K1 >= K2:
        K2 = K1 + M2k[i]
    else:
        K2 = K2 + M2k[i]
    if K2 >= K3:
        K3 = K2 + M3k[i]
    else:
        K3 = K3 + M3k[i]
if K3MIN > K3:
    K3MIN = K3

print("-------------------------------------")
print("Czas rozwiazania optymalnego", K3MIN)
"""