#!/usr/bin/env python

import sys

current_edge = None
#current_count = 0
word = None
list_node=[]
current_key=None

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the input we got from mapper.py
	key,edge_A = line.split('\t')

	# convert count (currently a string) to int
	try:
		key=(key)
		edge_A = (edge_A)
		#edge_B= (edge_B)
	except ValueError:
		# count was not a number, so silently
		# ignore/discard this line
		continue
	print('%s\t%s'%(edge_A,key))
	
	# this IF-switch only works because Hadoop sorts map output
	# by key (here: word) before it is passed to the reducer
	if current_key == key:
#		current_count += count
		list_node.append(edge_A)
		#if edge_A ==key:
		#	list_node.append(edge_B)
		#else:
		#	list_node.append(edge_A)
	else:
		if current_key:# and current_count>200:
			# write result to STDOUT
			#speaker_index=current_word.index(',')
			print('%s\t%s' % (current_key, list_node))
		current_key = key
		list_node=[]
		list_node.append(edge_A)
		#if edge_A ==key:
	#		list_node.append(edge_B)
	#	else:
	#		list_node.append(edge_A)

# do not forget to output the last word if needed!
if current_key == key:# and current_count>200:
	print('%s\t%s' % (current_key, list_node))
