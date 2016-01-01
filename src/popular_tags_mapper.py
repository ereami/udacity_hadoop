#!/usr/bin/python
"""

"""

import sys
import csv

def mapper():
    reader = csv.DictReader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if line['node_type'] != 'question':
          continue

        tags=line['tagnames'].split()
        for tag in tags: 
          writer.writerow([tag, 1])
        
mapper()
