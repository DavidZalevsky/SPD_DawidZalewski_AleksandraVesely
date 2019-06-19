import math


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


def inicjalizacja_zerowa():
    r = mega_maszyna[0]
    p = mega_maszyna[1]
    q = mega_maszyna[2]

    globals()['r'] = r
    globals()['p'] = p
    globals()['q'] = q

    r_org = mega_maszyna[0][::]
    p_org = mega_maszyna[1][::]
    q_org = mega_maszyna[2][::]

    globals()['r_org'] = r_org
    globals()['p_org'] = p_org
    globals()['q_org'] = q_org


def schrage(r_org, p_org, q_org):
    t = 0
    k = 0
    c_max = 0
    G = [];
    N = list(range(0, zadania))
    lista_pomocnicza = []
    pi = [0] * zadania
    Q = []
    l = 0
    test = 0

    r = r_org[::]
    p = p_org[::]
    q = q_org[::]

    q_kopia = q[::]

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
            b_pre = 0

        else:

            e = max(value for value in Q if value != None)

            eq = Q.index(e)
            e_arg = G[eq]

            q_kopia[e_arg] = None

            pi[k] = e_arg
            k = k + 1
            t = t + p[e_arg]
            c_max = max(c_max, t + q[e_arg])

            # MECHANIZM LICZENIA B:

            if t + q[e_arg] >= c_max:
                b_pre = test


            # KONIEC
            test += 1

            G.remove(e_arg)

        globals()['b_pre'] = b_pre
        globals()['c_max'] = c_max
        globals()['pi'] = pi
        #globals()['e_arg'] = e_arg
        Q = []
    print('Czas wykonywania: ', c_max)


def schrage_ptm(r_org, p_org, q_org):
    t = 0
    k = 0
    c_max = 0
    G = [];
    N = list(range(0, zadania))
    lista_pomocnicza = []
    pi = [0] * zadania

    Q = []
    l = 0

    r = r_org[::]
    p = p_org[::]
    q = q_org[::]

    q_kopia = q[::]

    while ((G != []) or (N != [])):

        while ((N != []) and (min(value for value in r if value != None) <= t)):
            e = min(value for value in r if value != None)
            e_arg = r.index(e)

            G.append(e_arg)
            N.remove(e_arg)

            if q[e_arg] > q[l]:
                p[l] = t - r[e_arg]
                t = r[e_arg]
                if p[l] > 0:
                    G.append(l)

            r[e_arg] = None

            if q[0] == math.inf:
                q[0] = q_core[0]

        for i in range(0, len(G)):
            x = q[G[i]]
            Q.append(x)

        if G == []:
            t = min(value for value in r if value != None)

        else:
            e = max(value for value in Q if value != None)

            eq = Q.index(e)
            e_arg = G[eq]

            l = e_arg
            t = t + p[e_arg]
            c_max = max(c_max, t + q[e_arg])

            G.remove(e_arg)

        Q = []
        P = mega_maszyna[1]

    print('Czas wykonywania: ', c_max)



# ---------------------  INICJALIZACJA  ---------------------

UB = 10000000
czytanie_z_pliku("data2.txt")
inicjalizacja_zerowa()


# ---------------------------  1  ---------------------------
def carier(UB):

    schrage(r, p, q)
    U = c_max

    # ---------------------------  2  ---------------------------

    if U < UB:
        UB = U
        pi_nowe = pi[::]

    # ---------------------------  3  ---------------------------
    ### b

    b = pi[b_pre]

    ### a
    r_a = r[::]
    p_a = p[::]
    q_a = q[::]
    p_as = 0
    brakuje_mi_zmiennych_xd = []



    for i in range(0, zadania):
        for s in range(0, b):
            p_as = p_a[s] + p_as

        liczba_a = r_a[i] + p_as + q_a[b]
        brakuje_mi_zmiennych_xd.append(liczba_a)

    for i in range(0, zadania):
        if brakuje_mi_zmiennych_xd[i] == min(brakuje_mi_zmiennych_xd):
            a = i

    a = pi[a]

    a_arg = pi.index(a)
    b_arg = pi.index(b)

    ### c
    for i in range(a_arg,b_arg):

        if q_a[i] < q_a[b]:
            c_arg = i
            c = pi[c_arg]
        else:
            c = None

    #print(a, b, c)
    # ---------------------------  4  ---------------------------
    if c == None:
        print("Program zakonczony, czas wykonania to:", UB, pi_nowe)
        return

    # ---------------------------  5  ---------------------------
    # r prim
    r_prim = []

    if c<b:
        for i in range(c + 1, b + 1):
            r_prim.append(r[i])
    else:
        r_prim.append(r[b])

    r_prim = min(r_prim)

    # q prim
    q_prim = []

    if c < b:
        for i in range(c + 1, b + 1):
            q_prim.append(q[i])
    else:
        q_prim.append(q[b])

    q_prim = min(q_prim)

    # p_prim

    p_prim = 0
    for i in range(c + 1, b + 1):
        p_prim = p_prim + p[i]

    # ---------------------------  6  ---------------------------
    r_poprzednie = r[c]
    r[c] = max(r[c], r_prim + p_prim)

    # ---------------------------  7  ---------------------------
    schrage_ptm(r, p, q)
    LB = c_max

    globals()['UB'] = UB
    # ---------------------------  8  ---------------------------

    if LB < UB:

    # ---------------------------  9  ---------------------------

        carier(UB)

    # ---------------------------  10  ---------------------------
    r[c] = r_poprzednie

    # ---------------------------  11  ---------------------------
    q_poprzednie = q[c]
    q[c] = max(q[c], q_prim + p_prim)

    # ---------------------------  12  ---------------------------

    schrage_ptm(r, p, q)
    LB = c_max

    # ---------------------------  13  ---------------------------
    if LB < UB:
        # ---------------------------  14  ---------------------------
        Carlier()

    # ---------------------------  15  ---------------------------
    q[c] = q_poprzednie

    globals()['pi_nowe'] = pi_nowe


carier(UB)

# print('Czas wykonania:', UB)


# dziala dla 5 i 1, dla 7 i 8 jest roznica 1