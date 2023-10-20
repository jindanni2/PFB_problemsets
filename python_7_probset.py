#!/usr/bin/env python3
import re

##Question 1 & 2
#with open("Python_07_nobody.txt","r") as fh_nobody, open("Boris.txt","w") as fh_boris:
#	str_nobody = ""
#	for line in fh_nobody:
#		str_nobody += line  # read file and store in str_nobody as a string
#
#	pos_list = []
#	for found in re.finditer("Nobody",str_nobody):
#		pos = found.start(0)
#		pos_list.append(pos)
#	print(pos_list)
#
#	str_boris = re.sub(r"Nobody","Boris",str_nobody)
#	fh_boris.write(str_boris)

##Question 3 & 4
#with open("Python_07.fasta","r") as fh:
#	str_fasta = ""
#	for line in fh:
#		str_fasta += line # read fasta file as one string
#	
#	for header in re.finditer(r">(\S+)\s(.*)",str_fasta):
#		seqName = header.group(1)
#		seqDescription = header.group(2)
#		print(f"id: {seqName} desc: {seqDescription}")

##Question 5: FASTA parser modified with re
#fastaDic = {}
#with open("Python_07.fasta","r") as seq_read:
#	header = ""
#	for line in seq_read:
#			line = line.rstrip()
#			if re.search(r"^>(\S+)\s?(.*)",line):  # Header line: remove >, create new entry to fastaDic
#				header = line.lstrip(">")
#				fastaDic[header] = ""
#			else:  # Sequence line: append line to value of last header's value
#				fastaDic[header] += line
#print(fastaDic)	

#Question 6,7,8: Apol with degenerate nucleotides
with open("Python_07_ApoI.fasta","r") as fh_Apol:
	header = ""
  # Fasta parser
	fastaDic = {}
	for line in fh_Apol: 
		line = line.rstrip()
		if re.search(r"^>(\S+)\s?(.*)",line):  # Header line: remove >, create new entry to fastaDic
			header = line.lstrip(">")
			fastaDic[header] = ""
		else:  # Sequence line: append line to value of last header's value
			fastaDic[header] += line		
	
	# Regular expression to find Apol site positions, return list of tuples(pos,seq)	
	Apol_sites = []
	for found in re.finditer(r"[AG]AATT[CT]",fastaDic[header]):
		Apol_sites.append((found.start(0),found.group(0)))
	print(Apol_sites)
	
	# display cut sites with ^
	new_seq = re.sub(r"([AG])AATT([CT])",r"\1^AATT\2",fastaDic[header])
	print(new_seq)

	# sort fragments by length
	frag_list = new_seq.split("^")
	frag_list_sorted = sorted(frag_list,key=len)
	print(frag_list_sorted)
