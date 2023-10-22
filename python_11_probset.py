#!/usr/bin/env python3

#Question 1: creating a DNA sequence class
class DNArecord(object):
	def __init__(self, sequence, name, organism):
		self.sequence = sequence
		self.gene_name = name
		self.organism = organism
		self.length = len(self.sequence)	

	def nt_composition(self):
		A_compo = self.sequence.count("A")/self.length
		T_compo = self.sequence.count("T")/self.length
		C_compo = self.sequence.count("C")/self.length
		G_compo = self.sequence.count("G")/self.length
		print(f"A: {A_compo:.2%}, T: {T_compo:.2%}, C: {C_compo:.2%}, G: {G_compo:.2%}")

	def GC_content(self):
		GC = (self.sequence.count("G") + self.sequence.count("C"))/self.length
		return GC

	def FASTAformatter(self):
		FASTAstr = ">" + self.gene_name + "\n" + self.sequence
		return FASTAstr	

	def compare(self,record2):
		Flag = self.sequence == record2.sequence and self.gene_name == record2.gene_name and self.organism == record2.organism
		return Flag

sampleseq1 = DNArecord("AAAATTTT","seq1","unicorn")
sampleseq2 = DNArecord("GGGGCCCC","seq2","imaginery_species")
sampleseq3 = DNArecord("AAAATTTT","seq1","unicorn")

print(f"sampleseq1:\nSequence: {sampleseq1.sequence}\nName: {sampleseq1.gene_name}\nOrganism:{sampleseq1.organism}\nLength: {sampleseq1.length}")
sampleseq1.nt_composition()
print(f"GC content: {sampleseq1.GC_content():2%}")
print(sampleseq1.FASTAformatter())
FLAG = sampleseq1.compare(sampleseq2)
FLAG2 = sampleseq1.compare(sampleseq3)
print(f"samples 1&2 are the same: {FLAG}")
print(f"samples 1&3 are the same: {FLAG2}")
