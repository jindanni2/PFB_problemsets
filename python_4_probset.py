#!/usr/bin/env python3

import sys

##Question 2
#taxa = "sapiens, erectus, neanderthalensis"
#print(taxa)
#print(taxa[1])
#print(type(taxa))
#species = taxa.split(", ")
#print(species)
#print(species[1])
#print(type(species))
#species_sorted = sorted(species)
#print(species_sorted)
#species_sorted_len = sorted(species, key=len)
#print(species_sorted_len)

##Question 4: print out 1-100
#i = 0
#while i in range(100):
#	i += 1
#	print(i)

##Question 5: factorial of 1000 (or any number in command line argument)
#i = 0
#fac = 1
#while i in range(int(sys.argv[1])):
#	i += 1
#	fac *= i
#print(fac)

#Question 6&7
#value_list = [101,2,15,22,95,33,2,27,72,15,52]
#sorted_list = sorted(value_list)
#sum_even = 0
#sum_odd = 0
#for i in sorted_list:
#	print(i)
#	if i % 2 == 0:
#		sum_even += i
#	else:
#		sum_odd += i
#print(f"Sum of even numbers: {sum_even}\nSum of odds: {sum_odd}")

#Question 8
#for i in range(100):
#	print(i+1)

#Question 9
#num_list = [num+1 for num in range(100)]
#print(num_list)

#Question 10
start = int(sys.argv[1])
end = int(sys.argv[2])
i = start
for i in range(start,end+1):
	if i %2 == 1:
		print(i)
	

