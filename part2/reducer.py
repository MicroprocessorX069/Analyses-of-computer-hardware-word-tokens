#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    #word, next_word=words.split(",")
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        current_count += count
    else:
        if current_word:
		if current_count>1000:
            # write result to STDOUT
		    #temp=current_word+","+next_word
	            print '"%s\t%s",' % (current_word, current_count)
        current_count = count
        current_word = word

