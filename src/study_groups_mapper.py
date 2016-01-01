#!/usr/bin/python
"""

"""

import sys
import csv

def mapper():
    reader = csv.DictReader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if line['node_type'] == 'question':
          id = line['id']
        else:
          id = line['abs_parent_id']
        
        writer.writerow([id, line['author_id']])
        
mapper()
