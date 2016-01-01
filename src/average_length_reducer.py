#!/usr/bin/python

import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    current_id = None
    question_size = 0
    num_answers = 0
    tot_answers_size = 0

    for line in reader:
      if len(line) != 3:
        continue

      id, node_type, body_size  = line[0], line[1], int(line[2])

      if current_id and id != current_id:
        dump_data(writer, current_id, question_size, tot_answers_size, num_answers)
        question_size = None
        num_answers = 0
        tot_answers_size = 0

      if node_type == 'question':
        question_size = body_size
      elif node_type == 'answer':
        num_answers+=1
        tot_answers_size+=body_size

      current_id = id

    if current_id != None:
        dump_data(writer, current_id, question_size, tot_answers_size, num_answers)

def dump_data(writer, id, question_size, tot_answers_size, num_answers):
    if num_answers > 0:
      avg_answer_size = 1.0 * tot_answers_size / num_answers
    else:
      avg_answer_size = 0

    writer.writerow([id, question_size, avg_answer_size])

reducer()
