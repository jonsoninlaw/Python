import random

# nombre_secret = random.randint(0, 100)
nombre_secret = random.randint(0, 5)
tentatives = []
reponse = ()

while reponse != nombre_secret:
	reponse = int(input("Essayez de deviner le nombre auquel je pense entre 0 et 100 :  "))
	tentatives.append(reponse)
	if reponse < nombre_secret:
		print("Plus grand !")
	elif reponse > nombre_secret:
		print("Plus petit !")

print("Bravo !")
nb_coups = len(tentatives)
print("Vous avez réussi en", nb_coups, "tentatives :")
for tent in tentatives:
	print(" - ", tent)