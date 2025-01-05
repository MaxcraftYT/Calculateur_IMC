# Calculateur d'IMC en Python

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Licence](https://img.shields.io/badge/licence-MIT-green)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)

## Description

Ce programme calcule l'IMC de l'utilisateur en fonction de son poids et de sa taille. Il affiche le résultat avec une interprétation (sous-poids, poids normal, surpoids, obésité) et dis incis si vous êtes dans quel situation d'IMC 
---

## ✨ Fonctionnalités

- Saisie utilisateur : Demande le poids et la taille de l'utilisateur en kg et m.
- Calcul de l'IMC : L'IMC est calculé selon la formule suivante : 
​- Interprétation du résultat : Le programme donne une interprétation en fonction du résultat de l'IMC : **IMC = Poids (kg) / Taille² (m²)**
     - Sous poids : IMC < 18.5
     - Poids normal : 18.5 ≤ IMC < 24.9
     - Surpoids : 25 ≤ IMC < 29.9
     - Obésité : IMC ≥ 30
- Barre de progression : Lors du calcul, une barre de progression est affichée pour simuler le calcul de l'IMC de manière dynamique et visuellement engageante.
- Affichage coloré : Les résultats sont affichés avec des couleurs pour les rendre plus visuellement attractifs.

## 🚀 Installation

### Prérequis
- Python 3.x
- [termcolor](https://pypi.org/project/termcolor/) pour ajouter des couleurs aux messages affichés dans le terminal.

### Étapes
1. Installation de python : 

   ```bash
   pip install python

2. Installation de termcolor :
   ```bash
   pip install termcolor

## ✨ Améliorations possibles

- Créer une interface graphique pour le calculateur d'IMC.

## 🤝 Contribution

Si vous souhaitez contribuer à ce projet, veuillez suivre ces étapes :

1. Faites un fork de ce dépôt.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/ma-fonctionnalité`).
3. Commitez vos changements (`git commit -am 'Ajout de ma fonctionnalité'`).
4. Poussez vos modifications (`git push origin feature/ma-fonctionnalité`).
5. Ouvrez une pull request.


## 📄 Licence
Ce projet est sous licence MIT. Consultez le fichier [LICENSE] pour plus de détails.

Si vous utilisez, modifiez ou redistribuez ce code, vous devez inclure une copie de la licence et mentionner l'auteur original : Maxcraft_YT. Merci de respecter cette règle ! 😊
