#!/usr/bin/env python
"""mapper.py"""

import sys
top10words_cc=["function","pdf","short","doc","data","manual","ui","description","information","service"]

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for i in range(len(words)-1):
	if words[i] in top10words_cc:
	       	print '%s\t%s' % (words[i]+", "+words[i+1], 1)
        
