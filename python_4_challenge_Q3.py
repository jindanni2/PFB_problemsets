#!/usr/bin/env python3

import sys

EcoRI = "GAATTC"
DNA = sys.argv[1]
newDNA = DNA.replace(EcoRI, "G^AATTC")
#print(newDNA)
fragments = newDNA.split("^")
frag_No = 1
for block in fragments:
	start = DNA.find(block) + 1
	end = start + len(block) -1
	print(f"Fragment {frag_No}: startPos {start}, endPos {end}, length {len(block)}")
	frag_No += 1
