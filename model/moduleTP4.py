from datetime import datetime


class Mesure():
    def __init__(self):
        self.dateHeureMesure = datetime.now(); 
        self.donneesMesure = []
        
    def __repr__(self):
        return f"Date: {self.dateHeureMesure} Donnees: {self.afficherMesure}"
    
    def afficherMesure(self):
        return "rien pour l'instant"
        