import datetime
start = datetime.datetime.now()
#algorytm


K2MIN = 9999999
K1 = 0
K2 = 0


def czytanie_z_pliku(plik):
    mega_maszyna = []

    file_handle = open(plik, 'r')

    lines_list = file_handle.readlines()

    zadania, maszyna = (int(val) for val in lines_list[0].split())
    globals()['zadania'] = zadania
    globals()['maszyna'] = maszyna

    mega_kursor = [0] * maszyna
    globals()['mega_kursor'] = mega_kursor

    dane = [[int(val) for val in line.split()] for line in lines_list[1:]]
    globals()['dane'] = dane

    for i in range(1, maszyna + 1):
        mini_maszyna = [0] * zadania
        globals()['M%s' % i] = [0] * zadania
        globals()['K%s' % i] = 0
        j = i
        for i in range(0, zadania):
            mini_maszyna[i] = dane[i][j - 1]
            globals()['M%s' % j][i] = dane[i][j - 1]
        mega_maszyna.append(mini_maszyna)
    globals()['mega_maszyna'] = mega_maszyna


def liczenie_mega_kursora(dane):
    mega_kursor = [0] * maszyna

    for i in range(0, len(dane)):
        mega_kursor[0] = mega_maszyna[0][dane[i]] + mega_kursor[0]

        for j in range(0, maszyna):
            if j != (maszyna - 1):
                if mega_kursor[j] >= mega_kursor[j + 1]:
                    mega_kursor[j + 1] = mega_kursor[j] + mega_maszyna[j + 1][dane[i]]
                else:
                    mega_kursor[j + 1] = mega_kursor[j + 1] + mega_maszyna[j + 1][dane[i]]

        kursor_max = max(mega_kursor)

    globals()['kursor_max'] = kursor_max


# pobieranie danych z pliku
file_handle = open('data.txt', 'r')

lines_list = file_handle.readlines()

pakiet, maszyna = (int(val) for val in lines_list[0].split())

dane = [[int(val) for val in line.split()] for line in lines_list[1:]]

for i in range(1, maszyna + 1):
    globals()['M%s' % i] = [None] * pakiet
    j = i
    for i in range(0, pakiet):
        globals()['M%s' % j][i] = dane[i][j - 1]

print(M1)

johnson = [None] * len(M1)
koniec = (len(M1) - 1)
poczatek = 0

########## Algorytm Johnsona dla 3 maszyn ##########

K3MIN = 9999999
K1 = 0
K2 = 0
K3 = 0

johnson = [None] * len(M1)
koniec = (len(M1) - 1)
poczatek = 0

M12 = [None] * len(M1)
M23 = [None] * len(M1)

for i in range(0, len(M1)):
    M12[i] = M1[i] + M2[i]
    M23[i] = M2[i] + M3[i]
print(M12)
print(M23)

for i in range(0, len(M1)):
    min1 = min(M12)
    min2 = min(M23)

    minA = min(min1, min2)

    for i in range(0, len(M12)):
        if M12[i] == minA:
            johnson[poczatek] = i
            poczatek += 1
            break

        elif M23[i] == minA and min1 != min2:
            johnson[koniec] = i
            koniec -= 1
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

for i in range(1, maszyna + 1):
    globals()['M%s' % i] = [None] * pakiet
    j = i
    for i in range(0, pakiet):
        globals()['M%s' % j][i] = dane[i][j - 1]

print("Tabela dla algorytmu Johnsona ", johnson)



czytanie_z_pliku("data.txt")
liczenie_mega_kursora(johnson)

print("-------------------------------------")
print("Czas rozwiazania optymalnego", kursor_max)


duration = datetime.datetime.now() - start
print(duration)