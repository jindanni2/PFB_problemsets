#!/usr/bin/env python3
import sys
import random

seq = sys.argv[1]
N = len(seq)
new_seq = seq

for i in range(N):
	posA = random.randrange(0,N-1,1)
	posB = random.randrange(posA+1,N,1)
	new_seq = "".join([new_seq[:posA],new_seq[posB],new_seq[posA+1:posB],new_seq[posA],new_seq[posB+1:]])
#	print(posA, posB, new_seq)
print(new_seq)

