############################
# Exercice 1
############################

diviseur = 'abc'

try:
    resultat = 10 / diviseur
except ZeroDivisionError:
    print("Erreur, division par 0 !")
except TypeError:
    print("Erreur, le diviseur n'est pas un nombre")

############################
# Exercice 2
############################
blog_posts = [
    {'Photos': 3, 'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Photos': 5, 'Comments': 8, 'Shares': 3},
]
likes = 0
for post in blog_posts:
    try:
        likes += post['Likes']
    except KeyError:
        post['Likes'] = 0
    print(f"nombre de likes : {likes}")
print(f"nombre de likes : {likes}")
print("####### DEBUG ############")
print(blog_posts)


#############################
# Exercice 3
#############################
def dire_bonjour(nom):
    """
    Dit bonjour à nom...
    :param nom: string
    :return: None
    """
    if nom == '':
        raise NameError("Le nom ne doit pas être vide")
    print(f"Bonjour {nom}")


#############################
# Exercice 4
#############################
def calculer_moyenne_eleve(liste_notes):
    """
    Calcule la moyenne des notes passées en liste
    :param liste_notes: list (integers)
    :return: float
    """
    if len(liste_notes) < 3:
        raise NameError("Le calcul ne peut pas se faire à moins de 3 notes")
    try:
        return sum(liste_notes)/len(liste_notes)
    except TypeError:
        raise NameError("Erreur de type")


##############################
# Lancements
##############################

dire_bonjour("Steph")
try:
    dire_bonjour("")
except NameError:
    print(" *** Le nom ne doit pas être vide !")
# dire_bonjour("")

print(calculer_moyenne_eleve([10, 12, 42]))
try:
    print(calculer_moyenne_eleve([10, 12]))
except NameError as err:
    print(f" *** Pas assez de notes pour faire le calcul : {err}")

try:
    print(calculer_moyenne_eleve([10, 12, 'a']))
except NameError as err:
    print(err)
    if err == "Erreur de type":
        print(f"CA MARCHE")
    else:
        print(f"Pas bon {err}")
