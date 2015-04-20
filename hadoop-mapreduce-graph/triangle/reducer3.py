#!/usr/bin/env python

import sys
sum=0
# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# parse the input we got from mapper.py
	key,val1 = line.split('\t')
	#As key is 1 for all values, just sum up
	val1=int(val1)
	sum+=val1

print sum
