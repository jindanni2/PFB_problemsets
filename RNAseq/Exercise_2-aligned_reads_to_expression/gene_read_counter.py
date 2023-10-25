#!/usr/bin/env python3

sam_fh = open("bowtie2.sam","r")
readDict = {}
for line in sam_fh:
	line = line.rstrip()
	info_list = line.split("\t")
	read_name = info_list[0]
	transcript = info_list[2]
	gene = transcript.split("^")[0]

	if gene not in readDict:
		readDict[gene] = set()
	
	readDict[gene].add(read_name)
#print(readDict)

readcountDict = {}
for gene in readDict:
	readcountDict[gene] = len(readDict[gene])
#print(readcountDict)

#Sort genes based on read number mapped:
gene_list = list(readcountDict.keys())
gene_list_sorted = sorted(gene_list, key = lambda x:readcountDict[x], reverse=True)

for gene in gene_list_sorted:
	print(f"{gene:<10}", readcountDict[gene])
