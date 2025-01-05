import time
import sys
from termcolor import colored
from tqdm import tqdm  # Ajout de la barre de progression

# Fonction pour demander et valider la saisie de l'utilisateur
def demander_mesure():
    while True:
        try:
            kilogramme = float(input(colored("Entrez votre poids (en kg) :", "magenta")))
            taille = float(input(colored("Entrez votre taille (en mètres) :", "magenta")))
            return kilogramme, taille
        except ValueError:
            print(colored("❌ Veuillez entrer un nombre valide pour la mesure.", "red"))

# Fonction pour calculer l'IMC
def calculer_IMC(kilogramme, taille):
    return kilogramme / taille**2

# Fonction pour interpréter l'IMC
def interpreter_IMC(imc):
    if imc < 18.5:
        return "Sous poids"
    elif 18.5 <= imc < 24.9:
        return "Poids normal"
    elif 25 <= imc < 29.9:
        return "Surpoids"
    else:
        return "Obésité"

# Fonction pour afficher une barre de progression lors du calcul
def afficher_animation():
    print(colored("\n🔄 Calcul en cours, veuillez patienter...", "yellow"))
    for _ in tqdm(range(100), desc="Calcul", ncols=100, ascii=True):
        time.sleep(0.02)  # Simulation d'un calcul avec une barre de progression

# Fonction pour afficher le résultat
def afficher_resultat(kilogramme, taille, imc, categorie):
    print("\n\033[1;35m✨ Résultats :\033[0m")
    print()
    print(colored(f"Poids : {kilogramme:.2f} kg", "green"))
    print(colored(f"Taille : {taille:.2f} m", "green"))
    print(colored(f"Votre IMC est de : {imc:.2f}", "yellow"))
    print(colored(f"Catégorie : {categorie}", "yellow"))

# Lancer le programme
if __name__ == "__main__":
    kilogramme, taille = demander_mesure()  # Demande la saisie de l'utilisateur
    afficher_animation()  # Affiche l'animation de calcul
    imc = calculer_IMC(kilogramme, taille)  # Calcule l'IMC
    categorie = interpreter_IMC(imc)  # Interprète l'IMC
    afficher_resultat(kilogramme, taille, imc, categorie)  # Affiche le résultat
