#!/usr/bin/python

import sys
import csv
import pandas as pd


def Main():
  data = read_data_from_csv()
  qrylist = find_unique_queries(data)
  count_unique_queries(qrylist)

def read_data_from_csv():
  df = pd.read_csv(sys.stdin)
  return df

def find_unique_queries(df):
  querylist = list(df.Query)
  for qry in querylist:
    print("{0}\t{1}".format(qry, 1))
  return querylist
  
Main()

"""
def readdata_query():
        print(querylist)
   	from collections import Counter
	counts = Counter(querylist)
	print(counts)
	return counts
#def readcsvdata():
#	df = pd.read_csv(sys.stdin)
 
readdata_query()

"""
