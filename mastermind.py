
import random

mastermind = [str(random.randint(0,5)), str(random.randint(0,5)), str(random.randint(0,5)), str(random.randint(0,5)), str(random.randint(0,5))]
mastermind_set = set(mastermind)

reponse = None
reponse_compteur = 0

while reponse != mastermind:

	reponse = str(input("Devinez la série de 5 chiffres compris entre 0 et 5 : "))
	reponse_set = set(reponse)

	if reponse == "mastermind":
		print(mastermind, type(mastermind))

	if len(reponse) != 5:
		print("\n Il faut donner un nombre à 5 chiffres, banane !\n")

	else:

		reponse = list(reponse)
		reponse_compteur += 1

		nb_place = 0
		nb_exist = len(reponse_set & mastermind_set)

		if reponse[0] == mastermind[0]:
			nb_place += 1
		if reponse[1] == mastermind[1]:
			nb_place += 1
		if reponse[2] == mastermind[2]:
			nb_place += 1
		if reponse[3] == mastermind[3]:
			nb_place += 1
		if reponse[4] == mastermind[4]:
			nb_place += 1	

		if nb_place == 0:
			print("\n", nb_exist, "chiffre(s) présent(s) dans la combinaison et", "\n", nb_place, "chiffre bien placé... Nul ! -_-\n")
		if nb_place == 1:
			print("\n", nb_exist, "chiffre(s) présent(s) dans la combinaison et", "\n", nb_place, "chiffre bien placé... C'est un bon début !\n")
		if nb_place == 2:
			print("\n", nb_exist, "chiffre(s) présent(s) dans la combinaison et", "\n", nb_place, "chiffres bien placés, c'est pas mal !\n")
		if nb_place == 3:
			print("\n", nb_exist, "chiffre(s) présent(s) dans la combinaison et", "\n", nb_place, "chiffres bien placés ! Pinaise !\n")
		if nb_place == 4:
			print("\n", nb_exist, "chiffre(s) présent(s) dans la combinaison et", "\n", nb_place, "chiffres bien placés !!! OMG, presque !!\n")
		
print("\n Wouhou, c'est gagné !! Bravo !!\n Vous avez trouvé la combinaison en", reponse_compteur, "tentatives.")
