#!/usr/bin/python
"""

"""

import sys
import csv

def mapper():
    reader = csv.DictReader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        node_type = line['node_type']
        if node_type == 'question':
          id = line['id']
        elif node_type == 'answer':
          id = line['abs_parent_id']

        body_size = len(line['body'])
        
        writer.writerow([id, node_type, body_size])
        
mapper()
