import random


class Dice:
    """
    Class Dice
    Permet de gérer un dé
    """
    def __init__(self, face=6):
        """
        Fonction init
        permet de régler le nombre de faces
        :param face: int : nombre de faces du dé
        """
        self.nb_faces = face
        self.mon_lancer = None

    @property
    def nb_faces(self):
        """
        Getter du nb_face
        :return: integer
        """
        return self.__nb_faces

    @nb_faces.setter
    def nb_faces(self, face):
        """
        Setter du nombre de faces
        """
        if 2 <= face <= 100:
            self.__nb_faces = face
        else:
            print("Nombre de face invalide, mise à défaut à 6")
            self.__nb_faces = 6

    def est_reussite_critique(self):
        """
        Dit si un lancer est une réussite critique
        :return: bool
        """
        return self.mon_lancer == self.nb_faces

    def est_echec_critique(self):
        """
        Dit si un lancer est un échec critique
        :return:
        """
        return self.mon_lancer == 1

    def lancer(self):
        """
        Lance une instance de dé
        :return: integer
        """
        self.mon_lancer = random.randint(1, self.nb_faces)
        if self.est_reussite_critique():
            print("Ce lancer est une réussite critique")
        elif self.est_echec_critique():
            print("Ce lancer est un ECHEC critique")
        return self.mon_lancer


if __name__ == '__main__':
    """
    Fonction de test de la classe
    """
    print("Lancer de D6")
    de_6 = Dice(6)
    for i in range(20):
        print(de_6.lancer())

    print("")
    print("Lancer de D20")
    de_20 = Dice(20)
    for i in range(20):
        print(de_20.lancer())

    print("")
    print("Gestion d'erreurs")
    de_1 = Dice(1)
