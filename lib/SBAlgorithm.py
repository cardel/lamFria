#!/usr/bin/python
# -*- coding: utf-8 -*- 

#Author: Carlos Andres Delgado
#Creation date 14th March 2018
#Edition date 12th December 2018
#Description: This algorithm calculates the multifractal dimension with SB method
import math
import snap
import random
import lib.utils as utils
import numpy as np

#Initially, make sure all nodes in the entire network are not selected as a center of a sandbox
#Set the radius r of the sandbox which will be used to cover the nodes in the range r [1, d], where d is the diameter of the network
def SBAlgorithm(g,minq,maxq,percentSandBox,repetitions,diameter):
	"""Calculate fractal dimension with SandBox method

	Inputs are parameters to configure algorithm behaviour.

	:param g: Network.
	:type g: Snap PUN Graph.
	:param minq: Minimum value of q
	:type args: Integer
	:param minq: Maximum value of q
	:type maxq: Integer	
	:param percentSandBox: Number of combinations of center nodes. This value is a percent of the total nodes
	:type percentSandBox: Double
	:param repetitions: Number of repetitions of algorithm
	:type repetitions: Integer		
	:param CenterNodes: Calculated center. If this is null, then the centers are calculated
	:type CenterNodes: np 1D Array	
	:para diameter: Diameter of the full network
	:type diameter: Integer
	:returns:				
		logR: np array
			logarithm of r/d
		Indexzero: Integer
			position of q=0 in Tq and Dq
		Tq: np array
			mass exponents		
		Dq: np array
			fractal dimensions		
		lnMrq: np 2D array
			logarithm of number of nodes in boxes by radio
		"""	
	graph = g


	numNodes = graph.GetNodes()

	listID = snap.TIntV(numNodes)
	index = 0
		
	rangeQ = maxq-minq+1	
	
	#Mass Exponents
	Tq = np.zeros([repetitions,rangeQ])	
	#Generalized dimensions
	Dq = np.zeros([repetitions,rangeQ])
	
	#Calculate loge = logR/diameter
	logR = np.array([])
	for radius in range(1,diameter+1):
		logR = np.append(logR,math.log(float(radius)/diameter))
		
	#LnrqTotal
	lnMrqTotal = np.zeros([rangeQ,diameter],dtype=float)	
	#Index of Tq[0]
	Indexzero = 0


	#Rearrange the nodes of the entire network into ran- dom order. More specifically, in a random order, nodes which will be selected as the center of a sandbox box are randomly arrayed.

	for r in range(0,repetitions):
		
		#Total q
		lnMrq = np.zeros([rangeQ,diameter],dtype=float)
		sand = []
		numberOfBoxes = int(percentSandBox*numNodes);

		for i in range(0,numberOfBoxes):
			randomCenter =graph.GetRndNId()
			
			valuePerNodes = np.zeros([diameter])
			
			
			for radius in range(1, diameter+1):
				NodeVec = snap.TIntV()
				snap.GetNodesAtHop(graph, randomCenter, radius, NodeVec, False)
				valuePerNodes[radius-1]=int(len(NodeVec))
				
				if radius > 1:
					valuePerNodes[radius-1]+=valuePerNodes[radius-2]
				else:
					valuePerNodes[radius-1]+=1
		
			sand.append(valuePerNodes)
		
		sandBoxes = np.transpose(np.array(sand))
		#Index of q
		count = 0
		Indexzero  = 0 
		
		for q in range(minq,maxq+1,1):
			i = 0
			for sand in sandBoxes:				
				MrA = np.power(sand,q-1)
				Mr = np.log(np.average(MrA))
				lnMrq[count][i]=Mr
				lnMrqTotal[count][i]+=Mr
				i+=1				
			

			
			m,b = utils.linealRegresssion(logR,lnMrq[count])

			if math.isnan(m):
				print(logR, sand,lnMrq[count],m,b)				
				exit()
			#Adjust due to size of array (q is a Real number, and index of array is a integer number >=0)
			#Find the mass exponents
			if q == 0: 
				countDim = count;		

			Tq[r][count] = m
			
			#Find the Generalizated Fractal dimensions
			if q != 1:
				m,b = utils.linealRegresssion((q-1)*logR,lnMrq[count])
				if math.isnan(m):
					print(m,b)					
			else:
				Z1e = np.array([])
				for sand in sandBoxes:					
					Ze = np.log(sand)
					Ze = np.average(Ze)
					Z1e = np.append(Z1e,Ze)
				m,b = utils.linealRegresssion(logR,Z1e)	
			Dq[r][count] = m

			if q == 0:
				Indexzero = count
			
			count+=1
	
	lnMrqTotalA = lnMrqTotal/repetitions
	TqA = np.mean(Tq,axis=0)
	DqA = np.mean(Dq,axis=0)

	return logR, Indexzero,TqA, DqA,lnMrqTotalA
