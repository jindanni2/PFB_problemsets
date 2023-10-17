#!/usr/bin/env python3

import sys

var = float(sys.argv[1])

#if var:
#  print("Aye Captain")
#else:
#  print("Nope")

print(f"The value you entered is: {sys.argv[1]}")
if var > 0:
  print("positive")
  if var < 50:
    print("value is smaller than 50")
    if var % 2 == 0:
      print("it is an even number that is smaller than 50")
  elif var > 50:
    print("value is greater than 50")
    if var % 3 == 0:
      print("it is larger than 50 and divisible by 3")
  else:
    print("value is equal to 50")
elif var == 0:
  print("value is zero")
else:
  print("negative")

