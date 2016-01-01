#!/usr/bin/python

import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    current_id = None
    students = []

    for line in reader:
      if len(line) != 2:
        continue

      id, author_id  = line[0], line[1]

      if current_id and id != current_id:
        dump_data(writer, current_id, students)
        students = []

      students.append(author_id)
      current_id = id

    if current_id != None:
        dump_data(writer, current_id, students)

def dump_data(writer, id, students):

    writer.writerow([id, students])

reducer()
