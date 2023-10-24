#!/usr/bin/env python3
import subprocess
from Bio.SeqIO.FastaIO import SimpleFastaParser
from Bio import SeqIO

#Question 1
Q1 = f"grep '>' D_melanogaster_genomic.fna | wc -l"
Q1_run = subprocess.run(Q1, shell=True)

#Question 2: nucleotide content

#Fasta parser
fastaDic={}
with open("D_melanogaster_genomic.fna","r") as fh:
	for title,seq in SimpleFastaParser(fh):
		fastaDic[title] = seq

#print(len(fastaDic))

#Counting nucleotides
seq_list = [fastaDic[header] for header in fastaDic]
full_seq = "".join(seq_list)
Acount = full_seq.count("A") + full_seq.count("a")
Tcount = full_seq.count("T") + full_seq.count("t")
Ccount = full_seq.count("C") + full_seq.count("c")
Gcount = full_seq.count("G") + full_seq.count("g")
print(f"A count: {Acount} T count: {Tcount} C count: {Ccount} G count: {Gcount}")

#Question 3: gaps
Ncount = full_seq.count("N")
fGaps = Ncount/len(full_seq)
print(f"{fGaps:.2%} of the genome is comprised of gaps.")
