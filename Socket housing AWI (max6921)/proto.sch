EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:lib_reveil
LIBS:Raspberry_PI_B
LIBS:reveil-cache
LIBS:RPi_Hat-cache
LIBS:proto-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L CONN_01X14 P5
U 1 1 58973375
P 5975 3250
F 0 "P5" H 5975 4000 50  0000 C CNN
F 1 "CONN_01X14" V 6075 3250 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x14_Pitch2.54mm" H 5975 3250 50  0001 C CNN
F 3 "" H 5975 3250 50  0000 C CNN
	1    5975 3250
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X14 P2
U 1 1 589733BE
P 2425 3275
F 0 "P2" H 2425 4025 50  0000 C CNN
F 1 "CONN_01X14" V 2525 3275 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x14_Pitch2.54mm" H 2425 3275 50  0001 C CNN
F 3 "" H 2425 3275 50  0000 C CNN
	1    2425 3275
	-1   0    0    1   
$EndComp
$Comp
L CONN_01X14 P1
U 1 1 58973433
P 2025 3275
F 0 "P1" H 2025 4025 50  0000 C CNN
F 1 "CONN_01X14" V 2125 3275 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x14_Pitch2.54mm" H 2025 3275 50  0001 C CNN
F 3 "" H 2025 3275 50  0000 C CNN
	1    2025 3275
	-1   0    0    1   
$EndComp
$Comp
L CONN_01X14 P4
U 1 1 58973328
P 5550 3250
F 0 "P4" H 5550 4000 50  0000 C CNN
F 1 "CONN_01X14" V 5650 3250 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x14_Pitch2.54mm" H 5550 3250 50  0001 C CNN
F 3 "" H 5550 3250 50  0000 C CNN
	1    5550 3250
	1    0    0    -1  
$EndComp
$Comp
L MAX6902 U1
U 1 1 589776E1
P 3625 4375
F 0 "U1" H 3825 6125 60  0000 C CNN
F 1 "MAX6902" H 3875 6225 60  0000 C CNN
F 2 "mod_reveil:MAX6921 - SOP28" H 4025 5925 60  0001 C CNN
F 3 "" H 4025 5925 60  0001 C CNN
	1    3625 4375
	1    0    0    -1  
$EndComp
Wire Wire Line
	4950 3500 5350 3500
Wire Wire Line
	4925 3600 5350 3600
Wire Wire Line
	4900 3700 5350 3700
Wire Wire Line
	4900 3800 5350 3800
Wire Wire Line
	4925 3900 5350 3900
Wire Wire Line
	4975 3400 5350 3400
Wire Wire Line
	5000 3300 5350 3300
Wire Wire Line
	5025 3200 5350 3200
Wire Wire Line
	5050 3100 5350 3100
Wire Wire Line
	5075 3000 5350 3000
Wire Wire Line
	5100 2900 5350 2900
Wire Wire Line
	5125 2800 5350 2800
Wire Wire Line
	5150 2700 5350 2700
Wire Wire Line
	5175 2600 5350 2600
Wire Wire Line
	2625 2625 2950 2625
Wire Wire Line
	2625 2725 3325 2725
Wire Wire Line
	2625 2825 3300 2825
Wire Wire Line
	2625 2925 3275 2925
Wire Wire Line
	2625 3025 3250 3025
Wire Wire Line
	2625 3125 3225 3125
Wire Wire Line
	2625 3225 3200 3225
Wire Wire Line
	2625 3325 3175 3325
Wire Wire Line
	2625 3425 3150 3425
Wire Wire Line
	2625 3525 3125 3525
Wire Wire Line
	2625 3625 3100 3625
Wire Wire Line
	2625 3725 3075 3725
Wire Wire Line
	2625 3825 3400 3825
Wire Wire Line
	2625 3925 3325 3925
Wire Wire Line
	2650 2625 2225 2625
Connection ~ 2650 2625
Wire Wire Line
	2650 2725 2225 2725
Connection ~ 2650 2725
Wire Wire Line
	2225 2825 2650 2825
Connection ~ 2650 2825
Wire Wire Line
	2650 2925 2225 2925
Connection ~ 2650 2925
Wire Wire Line
	2650 3025 2225 3025
Connection ~ 2650 3025
Wire Wire Line
	2650 3125 2225 3125
Connection ~ 2650 3125
Wire Wire Line
	2650 3225 2225 3225
Connection ~ 2650 3225
Wire Wire Line
	2650 3325 2225 3325
Connection ~ 2650 3325
Wire Wire Line
	2650 3425 2225 3425
Connection ~ 2650 3425
Wire Wire Line
	2650 3525 2225 3525
Connection ~ 2650 3525
Wire Wire Line
	2650 3625 2225 3625
Connection ~ 2650 3625
Wire Wire Line
	2650 3725 2225 3725
Connection ~ 2650 3725
Wire Wire Line
	2650 3825 2225 3825
Connection ~ 2650 3825
Wire Wire Line
	2650 3925 2225 3925
Connection ~ 2650 3925
Wire Wire Line
	5325 3900 5775 3900
Connection ~ 5325 3900
Wire Wire Line
	5325 3800 5775 3800
Connection ~ 5325 3800
Wire Wire Line
	5325 3700 5775 3700
Connection ~ 5325 3700
Wire Wire Line
	5325 3600 5775 3600
Connection ~ 5325 3600
Wire Wire Line
	5325 3500 5775 3500
Connection ~ 5325 3500
Wire Wire Line
	5325 3400 5775 3400
Connection ~ 5325 3400
Wire Wire Line
	5325 3300 5775 3300
Connection ~ 5325 3300
Wire Wire Line
	5325 3200 5775 3200
Connection ~ 5325 3200
Wire Wire Line
	5325 3100 5775 3100
