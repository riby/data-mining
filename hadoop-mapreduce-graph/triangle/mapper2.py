#!/usr/bin/env python
import sys
import re
dict_node=dict()
count=0
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	#spliting the line based on tab
	points=line.split('\t')
	#input key from mapper
	key=(points[0])
	#find list of items from the mapper 1
	if "[" in points[1]:
		# Use regex to get numbers from the string output of the mapper
		list_edge=re.findall("\d+",points[1])
		dict_node[key]=list_edge
	else:
		#Print other points not in list to output
		print("%s\t%s"%(key+"_"+points[1],"*"))
#Make the 2 loop possible edges

for d in dict_node:
	for v in dict_node[d]:
		if v in dict_node:
			for vin in dict_node[v]:
				# Remove the duplication of results from the combinations
				if d<vin and v<vin:
					print("%s\t%s" %(d+"_"+vin,v))

