#!/usr/bin/python

import csv
dictc = ['name',' Robert']
match = 0
nomatch = 0

with open('test.csv', 'rb') as f1:
    file1 = csv.reader(f1,delimiter=':', quoting=csv.QUOTE_NONE)
    for row in file1:
        dict1 = row
        if dictc == dict1:
            match = match + 1
            writer = csv.writer(open('matches.csv', 'wb'))
            writer.writerows([row])
        else:
            nomatch=nomatch + 1

if match <> 0:
    print "%s matches found" %match
else:
    print "%s no matches found" %nomatch

