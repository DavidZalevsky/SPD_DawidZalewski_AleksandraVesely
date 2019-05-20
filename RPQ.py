import datetime



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


def inicjalizacja():
    t = 0
    k = 0
    c_max = 0
    G = [];
    N = list(range(0, zadania))
    lista_pomocnicza = []
    pi = [0] * zadania
    r = mega_maszyna[0]
    p = mega_maszyna[1]
    q = mega_maszyna[2]


    globals()['r'] = r
    globals()['p'] = p
    globals()['q'] = q
    globals()['t'] = t
    globals()['k'] = k
    globals()['c_max'] = c_max
    globals()['G'] = G
    globals()['N'] = N
    globals()['lista_pomocnicza'] = lista_pomocnicza
    globals()['pi'] = pi


# --------------------------DEFINICJE--------------------------#

start = datetime.datetime.now()

czytanie_z_pliku('data.txt')
inicjalizacja()
q_kopia = q[::]
Q = []

while ((G != []) or (N != [])):

    while ((N != []) and (min(value for value in r if value != None) <= t)):
        e = min(value for value in r if value != None)
        e_arg = r.index(e)
        r[e_arg] = None

        G.append(e_arg)
        N.remove(e_arg)


    for i in range(0, len(G)):
        x = q[G[i]]
        Q.append(x)

    if G == []:
        t = min(value for value in r if value != None)

    else:
        e = max(value for value in Q if value != None)

        eq = Q.index(e)
        e_arg = G[eq]

        q_kopia[e_arg] = None

        pi[k] = e_arg
        k = k + 1
        t = t + p[e_arg]
        c_max = max(c_max, t + q[e_arg])

        G.remove(e_arg)


    Q = []


print('Czas wykonywania: ', c_max)
print('Kolejnosc: ', pi)


duration = datetime.datetime.now() - start
print(duration)
