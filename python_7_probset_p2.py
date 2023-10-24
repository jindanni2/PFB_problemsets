#!usr/bin/env python3
import sys
import re

#Question 9: create enzyme dictionary
bionet_fo = open("bionet.txt","r")
line_no = 1
enzyme_dict = {}

for line in bionet_fo:
	line = line.rstrip()
	if line_no <= 10:
	#	print("skipped line")
		pass
	else:
	#	print(line)
		enz,site = re.split(r"\s\s+", line)
		enzyme_dict[enz] = site
	line_no += 1

#print(enzyme_dict)

bionet_fo.close()
#exit()
#Question 10
my_enzyme = sys.argv[1]
DNA_fo = open(sys.argv[2],"r")
seq = DNA_fo.read().rstrip()
degen_nt = {"W":"[AT]","S":"[CG]","M":"[AC]","K":"[GT]","R":"[AG]","Y":"[CT]","B":"[CGT]","D":"[AGT]","H":"[ACT]","V":"[ACG]","N":"[ATCG]"}

if my_enzyme in enzyme_dict:

	# retriving enzyme cutsite from library
	plain_site = enzyme_dict[my_enzyme].replace("^","")
	annotated_site = enzyme_dict[my_enzyme]
	pos = annotated_site.find("^")
	
	plain_re = plain_site
	annotated_re = annotated_site

	# determine RE pattern
	for NT in degen_nt:
		plain_re = plain_re.replace(NT,degen_nt[NT])
		annotated_re = annotated_re.replace(NT,degen_nt[NT])
		#print(f"enzyme RE pattern: {plain_re},{annotated_re}")

	if re.search(rf"{plain_re}",seq):
		# Look for cutsite
		seq_annotated = seq
		for found in re.finditer(rf"{plain_re}",seq):
			startsite = found.start(0)
			cutpos = startsite + pos
			# annotating cutsite with ^
			seq_annotated = seq_annotated[:cutpos]+"^"+seq_annotated[cutpos:]
			# fragment list, number, sorting
			frag_list = seq_annotated.split("^")
			frag_list_sorted = sorted(frag_list, key=len, reverse=True)
		print(f"Cutsite annotated sequence: {seq_annotated}\nFragment number: {len(frag_list)}")
		print(f"Fragment in natural order: {frag_list}\nFragment in sorted order:{frag_list_sorted}")
	else:
		print(f"{my_enzyme} cutsite not found.")
else:
	print("Enzyme not found:(")
