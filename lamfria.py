#!/usr/bin/python3
# -*- coding: utf-8 -*- 

#Author: Carlos Andres Delgado
#Creation date 19th December 2020
#Last edition date 19th December 2020
#Description: The main file
import sys
import getopt
import snap
import lib.utils as utils
import lib.SBAlgorithm as SBAlgorithm
import lib.robustness as Robustness
import lib.analyseResults as Results
import time
import numpy as np


def main(argv):
	fileInput = ""
	typeNet = ""
	fileOutput = ""
	typeMeasure = ""
	try:
		opts, args = getopt.getopt(argv,'f:t:o:m:a:h:n:d:y',['file=','type=','output=','attack=','help=','node=','desired=','measure='])
	except getopt.GetoptError as err:
		print(err)
		print("You must execute: python GreedyAlgorithm.py --file <file> --type <type> --output <file>")
		sys.exit(2)
	
	for opt, arg in opts:
		if opt in ('-f', '--file'):
			fileInput = arg
		elif opt in ('-t','--type'):
			typeNet = arg
		elif opt in ('-o','--output'):
			fileOutput = arg
		else:
			print("You must execute: python GreedyAlgorithm.py --file <file> --type <type> --output <file> --attack centrality|degree|random")
			sys.exit(0)
										
	Rnd = snap.TRnd(1,0)
	
	
	if typeNet == "Edge":
		graph = snap.LoadEdgeList(snap.PUNGraph, fileInput, 0, 1)
	elif typeNet == "ConnList":
		graph = snap.LoadConnList(snap.PUNGraph, fileInput)
	elif typeNet == "Pajek":
		graph = snap.LoadPajek(snap.PUNGraph, fileInput)
	else:
		print("Your must select filetype")
		sys.exit()
	

	minq = 0
	maxq = 10
	
	#SandBox
	percentOfSandBoxes = 0.4
	repetitionsSB = 20


	numNodes = graph.GetNodes()
	d = snap.GetBfsFullDiam(graph,100,False)
	
	TqRandom,measureGCA,measureAPLA=Robustness.robustness_analysis(graph,'Random',minq,maxq,percentOfSandBoxes,repetitionsSB,fileOutput)
	TqDegree,measureGCB,measureAPLB=Robustness.robustness_analysis(graph,'Degree',minq,maxq,percentOfSandBoxes,repetitionsSB,fileOutput)
	TqCentrality,measureGCC,measureAPLC=Robustness.robustness_analysis(graph,'Centrality',minq,maxq,percentOfSandBoxes,repetitionsSB,fileOutput)
	
	data = [TqRandom,TqDegree,TqCentrality,measureGCA,measureAPLA,measureGCB,measureAPLB,measureGCC,measureAPLC]
	
	Results.generateGraphics(data,fileOutput)
	Results.saveFiles(data,fileOutput)
					
if __name__ == "__main__":
   main(sys.argv[1:])

