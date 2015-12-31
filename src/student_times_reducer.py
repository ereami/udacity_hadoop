#!/usr/bin/python

import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    current_author_id = None
    hour_counts = [0] * 24

    for line in reader:
      if len(line) != 3:
        continue

      author_id, hour, count  = line[0], int(line[1]), int(line[2])

      if current_author_id is None or author_id != current_author_id:
        if not current_author_id is None:
          dump_data(writer, current_author_id, hour_counts)
        hour_counts = [0] * 24
        current_author_id = author_id
      hour_counts[hour] += count

    dump_data(writer, current_author_id, hour_counts)


def dump_data(writer, author_id, hour_counts):
  max_hours=[i for i in range(24) if hour_counts[i] == max(hour_counts)]

  for max_hour in max_hours:
    writer.writerow([author_id, max_hour])

reducer()
