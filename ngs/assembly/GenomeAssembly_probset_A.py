#!/usr/bin/env python3

#Fasta parser
fastaDic = {}
with open("ecoli_0.25.contigs.fasta","r") as fh:
	header = ""
	for line in fh:
		line = line.rstrip()
		if line[0] == ">":
			header = line.lstrip(">")
			fastaDic[header]=""
		else:
			fastaDic[header] += line
#print(fastaDic)

# Number of contigs
print(f"Number of contigs:{len(fastaDic)}")

#shortest and longest contigs
contig_list = [fastaDic[contig] for contig in fastaDic]
#print(len(contig_list))
contig_l_sorted = sorted(contig_list, key=len,reverse=True)
print(f"Shorted contig: {contig_l_sorted[-1]}\nLongest contig: {contig_l_sorted[0]}")

#total contig length
total_len = 0
for con in contig_list:
	total_len += len(con)
print(f"Total contig length: {total_len}")

#L50 and N50 size
contig_count = 0
length = 0
for con in contig_l_sorted:
	length += len(con)
	contig_count += 1
	if length >= total_len /2:
		N50 = len(con)
		L50 = contig_count
		break
print(f"N50: {N50}, L50: {L50}")		

