#!/usr/bin/env python3

##Question 5 & 6
#with open("Python_06.txt","r") as fo_r, open("Python_06_uc.txt","w") as fo_w:
#	for line in fo_r:
#		line = line.rstrip()
#		#print(line)
#		fo_w.write(line+"\n")

##Question 7

#with open("Python_06.seq.txt","r") as seq_r:
#	for line in seq_r:
#		header,seq = line.split("\t")
#		seq = seq.rstrip()
#		##Reverse complement, modified from probset 3 Question 13
#		DNA13 = seq.upper() #original nt are in upper case, complemented nt are in lower. At the end, convert everything back to upper case.
#		DNA13_a = DNA13.replace("T","a")
#		DNA13_at = DNA13_a.replace("A","t")
#		DNA13_atc = DNA13_at.replace("G","c")
#		DNA13_atcg = DNA13_atc.replace("C","g")
#		DNA13_rc = DNA13_atcg.upper()[::-1]		
#		print(f">{header}\n{DNA13_rc}")	

#Question 8
#with open("Python_06.fastq","r") as fastq_fo:
#	line_count = 0
#	char_count = 0	
#	for line in fastq_fo:
#		line = line.rstrip()
#		line_count += 1
#		char_count += len(line)
#	avg_len = char_count / line_count
#	print(f"Number of lines: {line_count}\nNumber of characters: {char_count}\nAverage line length: {avg_len}")

#Question 9: FASTA parser
#fastaDic = {}
#with open("testseq.fasta","r") as seq_read:
#	header = ""
#	for line in seq_read:
#			line = line.rstrip()
#			if line[0] == ">":  # Header line: remove >, create new entry to fastaDic
#				header = line.lstrip(">")
#				fastaDic[header] = ""
#			else:  # Sequence line: append line to value of last header's value
#				fastaDic[header] += line
#print(fastaDic)

#Question 10

