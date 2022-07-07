import random


########################
# Boucles
########################
nb_jour_trajet = 40
for i in range(nb_jour_trajet, -1, -1):
    pluriel = ''
    if i >= 2:
        pluriel = 's'
    print(f"Plus que {i} jour{pluriel} de trajet !")


#########################
# Fonctions 1
#########################
def est_dans_la_communaute(nom):
    """
    :param nom: Nom a rechercher
    :return: Bool - vrai si nom dans la liste
    """
    liste_nom = ['aragorn', 'boromir', 'frodon', 'gandalf', 'gimli', 'legolas', 'merry', 'pippin', 'sam']
    return nom.lower() in liste_nom


###########################
# Fonction 2
###########################
def le_plus_petit(mon_dict):
    """
    Retourne l'espèce la plus petite
    :param mon_dict: dict
    :return: string
    """
    plus_petit = list(mon_dict.values())[0]
    espece = ''
    for key, val in mon_dict.items():
        if val < plus_petit:
            espece = key
            plus_petit = val
    print(f"Le plus petit est {espece}")


def le_plus_petit2(mon_dict):
    """
    Retourne une liste des espèces les plus petites
    :param mon_dict: dict
    :return: list
    """
    list_sorted = sorted(mon_dict.items(), key=lambda item: item[1])
    taille_la_plus_petite = list_sorted[0][1]
    espece = []
    x = 0
    while list_sorted[x][1] == taille_la_plus_petite and x < len(list_sorted):
        espece.append(list_sorted[x][0])
        x += 1
    print(espece)


def le_plus_petit3(mon_dict):
    """
    Retourne une liste des espèces les plus petites
    :param mon_dict: dict
    :return: list
    """
    list_sorted = sorted(mon_dict.items(), key=lambda item: item[1])
    taille_la_plus_petite = list_sorted[0][1]

    liste_especes_petites = [espece for espece, taille in mon_dict.items() if taille == taille_la_plus_petite]
    print(liste_especes_petites)


###########################
# Module random
###########################
def citer_lieu_alea(var_liste_lieux):
    """
    retourne un lieu parmi ceux de la liste
    :param var_liste_lieux: liste de lieux en entrée
    :return: string - le lieu choisi
    """
    return var_liste_lieux[random.randint(0, len(var_liste_lieux) - 1)]


###########################
# Tests
###########################
print(est_dans_la_communaute('BoRoMir'))
print(est_dans_la_communaute('toto'))
liste_lieux = ['La Comté', 'Le Gondor', 'Le Mordor', 'Le Rohan']
for i in range(1, 20, 1):
    print(citer_lieu_alea(liste_lieux))

taille_espece = {
    "nain": 130,
    "elfe": 190,
    "hobbit": 90,
    "petit_hobbit": 90,
}
le_plus_petit(taille_espece)
le_plus_petit2(taille_espece)
le_plus_petit3(taille_espece)

print(f"{taille_espece}")
