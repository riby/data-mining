#!/usr/bin/env python

import sys

current_edge = None
list_node=[]
current_key=None
dict_node=dict()
current_count=0

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the input we got from mapper.py
	key,value_node = line.split('\t')
	#Count the number of triangles formed
	if current_key==key:
		current_count+=1
	else:
		if current_key:
			print('%s\t%s' % ("1", current_count))
		if value_node=="*":
			current_key=key
			current_count=0
		else:
			current_count=0
if current_key == key:# and current_count>1:
	print('%s\t%s' % ("1", current_count))
