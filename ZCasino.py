# -*-coding:utf-8 -*

from os import system
from math import ceil
from random import randrange

tirage = 0
numero_choisi = -1
argent = 1000
mise = -1
gain = 0

print("\nBienvenue à la roulette du casino ! Vous disposez de", argent, "dollars.")

while argent > 0:

    # Le tirage est effectué
    tirage = randrange(50)

    while numero_choisi < 0:

        # On demande son choix au joueur
        numero_choisi = input("\nChoisissez un numéro entre 0 et 49 : ")

        # On vérifie que le joueur a entré un nombre
        try:
            numero_choisi = int(numero_choisi)
        except ValueError:
            print("\nVous devez entrer un nombre !")
            numero_choisi = -1
            continue
        if numero_choisi < 0:
            print("\nVous avez entré un nombre négatif !")
            numero_choisi = -1
            continue
        elif numero_choisi > 49:
            print("\nVous avez entré un nombre supérieur à 49 !")
            numero_choisi = -1
            continue

        while mise < 0:
            # On demande combien d'argent il souhaite miser
            mise = int(input("\nCombien souhaitez-vous miser ? "))

            try:
                mise = int(mise)
            except ValueError:
                print("\nVous devez entrer un nombre !")
                mise = -1
                continue
            if mise < 0:
                print("\nVous avez entré un nombre négatif !")
                mise = -1
                continue
            if mise > argent:
                print("\nVous n'avez pas assez d'argent !")
                mise = -1
                continue
        
    argent -= mise

    print("\nLa roulette s'arrête sur le numéro", tirage, "!")

    if numero_choisi == tirage:
        gain = mise * 10
        argent += gain
        print("\nBravo ! Vous gagnez", gain, "dollars.")
    elif numero_choisi % 2 == tirage % 2:
        gain = ceil(mise * 2)
        argent += gain
        if tirage % 2 == 0:
            print("\nLe nombre est pair ! Vous gagnez", gain, "dollars.")
        else:
            print("\nLe numéro est impair ! Vous gagnez", gain, "dollars.")
    else:
        print("\nVous avez perdu !")

    print("\nIl vous reste", argent, "dollars.")
    numero_choisi = -1

system("pause")
