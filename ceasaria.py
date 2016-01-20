#! /usr/bin/env python
import urllib2
import csv
import posixfile

#Get remote file to local copy
FILE_LINK = 'https://docs.google.com/spreadsheets/d/1r_DUqKKEPSV__GKNqlBalXOkB-xk2SsuP5ID-ReCtUs/pub?gid=0&single=true&output=csv'
response = urllib2.urlopen(FILE_LINK)
local_CSV = open('./out.csv', 'w')
local_CSV.write(response.read())
local_CSV.close()

def reader():
	with open('./out.csv', 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter = ',', dialect=csv.excel)
			for row in reader:
					yield[row]

list = reader()

for rows in list:
	for row in rows:
		key = row[1]
		for x in range(2, len(row)):
			output=posixfile.open("./{}.csv".format(x), 'a')
			output.lock('w|')
			output.write("{{\"{}\":\"{}\"}}\n".format(key, row[x]))
			output.lock('u')
			output.close