#!/usr/bin/env python3
import sys

#Question 1: fasta nt composition

## fasta parser from p6 Q9, creating fasta dictionary
#fastaDic = {}
#with open("Python_08.fasta","r") as fastaFO:
#	header = ""
#	for line in fastaFO:
#			line = line.rstrip()
#			if line[0] == ">":  # Header line: remove >, create new entry to fastaDic
#				header = line.lstrip(">")
#				fastaDic[header] = ""
#			else:  # Sequence line: append line to value of last header's value
#				fastaDic[header] += line
##print(fastaDic)

## creating datastructure with nt composition from fasta dictionary
#NTcompo = {}
#for gene in fastaDic:
#	NTcompo[gene] = {}
#	NTcompo[gene]["A"] = fastaDic[gene].count("A")
#	NTcompo[gene]["T"] = fastaDic[gene].count("T")
#	NTcompo[gene]["C"] = fastaDic[gene].count("C")
#	NTcompo[gene]["G"] = fastaDic[gene].count("G")
#print(NTcompo)

#Question 2: breaking seq into codons
## Fasta parser with user input file name
fastaDic = {}
with open("testseq.fasta","r") as fastaFO:
	header = ""
	for line in fastaFO:
			line = line.rstrip()
			if line[0] == ">":  # Header line: remove >, create new entry to fastaDic
				header = line.lstrip(">")
				fastaDic[header] = ""
			else:  # Sequence line: append line to value of last header's value
				fastaDic[header] += line
print(fastaDic)

# Breaking sequence into codons
for gene in fastaDic:
	# frame 1
	pos = 0
	codons = [] 
	while pos < len(fastaDic[gene])-3:
		codons.append(fastaDic[gene][pos:pos+3])
		pos += 3
	codons.append(fastaDic[gene][pos:len(fastaDic[gene])])
	jointcodons = " ".join(codons)
	print(gene+"-frame-1-codons\n",jointcodons)
	# frame 2
	pos = 1 
	codons = []  
	while pos < len(fastaDic[gene])-3:
		codons.append(fastaDic[gene][pos:pos+3])
		pos += 3
	codons.append(fastaDic[gene][pos:len(fastaDic[gene])])
	jointcodons = " ".join(codons)
	print(gene+"-frame-2-codons\n",jointcodons)
	# frame 3
	pos = 2 
	codons = []  
	while pos < len(fastaDic[gene])-3:
		codons.append(fastaDic[gene][pos:pos+3])
		pos += 3
	codons.append(fastaDic[gene][pos:len(fastaDic[gene])])
	jointcodons = " ".join(codons)
	print(gene+"-frame-3-codons\n",jointcodons)
