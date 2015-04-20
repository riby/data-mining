#!/usr/bin/env python

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	#split input based on tab
	points=line.split('\t')
	point_A=(points[0])
	point_B=(points[1])
	print('%s\t%s' % (point_A,point_B))
