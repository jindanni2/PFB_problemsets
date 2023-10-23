#!/usr/bin/env python3
import sys
from Bio import SeqIO
from Bio.SeqIO.QualityIO import FastqGeneralIterator

#Question 8: trimming poor quality bases from fastq

threshold = int(sys.argv[1])
s = "seq"
q = "qual"

# parse fastq to make dictionary
fastqDic ={}
count = 0 
total_len = 0
with open("SRR21901339.fastq") as in_handle:
	for title,seq,qual in FastqGeneralIterator(in_handle):
		count += 1
		total_len += len(seq)
		fastqDic[title] = {}
		fastqDic[title]["seq"] = seq
		fastqDic[title]["qual"] = qual
print("%i records with toal sequence length %i" % (count, total_len))
#print(fastqDic)

fh_trim = open("SRR21901339.trim.fastq","w")
for gene in fastqDic:
	fh_trim.write(f"@{gene}\n")
	rev_qstr = fastqDic[gene][q][::-1]
	for qchar in rev_qstr:
		if ord(qchar)-29 >= threshold:
			break
		else:
			fastqDic[gene][s]=fastqDic[gene][s][:-1]
			fastqDic[gene][q] = fastqDic[gene][q][:-1]
	#print(fastqDic[gene][s])
	fh_trim.write(f"{fastqDic[gene][s]}\n+\n{fastqDic[gene][q]}\n")

fh_trim.close()
