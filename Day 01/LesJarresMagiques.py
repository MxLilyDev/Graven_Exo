import random

print("Bienvenue dans le jeu !\nTu disposes de 5 jarres, dans certaines se trouvent des clés, et dans d'autres, des serpents")
print("Pour commencer, choisi le niveau de difficulté:")
print("- Niv 1 : 1 serpent pour 5 jarres\n- Niv 2 : 2 serpents pour 5 jarres\n- Niv 3 : 4 serpents pour 5 jarres")
lvl = input()
trousseau = 0
while trousseau != 3:
    possibilities = [1, 2, 3, 4, 5]
    print("Selectrionne un nombre entre 1 & 5:")
    if int(lvl) == 1:
        snipe1 = random.randint(1, 5)
    if int(lvl) == 2:
        snipe1 = random.choice(possibilities)
        possibilities.remove(snipe1)
        snipe2 = random.choice(possibilities)
    if int(lvl) == 3:
        nosnipe = random.randint(1, 5)
    nbj = input()
    if (int(lvl) == 1 and int(nbj) == snipe1) or (int(lvl) == 2 and (int(nbj) == snipe2 or int(nbj) == snipe1)) or (int(lvl) == 3 and int(nbj) != nosnipe) :
        if trousseau != 0:
            print("Perdu, tu viens de te faire mordre pas un serpent ! Dans le feu de l'action, tu laisses tomber une clé")
            trousseau = trousseau - 1
        else:
            print("Perdu, tu viens de te faire mordre pas un serpent !")
    else:
        print("Félicitation, tu as trouvé une clé !")
        trousseau = trousseau + 1
    print("Tu as actuellement " + str(trousseau) + " clé(s) sur ton trousseau")
print("Félicitation, tu as complété le trousseau")