#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, sqlite3, csv, itertools

file_loc = 'C:/Users/Nahla/Desktop/'
file_name = 'cats.csv' # str(sys.argv[1])
argfile =  file_loc + file_name

loc = 'C:/Users/Nahla/Anaconda3/envs/butler/'
sqlite_file = loc + 'butler.sqlite'    # name of the sqlite database file


tn = "cats" #table name


def adddata():
	
	# Connecting to the database file
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()	 

	with open( argfile ) as f: # `with` statement available in 2.5+
		# csv.DictReader uses first line in file for column headings by default
		getdata = csv.DictReader(f, delimiter=',') # comma is default delimiter
		to_db = [ (\
			i['Campaign'], \
			i['Ad Group'], \
			i['Labels'] \
			) for i in getdata]

	c.executemany("INSERT INTO " + tn + " ( " \
		"upload_date," \
		"campaign," \
		"ad_group," \
		"category" \
		") VALUES ((CURRENT_TIMESTAMP), ?, ?, ?);", to_db)
			
	# Committing changes and closing the connection to the database file
	conn.commit()
	conn.close()
	
	#os.remove(argfile)
	
def showall():
	# Connecting to the database file
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()

	for row in c.execute("SELECT * FROM " + tn + " ORDER BY category DESC;").fetchall():
		print (row)	

	# Committing changes and closing the connection to the database file
	conn.commit()
	conn.close()


	
adddata()
#showall()



