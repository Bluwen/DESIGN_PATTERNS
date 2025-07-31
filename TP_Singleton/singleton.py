class Singleton:
    _instance = None
    _intialized = False
    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            return cls._instance
    
    def __init__(self):
        if self._intialized:
            return
        self._intialized = True
        self._config = []
        self.lecture_fichier()

    def lecture_fichier(self):
        with open(r"TP_Singleton\configuration.ini", "r") as f: 
            for ligne in f: 
                ligne = ligne.strip()
                self._config.append(ligne)
        

fichier = Singleton()
print(fichier)

fichier2 = Singleton()
