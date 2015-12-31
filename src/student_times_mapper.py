#!/usr/bin/python
"""

"""

import sys
import csv

def mapper():
    reader = csv.DictReader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        author_id = line['author_id']
        hour = line['added_at'][11:13]
        
        writer.writerow([author_id, hour, 1])
        
mapper()
