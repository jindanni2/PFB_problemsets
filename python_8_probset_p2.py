#!/usr/bin/env python3
import sys
import re

#Question 2,3,4,5,6,7: breaking seq into codons, translation
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

translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}

fh_w = open("Python_08.codons-6frames.nt","w")
fh_tln = open("Python_08.translated.aa","w")
fh_longest = open("Python_08.translated-longest.aa","w")
fh_orf = open("Python_08.orf-longest.nt","w")

# Breaking sequence into codons
for gene in fastaDic:

	ORF_aa_6f = [] # list of longest ORF aa in each of the 6 frames
	Orf_nt_6f = [] # list of longest Orf nt in each of the 6 frames

	# frame 1-3 (og seq)
	DNA_og = fastaDic[gene].upper()
	for j in range(0,3):
		pos = j
		codons = []
		while pos <= len(DNA_og)-3:
			codons.append(DNA_og[pos:pos+3])
			pos += 3
		#codons.append(DNA_og[pos:len(DNA_og)])
		jointcodons = " ".join(codons)
		fastaSeq = "".join(codons)
		fh_w.write(f">{gene}-frame-{j+1}-codons\n{fastaSeq}\n")
		#translation
		peptide = [translation_table[cod] for cod in codons]
		jointpep = "".join(peptide)
		fh_tln.write(f"{gene}-frame-{j+1}-peptide\n{jointpep}\n")
		
		#Looking for ORFs in a single translated frame
		ORF_aa_all = re.findall(r"M[A-Z]+\*",jointpep)
		ORF_aa_sorted = sorted(ORF_aa_all, key=len,reverse=True)
		ORF_aa_longest = ORF_aa_sorted[0]
		ORF_aa_6f.append(ORF_aa_longest)
		
		#Looking for longest Orf in nt sequences[DOES NOT WORK]
		Orf_nt_all = re.findall(r"ATG ([ATCG]{3} )+ T(AA|GA|AG)", jointcodons)
		Orf_nt_sorted = sorted(Orf_nt_all, key=len, reverse=True)
		Orf_nt_longest = Orf_nt_sorted[0]
		Orf_nt_6f.append(Orf_nt_longest)
	
	# Reverse complement
	DNA = fastaDic[gene].upper()
	DNA_a = DNA.replace("T","a")
	DNA_at = DNA_a.replace("A","t")
	DNA_atc = DNA_at.replace("G","c")
	DNA_atcg = DNA_atc.replace("C","g")
	DNA_rc = DNA_atcg.upper()[::-1]
	#print(DNA_rc)

	# frame 4-6 (rc)
	for i in range(0,3):
		pos = i
		codons = []
		while pos <= len(DNA_rc)-3:
			codons.append(DNA_rc[pos:pos+3])
			pos += 3
		#codons.append(DNA_rc[pos:len(DNA_rc)])
		jointcodons = " ".join(codons)
		fastaSeq = "".join(codons)
		fh_w.write(f">{gene}-frame-{i+4}-codons\n{fastaSeq}\n")
		#translation
		peptide = [translation_table[cod] for cod in codons]
		jointpep = "".join(peptide)
		fh_tln.write(f"{gene}-frame-{i+4}-peptide\n{jointpep}\n")
	
		#Looking for ORFs in a single translated frame
		ORF_aa_all = re.findall(r"M[A-Z]+\*",jointpep)
		ORF_aa_sorted = sorted(ORF_aa_all, key=len,reverse=True)
		ORF_aa_longest = ORF_aa_sorted[0]
		ORF_aa_6f.append(ORF_aa_longest)

    #Looking for longest Orf in nt sequences[DOES NOT WORK]
		Orf_nt_all = re.findall(r"ATG ([ATCG]{3} )+ T(AA|GA|AG)", jointcodons)
		Orf_nt_sorted = sorted(Orf_nt_all, key=len, reverse=True)
		Orf_nt_longest = Orf_nt_sorted[0]
		Orf_nt_6f.append(Orf_nt_longest)

	#print("list of longest ORF aa in 6 frames:",ORF_aa_6f)
	ORF_aa_6f_sorted = sorted(ORF_aa_6f,key=len,reverse=True)
	THE_longest_ORF_aa = ORF_aa_6f_sorted[0].rstrip("*")
	Orf_nt_6f_sorted = sorted(Orf_nt_6f,key=len,reverse=True)
	THe_longest_Orf_nt = Orf_nt_6f_sorted[0]
	fh_longest.write(f">{gene} longest_translate_peptide\n{THE_longest_ORF_aa}\n")
	fh_orf.write(f"{gene} longest_Orf_nt\n{THE_longest_Orf_nt}\n")

fh_w.close()
fh_tln.close()
fh_longest.close()
fh_orf.close()
