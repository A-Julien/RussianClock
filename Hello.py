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
tmpclk = 0.0000001
tmp =    0.000001
tmpload = 0.0001


# --- Initialisation des pin ---
GPIO.setmode(GPIO.BOARD)
GPIO.setup(DIN, GPIO.OUT)
GPIO.setup(LOAD, GPIO.OUT ,initial=0)
GPIO.setup(BLK, GPIO.OUT, initial=0)
GPIO.setup(CLK, GPIO.OUT)



def displayH():
	#     |A,F,B,G,E,C,D,2,H,4,6,7,8,5,3,1,9|NC  |
	tab = [0,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
	#tab = [0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0]
	for x in range(20):
		if tab[x] == 1:
			GPIO.output(DIN, GPIO.HIGH) # mise au niveau haut de data in
		elif tab[x] == 0:
			GPIO.output(DIN, GPIO.LOW)
		GPIO.output(CLK, GPIO.LOW) 
		time.sleep(tmpclk)
		GPIO.output(CLK, GPIO.HIGH)
		time.sleep(tmpclk)
	GPIO.output(LOAD, GPIO.HIGH) # mise du load au niveau haut
	time.sleep(tmpload)
	GPIO.output(LOAD, GPIO.LOW) # le front descendant de load charge le buffer a l'affichage	

def displayO():
	
	#     |A,F,B,G,E,C,D,2,H,4,6,7,8,5,3,1,9|NC  |
	tab = [1,1,1,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0]
	#tab = [0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0]
	for x in range(20):
		if tab[x] == 1:
			GPIO.output(DIN, GPIO.HIGH) # mise au niveau haut de data in
		elif tab[x] == 0:
			GPIO.output(DIN, GPIO.LOW)
		GPIO.output(CLK, GPIO.LOW) 
		time.sleep(tmpclk)
		GPIO.output(CLK, GPIO.HIGH)
		time.sleep(tmpclk)
	GPIO.output(LOAD, GPIO.HIGH) # mise du load au niveau haut
	time.sleep(tmpload)
	GPIO.output(LOAD, GPIO.LOW) # le front descendant de load charge le buffer a l'affichage	

def displayL():
	
	#     |A,F,B,G,E,C,D,2,H,4,6,7,8,5,3,1,9|NC  |
	tab = [0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0]
	#tab = [0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0]
	for x in range(20):
		if tab[x] == 1:
			GPIO.output(DIN, GPIO.HIGH) # mise au niveau haut de data in
		elif tab[x] == 0:
			GPIO.output(DIN, GPIO.LOW)
		GPIO.output(CLK, GPIO.LOW) 
		time.sleep(tmpclk)
		GPIO.output(CLK, GPIO.HIGH)
		time.sleep(tmpclk)
	GPIO.output(LOAD, GPIO.HIGH) # mise du load au niveau haut
	time.sleep(tmpload)
	GPIO.output(LOAD, GPIO.LOW) # le front descendant de load charge le buffer a l'affichage

def displayE():
	
	#     |A,F,B,G,E,C,D,2,H,4,6,7,8,5,3,1,9|NC  |
	tab = [1,1,0,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0]
	#tab = [0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0]
	for x in range(20):
		if tab[x] == 1:
			GPIO.output(DIN, GPIO.HIGH) # mise au niveau haut de data in
		elif tab[x] == 0:
			GPIO.output(DIN, GPIO.LOW)
		GPIO.output(CLK, GPIO.LOW) 
		time.sleep(tmpclk)
		GPIO.output(CLK, GPIO.HIGH)
		time.sleep(tmpclk)
	GPIO.output(LOAD, GPIO.HIGH) # mise du load au niveau haut
	time.sleep(tmpload)
	GPIO.output(LOAD, GPIO.LOW) # le front descendant de load charge le buffer a l'affichage	
def displayL2():
	
	#     |A,F,B,G,E,C,D,2,H,4,6,7,8,5,3,1,9|NC  |
	tab = [0,1,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0]
	#tab = [0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0]
	for x in range(20):
		if tab[x] == 1:
			GPIO.output(DIN, GPIO.HIGH) # mise au niveau haut de data in
		elif tab[x] == 0:
			GPIO.output(DIN, GPIO.LOW)
		GPIO.output(CLK, GPIO.LOW) 
		time.sleep(tmpclk)
		GPIO.output(CLK, GPIO.HIGH)
		time.sleep(tmpclk)
	GPIO.output(LOAD, GPIO.HIGH) # mise du load au niveau haut
	time.sleep(tmpload)
	GPIO.output(LOAD, GPIO.LOW) # le front descendant de load charge le buffer a l'affichage	

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
		time.sleep(tmpclk)
		GPIO.output(CLK, GPIO.HIGH)
		time.sleep(tmpclk)
	#time.sleep(0.001)
	GPIO.output(LOAD, GPIO.LOW) # le front descendant de load charge le buffer a l'affichage




""" On ecrit ici une boucle qui tourne a l'infini pour mettre tous les digits a 1 ou a 0 """
""" Sortie de la boucle si on tape '0' """
while True:
	displayH()
 	time.sleep(tmp)
	displayE()
 	time.sleep(tmp)
 	displayL()
 	time.sleep(tmp)
 	displayL2()
 	time.sleep(tmp)
 	displayO()
 	time.sleep(tmp)
#	if raw_input() == "0" :
#		break






	
