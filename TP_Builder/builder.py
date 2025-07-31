from enum import Enum
from TP_Factory_method import Additif, Allergene, Ingredient

class Categorie:
    def __init__(self, nom:str):
        self.nom = nom

class Marque:
    def __init__(self, nom:str):
        self.nom = nom

class Grade(Enum):
    A=1
    B=2
    C=3
    D=4
    E=5
    F=6

class Produit:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def affichage_partie(self):
        print("Voici de quoi est composé le produit : ")
        for parts in self.parts:
            print(parts)

class ProduitBulder:
    def __init__(self):
        self._produit = Produit()
    
    def definir_info_produit(self, nom:str, grade: int):
        self._produit.add(nom)
        self._produit.add(Grade(grade))
        return self
    
    def ajouter_additif(self, nom:str, valeur:int, unite:int = 2):
        self._produit.add(Additif(nom, valeur, unite))
        return self
    
    def ajouter_allergene(self, nom:str, valeur:int, unite:int = 2):
        self._produit.add(Allergene(nom, valeur, unite))
        return self
    
    def ajouter_ingredient(self, nom:str, valeur:int, unite:int = 2):
        self._produit.add(Ingredient(nom, valeur, unite))
        return self
    
    def ajouter_marque(self, nom:str):
        self._produit.add(Marque(nom))
        return self
    
    def ajouter_categorie(self, nom:str):
        self._produit.add(Categorie(nom))

    def build(self):
        return self._produit

