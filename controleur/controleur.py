from model.model import Modele
from vue.vue import Vue

from time import sleep

class Controleur():
    def __init__(self):
        print("En attente de Vue et Model")
        self.model = Modele()
        self.vue = Vue()
    
    def executer(self):
        while True:
            print("Le programme est en route")
            sleep(1)
            
    
    def quitter(self):
        print("Quitter")