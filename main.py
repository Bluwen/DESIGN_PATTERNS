from TP_Builder.builder import ProduitBulder
from TP_Factory_method import ElementFactory

### Par for factory
# element1 = ElementFactory.create_element("Additif", "E512", 147.2, 1)
# print(element1)
# element2 = ElementFactory.create_element("Ingrédient", "Chataigne", 20.2, 2)
# print(element2)
# element3 = ElementFactory.create_element("Allergène", "Pomme", 2.0, 2)
# print(element3)

##Part for builder

builder = ProduitBulder()

produit1 = builder.definir_info_produit("Un premier produit", 2).ajouter_additif("collagene", 4).ajouter_allergene("pomme", 14.0).build()

produit1.affichage_partie()