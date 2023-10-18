#!/usr/bin/env python3

#Question 11
#data = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
#for seq in data:
#	print(data.index(seq),len(seq),seq,sep = "\t")

#Question 13
data = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
data_tuple = [(len(seq),seq) for seq in data]
print(data_tuple)

