#!usr/bin/python
# -*- coding: iso-8859-1 -*-

import struct


def cacher(nomFichier, nomResultat, message, decalageV, decalageH):
	fichier = open(nomFichier, 'rb')
	resultat = open(nomResultat, 'w')
	contenu = fichier.readlines()
	resultat.write(contenu[0])
	contenu.remove(contenu[0])
	i = 0
	for ligne in contenu:
		if(i > decalageV and i<len(message)+decalageV+1):
			ligne = ligne[0:decalageH] + message[i-decalageV-1] + ligne[decalageH+1:len(ligne)]
			#code = message[i-decalageV]
			#code += ligne
			#ligne = code
		i = i+1
		resultat.write(ligne)
	fichier.close()
	resultat.close()

def reveler(nomFichier, decalageV, decalageH, longueur):
	fichier = open(nomFichier, 'rb')
	contenu = fichier.readlines()
	i = 2
	resultat = ""
	while i<longueur:
		if(decalageH > len(contenu[decalageV+i])):
			indice = len(contenu[decalageV+i]) -1
			resultat += contenu[decalageV+i][indice]
		else:
			resultat += contenu[decalageV+i][decalageH]
		i = i+1
	return resultat

if __name__ == '__main__':
	cacher('Zeus.bmp', 'res.bmp', 'les chaussettes de l archiduchesse sont elles seches archi seches on continu la dessus est ce qu il y a un probleme bla bla bla et hop hello world mais voila que mettre maintenant dans ce code secret.', 15, 0)
	
	print reveler('res.bmp', 15, 0, 170)