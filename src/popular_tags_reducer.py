#!/usr/bin/python

import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    current_top10 = []

    current_tag = None
    tot_tag = 0

    for line in reader:
      if len(line) != 2:
        continue

      tag, count  = line[0], int(line[1])

      if current_tag and tag != current_tag:
        current_top10 = select_top10(current_top10, current_tag, tot_tag)
        tot_tag = 0

      tot_tag+=1

      current_tag = tag

    if current_tag != None:
        current_top10 = select_top10(current_top10, current_tag, tot_tag)

    writer.writerows(current_top10)

def select_top10(current_top10, current_tag, tot_tag):
    if len(current_top10) < 10 or tot_tag > current_top10[9][1]:
      current_top10.append([current_tag, tot_tag])
      current_top10 = sorted(current_top10, key=lambda item: item[1], reverse=True)[:10]

    return current_top10

reducer()
