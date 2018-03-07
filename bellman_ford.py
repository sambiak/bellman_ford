#
# 7 mars 2018
# Guillaume Augustoni
#


from copy import copy
from math import inf

def litGraphe(adr):
    """ adr est l’adresse du fichier source"""
    f=open(adr,'r')
    nbs=int(f.readline()) # nombre de sommets
    G=[[] for i in range(nbs)]
    l=f.readline()
    while l:
        d=l.split()
        s1=int(d[0]) # sommet 1
        G[s1].append([int(d[1]),int(d[2])]) # sommet 2, poids
        l=f.readline()
    f.close()
    return G



def afficheGraphe(G):
    for i, voisins in enumerate(G):
        for v, w in voisins:
            print(i, v, w)


def etape_BF(G, m, chemin):
    m2, chemin2 = [], []
    for i, voisins in enumerate(G):
        mini = m[i]
        suiv = None
        for v, w in voisins:
            if w + m[v] < mini:
                mini = w + m[v]
                suiv = v
        m2.append(mini)
        if suiv is not None:
            if chemin[suiv] is None:
                chemin2.append([suiv])
            else:
                chemin2.append([suiv] + chemin[suiv])
        else:
            chemin2.append(chemin[i])
    return m2, chemin2


def internal_BF(G, s2):
    m = [inf for i in range(len(G))]
    chemin = [None for i in range(len(G))]
    m[s2] = 0
    chemin[s2] = None
    for j in range(len(G) - 1):
        m, chemin = etape_BF(G, m, chemin)
    return m, chemin


def BF(G,s,s2):
    m, chemin = internal_BF(G, s2)
    return m[s], chemin[s]

def CycleNeg(G):
    G2 = copy(G)
    G2.append([[i, 0] for i in len(G)])
    m, chemin = internal_BF(G2, len(G))
    m2 = copy(m)
    m, chemin = etape_BF(G2, m, chemin)
    sommets_modifies = []
    if m2 != m: # s'il y a un cycle
        sommets_modifies_ini = set()
        for i, u, v in enumerate(zip(m2, m)[0:-1]): # on essaye de voir les sommets sur lesquels passe un cycle
            if u != v:
                sommets_modifies_ini.add(i)

    else:
        return None


G = litGraphe('graphe2')
afficheGraphe(G)
print(internal_BF(G, 91)[1][0])
