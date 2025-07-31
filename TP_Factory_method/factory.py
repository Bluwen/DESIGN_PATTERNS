from abc import ABC
from enum import Enum

class Unite(Enum):
    MICRO_GRAMMES = 1
    MILI_GRAMMES = 2

class Element(ABC):
    def __init__(self, nom:str, valeur: float, unite: int):
        self.nom = nom
        self.valeur = valeur
        self.unite = Unite(unite)

class Ingredient(Element):
    TYPE = "Ingrédient"

    def __str__(self):
        return f"C'est un {self.TYPE} qui a pour nom {self.nom}, pour quantité {self.valeur} {self.unite}"

class Additif(Element):
    TYPE = "Additif"
    
    def __str__(self):
        return f"C'est un {self.TYPE} qui a pour nom {self.nom}, pour quantité {self.valeur} {self.unite}"

class Allergene(Element):
    TYPE = "Allergène"

    def __str__(self):
        return f"C'est un {self.TYPE} qui a pour nom {self.nom}, pour quantité {self.valeur} {self.unite}"

class ElementFactory:
    @staticmethod
    def create_element(type_element: str, nom_element: str, valeur_element: float, unite_element: int):
        if type_element == "Ingrédient":
            return Ingredient(nom_element, valeur_element, unite_element)
        elif type_element == "Additif":
            return Additif(nom_element, valeur_element, unite_element)
        elif type_element == "Allergène":
            return Allergene(nom_element, valeur_element, unite_element)
        else : 
            raise ValueError(f"Type d'élement inconnue: {type_element}")
