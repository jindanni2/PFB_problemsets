#!/usr/bin/env python3

import sys

##Question 6

#DNA6 = sys.argv[1].upper() # turn input sequence into upper case and store in variable DNA
#countA = DNA6.count("A")
#countT = DNA6.count("T")
#countG = DNA6.count("G")
#countC = DNA6.count("C")
#print(f"This sequence contains {countA} A's, {countT} T's, {countG} G's and {countC} C's.")

##Question 7&8

#DNA7 = sys.argv[1].upper()
#RNA = DNA7.replace("T","U")
#print(RNA)

##Question 9

#DNA9 = sys.argv[1].upper()
#total_nt = len(DNA9)
#countA = DNA9.count("A")
#countT = DNA9.count("T")
#AT_percent = 100 * (countA + countT)/total_nt
#print(f"AT content of this sequence is: {AT_percent:.2f}%.")
## AT content of the provided sequence is 42.04%

#Question 10&11&12
#DNA10 = sys.argv[1].upper()
#sub_DNA = DNA10[99:199]
#countG = sub_DNA.count("G")
#print(f"Substring: {sub_DNA}\nNumber of G's: {countG}")
#The substring of the given sequence contains 34 G's.

##Question 13
#DNA13 = sys.argv[1].upper() #original nt are in upper case, complemented nt are in lower. At the end, convert everything back to upper case.
#DNA13_a = DNA13.replace("T","a")
#DNA13_at = DNA13_a.replace("A","t")
#DNA13_atc = DNA13_at.replace("G","c")
#DNA13_atcg = DNA13_atc.replace("C","g")
#DNA13_rc = DNA13_atcg.upper()[::-1]
#print(DNA13_rc)

#Question 14
EcoRI = "GAATTC"
EcoRI_rc = "CTTAAG"
DNA14 = sys.argv[1].upper()
if EcoRI in DNA14:
	start = DNA14.find(EcoRI) +1
	end = start +5
	print (f"EcoRI startPos: {start} endPos: {end}")
elif EcoRI_rc in DNA14:
	start = DNA14.find(EcoRI_rc) +1
	end = start +5
	print (f"EcoRI startPos: {start} endPos: {end}")
else:
	print("EcoRI cutsite not found.")


