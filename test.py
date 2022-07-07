class Vehicule:
    """
    Classe Vehicule
    Mere
    """

    def __init__(self, roues):
        """
        Init
        :param roues: int
        """
        self.nb_roues = roues
        self.nom_vehicule = 'Le véhicule'

    def avancer(self):
        """
        Avancer - afficher du texte
        :return: None
        """
        print(f"{self.nom_vehicule} avance")

    def freiner(self):
        print(f"{self.nom_vehicule} freine")

    def affiche_nombre_roues(self):
        print(f"{self.nom_vehicule} a {self.nb_roues} roues")


class Voiture(Vehicule):

    def __init__(self):
        super().__init__(4)
        self.nom_vehicule = 'La voiture'

    def reculer(self):
        print(f"{self.nom_vehicule} recule")


velo = Vehicule(2)
velo.avancer()
velo.freiner()
velo.affiche_nombre_roues()

fiesta = Voiture()
fiesta.affiche_nombre_roues()
fiesta.avancer()
fiesta.freiner()
fiesta.reculer()
fiesta.affiche_nombre_roues()
