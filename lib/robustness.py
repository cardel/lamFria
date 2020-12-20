#!/usr/bin/python3
# -*- coding: utf-8 -*- 

#Author: Carlos Andres Delgado
#Creation date 14th March 2018
#Edition date 12th December 2018
#Description: This algorithm provide some methods for robustness in complex networks

import random
import numpy
import sys
import lib.utils as utils
import lib.SBAlgorithm as SBAlgorithm
import snap

#Get meseaure of Robustness according giant component
#Article Mitigation of malicious attacks on networks
#http://w.pnas.org/cgi/doi/10.1073/pnas.1009440108
# Article Robustness surfaces of complex networks
#https://www.nature.com/articles/srep06133

#13-09-2018: Add **options 
def robustness_analysis(graph,typeRemoval,minq,maxq,percentSandBox,repetitions,nameFile):

	
	
	#Copy graph
	g = utils.copyGraph(graph)	
	
	#NumNodes
	N = g.GetNodes()

	#Remove 10% of nodes	
	numberNodesToRemove = int(0.05*float(N))
	
	#Initial distance
	d = snap.GetBfsFullDiam(g,10,False)	
	
	#Average PathLenght

	meanAverageIni = utils.getAveragePathLength(g)		
	
	#Outputs
	robustnessGC = numpy.array([N],dtype=float)
	robustnessAPL = numpy.array([meanAverageIni],dtype=float)	
	d = snap.GetBfsFullDiam(graph,100,False)
	print("Remove :",0,"%"," nodes:",N)
	logR, Indexzero,Tq, Dq,lnMrq = SBAlgorithm.SBAlgorithm(g,minq,maxq,percentSandBox,repetitions,d)
	RTq = Dq
	
		
	
	for p in range(5,100,5):
		
		measureGC = 0.
		measureAPL = 0.
		
		#try:
		Ng = g.GetNodes()
		diameterG = snap.GetBfsFullDiam(g,10,False)	

		maxDegree = 0.
		index = 0
		listID = snap.TIntV(Ng)
		listDegree =  snap.TIntV(Ng)
		for ni in g.Nodes():
			listID[index] = ni.GetId()
			listDegree[index] = int(ni.GetOutDeg())
			
			if listDegree[index] > maxDegree:
				maxDegree=listDegree[index]
				
			index+=1
		


		
		#Calculate clossness centrality
		#20-06-2019 Add condition to calculate ClosenessCentrality only it is necessary.
		ClosenessCentrality = numpy.array([])
		nodesToRemove = numpy.array([])	
			
		if typeRemoval == 'Centrality':
			ClosenessCentrality = utils.getOrderedClosenessCentrality(g,Ng)	
		#Remove nodes
		measureGC,measureAPL=utils.removeNodes(g,typeRemoval, p, numberNodesToRemove, ClosenessCentrality,listID,nodesToRemove)
		
		print("Remove :",p,"%"," nodes:",g.GetNodes())		
		
		
		#15-09-2018: Save nodes
		if nameFile != "none":
			snap.SaveEdgeList(g, "output/networks/"+nameFile+"remove"+typeRemoval+"-"+str(p)+"percent.txt")
		
		logR, Indexzero,Tq, Dq,lnMrq = SBAlgorithm.SBAlgorithm(g,minq,maxq,percentSandBox,repetitions,d)
		RTq = numpy.vstack((RTq,Dq))


		robustnessGC = numpy.append(robustnessGC,measureGC)
		robustnessAPL = numpy.append(robustnessAPL,measureAPL)

	return RTq, robustnessGC/N, robustnessAPL/meanAverageIni
	
