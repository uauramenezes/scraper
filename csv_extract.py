# A simple script to get first two rows of csv files and write into another file
# The files full path must be included as arguments when starting the script
# Ex: $python3 csv_extract.py /home/user/file_to_open.csv /home/user/file_to_extract.csv

##### BE CAREFUL, IF THE SECOND FILE ALREADY EXISTS IT'LL BE OVERWRITTEN #####
# Otherwise it'll be created automatically

import sys

arguments = sys.argv

f1 = open(sys.argv[1], "r")

list_f1 = []

for line in f1:
    entity = line.split(",")

    if len(list_f1) != 0 and f'{entity[0]}, {entity[1]}' == list_f1[len(list_f1) - 1]:
        continue
    else:
        list_f1.append(f'{entity[0]}, {entity[1]}')


import csv
entities = open(sys.argv[2], "w+")
csv.writer(entities, delimiter='\n').writerow(list_f1)
