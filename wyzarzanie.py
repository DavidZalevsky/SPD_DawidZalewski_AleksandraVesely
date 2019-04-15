import random
from random import shuffle
from math import exp
import datetime

start = datetime.datetime.now()


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

        c_max = max(mega_kursor)
        globals()['c_max'] = c_max

    globals()['c_max'] = c_max


def inicjalizacja():
    T = 40
    kolejnosc = [5 ,  2,  16,   7 , 18 , 14,  11,  8 , 9  ,15  , 0 ,  1 ,12 , 4  , 6  ,17,   3 , 10,  19,  13 ]

    #list(range(0, zadania))
    #shuffle(kolejnosc)
    print("----------Inicjalizacja ----------")
    print(kolejnosc)
    print("Temperatura to: ", T)
    globals()['kolejnosc'] = kolejnosc
    globals()['T'] = T


def generowanie_ruchu():
    print("----------Stary Ruch----------")
    r = random.randint(2, zadania) - 1
    kolejnosc_temp1 = kolejnosc[::]
    kolejnosc_temp1[0], kolejnosc_temp1[r] = kolejnosc_temp1[r], kolejnosc_temp1[0]
    print(kolejnosc_temp1)  # 1111
    print("Losowy numer zamiany to", r)
    liczenie_mega_kursora(kolejnosc_temp1)
    print("cmax to:", c_max)
    c_max_stare = c_max

    print("----------Nowy Ruch----------")
    r = random.randint(2, zadania) - 1
    kolejnosc_temp2 = kolejnosc[::]
    kolejnosc_temp2[0], kolejnosc_temp2[r] = kolejnosc_temp2[r], kolejnosc_temp2[0]
    print(kolejnosc_temp2)  # 1111
    print("Losowy numer zamiany to", r)
    liczenie_mega_kursora(kolejnosc_temp2)
    print("cmax to:", c_max)
    c_max_nowe = c_max

    globals()['kolejnosc_temp1'] = kolejnosc_temp1
    globals()['kolejnosc_temp2'] = kolejnosc_temp2
    globals()['c_max_nowe'] = c_max_nowe
    globals()['c_max_stare'] = c_max_stare


def wykonanie_lub_nie_ruchu(kolejnosc, T):
    if c_max_nowe < c_max_stare:
        p1 = 1
        p2 = 0
    else:
        p1 = 0
        p2 = exp((c_max_stare - c_max_nowe) / T)

    if p1 >= 1:
        kolejnosc = kolejnosc_temp2[::]

    elif p2 >= 1:
        kolejnosc = kolejnosc_temp1[::]

    T = T * 0.95

    print("----------Wykonanie Ruchu----------")

    liczenie_mega_kursora(kolejnosc)
    print("cmax to:", c_max)

    print("Temperatura to: ", T)
    print("Po wykonaniu ruchu kolejnosc to:", kolejnosc)

    globals()['kolejnosc'] = kolejnosc
    globals()['T'] = T


# ----------------------------------DEFINICJE----------------------------------


czytanie_z_pliku("data.txt")

inicjalizacja()

for i in range(0, 20):
    generowanie_ruchu()
    wykonanie_lub_nie_ruchu(kolejnosc, T)

duration = datetime.datetime.now() - start
print("Czas obliczen to:", duration)