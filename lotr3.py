import random


def citer_chaque_lieu_alea(liste_lieux):
    """
    Fait un print de la liste en entrée, en ordre aléatoire
    :param liste_lieux: list
    :return: None
    """
    try:
        list_randomized = random.sample(liste_lieux, len(liste_lieux))
        # brandom.shuffle(liste_lieux)
        # print(liste_lieux)
        print(list_randomized)
    except TypeError:
        print(" ### ERREUR - Le parametre en entrée n'est pas une liste")


def citer_lieu_connu(lieu, liste_lieux):
    """
    Voit si un lieu fait partie de la TM
    :param lieu: string
    :param liste_lieux: list
    :return:
    """
    if len(liste_lieux) < 4:
        raise NameError(" ### ERREUR - La liste des lieux doit contenir au moins 4 lieux ")
    # on met la liste en minusucle
    liste_lieux_min = []
    for temp_lieu in liste_lieux:
        liste_lieux_min.append(temp_lieu.lower())
    if lieu.lower() in liste_lieux_min:
        print(f"Le lieu {lieu} fait partie de la terre du milieu")
    else:
        print(f"Le lieu {lieu} ne fait pas partie de la terre du milieu")


# tests
liste_lieux_tm = ['La Comté', 'Le Gondor', 'Le Mordor', 'Le Rohan']
liste_lieux_tm_court = ['La Comté', 'Le Gondor', 'Le Rohan']
citer_chaque_lieu_alea(liste_lieux_tm)
# print("------")
# print(liste_lieux_tm)

citer_chaque_lieu_alea(1)

citer_lieu_connu("Howgarts", liste_lieux_tm)
citer_lieu_connu("le mOrdOr", liste_lieux_tm)
citer_lieu_connu("le mordor", liste_lieux_tm_court)



