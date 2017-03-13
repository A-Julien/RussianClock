#!/usr/bin/python
#title			:maxlib.py
#description	:Communication library for MAX6921
#author			:Alaimo-J,Gigot-N,Castanier-R
#date			:20170313
#version		:0
#usage			:python maxlib.py
#notes			:
#python_version	:2.6.6
#==============================================================================
import RPi.GPIO as GPIO
import time
#     |1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H|NNN|

#-----------------------------------------------
#Take BRUTE order and display it			
# In  :|A,F,B,G,E,C,D,2,H,4,6,7,8,5,3,1,9,N,N,N|
# Out : Max6921
#-----------------------------------------------
def display(tab[],tmpclk,tmpload)
	for x in range(20):
		#Data
		if tab[x] == 0:
			GPIO.output(DIN, GPIO.LOW)
		else
			GPIO.output(DIN, GPIO.HIGH)
		#Clock
		GPIO.output(CLK, GPIO.LOW)
		time.sleep(tmpclk)
		GPIO.output(CLK, GPIO.HIGH)
		time.sleep(tmpclk)
	#Load
	GPIO.output(LOAD, GPIO.HIGH) # Rising edge of load
	time.sleep(tmpload)          # Time in the high state
	GPIO.output(LOAD, GPIO.LOW)  # Falling edge of LOAD to load all the buffer 
#---------------------------------------------

#-----------------------------------------------
# Take Logical Frame and convert in BRUTE frame
# In  : Digit=Segment,
# In  : |1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H|
# Out : |A,F,B,G,E,C,D,2,H,4,6,7,8,5,3,1,9,N,N,N|
#-----------------------------------------------
def assoc(*args):
	for arg in args:
		


	for x in xrange(0,16):
		tab[x]
	return _tab[]

#-------------------------------------------------
# Take ASCII code, return code of it in logical frame
# In  : Segment,Segment,..
# In  : A,1,D,...
# Out : |0,0,0,0,0,0,0,0,0,A,B,C,D,E,F,G,H|
#-------------------------------------------------
def segment($args):
	for arg in args:










	