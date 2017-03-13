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

#---------------------------------------------
#Take BRUTE order and display it			
# Frame : |A,F,B,G,E,C,D,2,H,4,6,7,8,5,3,1,9,N,N,N|
#---------------------------------------------
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