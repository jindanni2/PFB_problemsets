#!/usr/bin/env python3
import sys

#Question 1-5
fav_dict = {"book":"Jitterbug Perfume", "song":"Tome Petty - I won't back down", "tree": "Cedar"}
#print(fav_dict["book"])
#fav_thing = "book"
#print(fav_dict[fav_thing])
#fav_thing = "tree"
#print(fav_dict[fav_thing])
fav_dict["organism"] = "bacteria"
fav_thing = "organism"
#print(fav_dict[fav_thing])

#Question 6
#for thing in fav_dict:
#	print(thing, fav_dict[thing])

#Question 7
#fav_thing = sys.argv[1]
#print(fav_dict[fav_thing])

#Question 8
#for key in fav_dict:
#	print(f"{key}")
#fav_thing = input(f"Please pick one of the item above:")
#print(fav_dict[fav_thing])

#Question 9
fav_dict["organism"] = "yeast"

#Question 10
fav_thing = sys.argv[1]
fav_value = sys.argv[2]
fav_dict[fav_thing] = fav_value
print(fav_thing, fav_dict[fav_thing], sep = ":")