Connection ~ 5325 3100
Wire Wire Line
	5325 3000 5775 3000
Connection ~ 5325 3000
Wire Wire Line
	5325 2900 5775 2900
Connection ~ 5325 2900
Wire Wire Line
	5775 2800 5325 2800
Connection ~ 5325 2800
Wire Wire Line
	5775 2700 5325 2700
Connection ~ 5325 2700
Wire Wire Line
	5325 2600 5775 2600
Connection ~ 5325 2600
Wire Wire Line
	3775 1975 3775 1900
Wire Wire Line
	3775 1900 5175 1900
Wire Wire Line
	5175 1900 5175 2600
Wire Wire Line
	3375 1875 5150 1875
Wire Wire Line
	5150 1875 5150 2700
Wire Wire Line
	4525 2375 5125 2375
Wire Wire Line
	5125 2375 5125 2800
Wire Wire Line
	4525 2475 5100 2475
Wire Wire Line
	5100 2475 5100 2900
Wire Wire Line
	4525 2575 5075 2575
Wire Wire Line
	5075 2575 5075 3000
Wire Wire Line
	4525 2675 5050 2675
Wire Wire Line
	5050 2675 5050 3100
Wire Wire Line
	4525 2775 5025 2775
Wire Wire Line
	5025 2775 5025 3200
Wire Wire Line
	4525 2875 5000 2875
Wire Wire Line
	5000 2875 5000 3300
Wire Wire Line
	4525 2975 4975 2975
Wire Wire Line
	4975 2975 4975 3400
Wire Wire Line
	4525 3075 4950 3075
Wire Wire Line
	4950 3075 4950 3500
Wire Wire Line
	4525 3175 4925 3175
Wire Wire Line
	4925 3175 4925 3600
Wire Wire Line
	4525 3275 4900 3275
Wire Wire Line
	4900 3275 4900 3700
Wire Wire Line
	3425 2825 3375 2825
Wire Wire Line
	3375 2825 3375 1875
Wire Wire Line
	3425 3275 3375 3275
Wire Wire Line
	3375 3275 3375 4675
Wire Wire Line
	3375 4675 4900 4675
Wire Wire Line
	4900 4675 4900 3800
Wire Wire Line
	3425 3075 3350 3075
Wire Wire Line
	3350 3075 3350 4700
Wire Wire Line
	3350 4700 4925 4700
Wire Wire Line
	4925 4700 4925 3900
Wire Wire Line
	4075 1975 4075 1925
Wire Wire Line
	4075 1925 2950 1925
Wire Wire Line
	2950 1925 2950 2625
Wire Wire Line
	3425 3675 3325 3675
Wire Wire Line
	3325 3675 3325 2725
Wire Wire Line
	4525 4275 4575 4275
Wire Wire Line
	4575 4275 4575 4725
Wire Wire Line
	4575 4725 3300 4725
Wire Wire Line
	3300 4725 3300 2825
Wire Wire Line
	4525 4175 4600 4175
Wire Wire Line
	4600 4175 4600 4750
Wire Wire Line
	4600 4750 3275 4750
Wire Wire Line
	3275 4750 3275 2925
Wire Wire Line
	3250 3025 3250 4775
Wire Wire Line
	3250 4775 4625 4775
Wire Wire Line
	4625 4775 4625 4075
Wire Wire Line
	4625 4075 4525 4075
Wire Wire Line
	3225 3125 3225 4800
Wire Wire Line
	3225 4800 4650 4800
Wire Wire Line
	4650 4800 4650 3975
Wire Wire Line
	4650 3975 4525 3975
Wire Wire Line
	3200 3225 3200 4825
Wire Wire Line
	3200 4825 4675 4825
Wire Wire Line
	4675 4825 4675 3875
Wire Wire Line
	4675 3875 4525 3875
Wire Wire Line
	3175 3325 3175 4850
Wire Wire Line
	3175 4850 4700 4850
Wire Wire Line
	4700 4850 4700 3775
Wire Wire Line
	4700 3775 4525 3775
Wire Wire Line
	3150 3425 3150 4875
Wire Wire Line
	3150 4875 4725 4875
Wire Wire Line
	4725 4875 4725 3675
Wire Wire Line
	4725 3675 4525 3675
Wire Wire Line
	3125 3525 3125 4900
Wire Wire Line
	3125 4900 4750 4900
Wire Wire Line
	4750 4900 4750 3575
Wire Wire Line
	4750 3575 4525 3575
Wire Wire Line
	3100 3625 3100 4925
Wire Wire Line
	3100 4925 4775 4925
Wire Wire Line
	4775 4925 4775 3475
Wire Wire Line
	4775 3475 4525 3475
Wire Wire Line
	3075 3725 3075 4950
Wire Wire Line
	3075 4950 4800 4950
Wire Wire Line
	4800 4950 4800 3375
Wire Wire Line
	4800 3375 4525 3375
Wire Wire Line
	3425 3475 3400 3475
Wire Wire Line
	3400 3475 3400 3825
Wire Wire Line
	3975 4650 3325 4650
Wire Wire Line
	3325 4650 3325 3925
Wire Wire Line
	3975 4575 3975 4650
$Comp
L PWR_FLAG #FLG01
U 1 1 58979DF5
P 3675 4600
F 0 "#FLG01" H 3675 4695 50  0001 C CNN
F 1 "PWR_FLAG" H 3675 4780 50  0000 C CNN
F 2 "" H 3675 4600 50  0000 C CNN
F 3 "" H 3675 4600 50  0000 C CNN
	1    3675 4600
	1    0    0    -1  
$EndComp
Wire Wire Line
	3675 4600 3675 4650
Connection ~ 3675 4650
$EndSCHEMATC
