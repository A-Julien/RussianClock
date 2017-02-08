#!/bin/python2.7


# --- Bibliothèques ---
import RPi.GPIO
import time



# --- Variables ---
""" Brochage du PI3 à modifier """
TEMPO = 100 # temporisation de l'execution des changements d'états (si besoin)
DIN = 12 # data input du max (pin à définir)
LOAD = 13 # loading (chargement du buffer sur le front descendant)
CLK = 14 # ajoute DIN au buffer sur le front montant
BLK = 15 # blank (niveau haut force sorties à bas, éteint l'affichage et éteint le max)


# --- Initialisation des pin ---
GPIO.setmode(GPIO.BOARD)
GPIO.setup(DIN)
GPIO.setup(LOAD, initial=0)
GPIO.setup(BLK, initial=1)
GPIO.setup(CLK)



# --- Fonctions d'affichage ---
def displayAll(state): 
	""" Met tous les digits à l'état state """
	GPIO.write(LOAD, 1) # mise du load au niveau haut
	GPIO.write(DIN, state) # mise au niveau haut de data in
	for x in range(19): # on remplit le buffer de '1' logiques
		GPIO.write(CLK, 0) 
		GPIO.write(CKL, 1)
	GPIO.write(LOAD, 0) # le front descendant de load charge le buffer à l'affichage




""" On écrit ici une boucle qui tourne à l'infini pour mettre tous les digits à 1 ou à 0 """
""" Sortie de la boucle si on tape '0' """
while True:
	displayAll(1)
	time.sleep(1) # teporisation 1 seconde
	displayAll(0)
	if raw_input() == "0" :
		break






	
