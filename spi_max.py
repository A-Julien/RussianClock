#!/bin/python2.7


# --- Bibliotheques ---
import RPi.GPIO as GPIO
import time



# --- Variables ---
""" Brochage du PI3 a modifier """
TEMPO = 100 # temporisation de l'execution des changements d'etats (si besoin)
DIN   = 11	# data input du max (pin a definir)
LOAD  = 13  # loading (chargement du buffer sur le front descendant)
CLK   = 15  # ajoute DIN au buffer sur le front montant
BLK   = 29  # blank (niveau haut force sorties a bas, eteint l'affichage et eteint le max)


# --- Initialisation des pin ---
GPIO.setmode(GPIO.BOARD)
GPIO.setup(DIN, GPIO.OUT)
GPIO.setup(LOAD, GPIO.OUT ,initial=0)
GPIO.setup(BLK, GPIO.OUT, initial=0)
GPIO.setup(CLK, GPIO.OUT)



# --- Fonctions d'affichage ---
def displayAll(state): 
	""" Met tous les digits a l'etat state """
	GPIO.output(LOAD, GPIO.HIGH) # mise du load au niveau haut
	if state == 1:
		GPIO.output(DIN, GPIO.HIGH) # mise au niveau haut de data in
	else :
		GPIO.output(DIN, GPIO.LOW) 

	for x in range(20): # on remplit le buffer de '1' logiques
		GPIO.output(CLK, GPIO.LOW) 
		time.sleep(0.001)
		GPIO.output(CLK, GPIO.HIGH)
		time.sleep(0.001)
	#time.sleep(0.001)
	GPIO.output(LOAD, GPIO.LOW) # le front descendant de load charge le buffer a l'affichage




""" On ecrit ici une boucle qui tourne a l'infini pour mettre tous les digits a 1 ou a 0 """
""" Sortie de la boucle si on tape '0' """
while True:
	displayAll(1)
	time.sleep(0.5) # teporisation 1 seconde
	displayAll(0)
	time.sleep(0.5) # teporisation 1 seconde
#	if raw_input() == "0" :
#		break






	
