from controleur.controleur import Controleur

if __name__ == "__main__":
    print("Système démarrer")
    
    try:
        print("Initialiser")
        application = Controleur()
        application.executer()
    except KeyboardInterrupt:
        print("Interruption par clavier")
        application.quitter()