#!/usr/bin/python

import operator
import sys
import pandas as pd

def Main():
  data = read_mapper_output()
  uqueries = find_unique_queries(data)
  max_query(uqueries)
  min_query(uqueries)
def read_mapper_output():
  data = []
  for line in sys.stdin:
    data.append(line)
  return data

def find_unique_queries(data):
  uqueries = {}
  for row in data:
    key, val = row.split("\t")
    val = int(val)
    if not uqueries.has_key(key):
      uqueries[key] = 0
    uqueries[key] += val 
  for key, val in uqueries.iteritems():
    print("{0}\t{1}".format(key, val))
  return uqueries

def max_query(uqueries):
  print max(uqueries.iteritems(), key = operator.itemgetter(1))[0]

def min_query(uqueries):
  print min(uqueries.iteritems(), key = operator.itemgetter(1))[0]


Main()


"""
qdata = readdata_query()
def function1():
        for i in counts:
		list.append(qdata[i])
	maxval = max(qdata)
	for query,qdata in qdata.iteritems():
		if qdata == maxval:
			return query
def function2():
	for i in qdata:
                list.append(qdata[i])
        minval = min(qdata)
        for query,qdata in qdata.iteritems():
                if qdata == minval:
                        return query
def function3():
        totalnum = len(qdata)
        return totalnum
def function4():
	
	
"""
	
    
