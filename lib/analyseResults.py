#!/usr/bin/python
# -*- coding: utf-8 -*- 

#Author: Carlos Andres Delgado
#Creation date 19th December 2020
#Last edition date 19th December 2020
#Description: Save and generate graphics
import numpy as np
np.set_printoptions(threshold=np.inf)
import matplotlib.pyplot as plt
import time
import math
from matplotlib.font_manager import FontProperties
minq = -10
maxq = 10
IndexZero = 0
symbols = ['r-p','b-s','g-^','y-o','m->','c-<','g--','k-.','c--']
nan=float('nan')
percentNodes=np.arange(0,100,5)


	
def generateGraphics(data,fileOutput):

	timestr = time.strftime("%Y%m%d_%H%M%S")
	font = {'weight': 'normal', 'size': 8}
	fig3 = plt.figure()
	ax = fig3.add_subplot(111)
	deltaA = np.array([])
	deltaB = np.array([])
	deltaC = np.array([])
	
	DqRandom = data[0]
	DqDegree = data[1]
	DqCentrality = data[2]

	for i in range(0,DqRandom.shape[0]):
		if i < DqRandom.shape[0]:
			deltaA = np.append(deltaA, np.max(DqRandom[i][IndexZero:-1])-np.min(DqRandom[i][IndexZero:-1]))
		if i < DqDegree.shape[0]:
			deltaB = np.append(deltaB, np.max(DqDegree[i][IndexZero:-1])-np.min(DqDegree[i][IndexZero:-1]))
		if i < DqCentrality.shape[0]:
			deltaC = np.append(deltaC, np.max(DqCentrality[i][IndexZero:-1])-np.min(DqCentrality[i][IndexZero:-1]))
	plt.plot(percentNodes,deltaA,'r-' , label = r'$\Delta D_q$ random')
	plt.plot(percentNodes,deltaB,'g-' , label = r'$\Delta D_q$ degree')
	plt.plot(percentNodes,deltaC,'b-' , label = r'$\Delta D_q$ centrality')
	fontP = FontProperties()
	fontP.set_size('small')
	plt.xlabel('Lost nodes (%)', fontdict=font)
	plt.ylabel(r'Differential $\Delta D_q$', fontdict=font)
	plt.title(u'Multifractality and robustness', fontdict=font)
	plt.xticks(np.arange(min(percentNodes), max(percentNodes)+1, 10))
	lgd = plt.legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))
	plt.grid(True)
	plt.savefig('output/graphics/'+"Dq"+fileOutput+timestr+'.svg', bbox_extra_artists=(lgd,),bbox_inches='tight',format="svg")	
	
	

	font = {'weight': 'normal', 'size': 8}
	fig4 = plt.figure()
	ax = fig4.add_subplot(111)
	RRandom = np.nansum(DqRandom,axis=0)/(DqRandom.shape[0])
	RDegree = np.nansum(DqDegree,axis=0)/(DqDegree.shape[0])
	RCentrality = np.nansum(DqCentrality,axis=0)/(DqDegree.shape[0])
	plt.plot(range(0,maxq),RRandom[IndexZero:-1],'r-' , label = u'R random')
	plt.plot(range(0,maxq),RDegree[IndexZero:-1],'g-' , label = u'R degree')
	plt.plot(range(0,maxq),RCentrality[IndexZero:-1],'b-' , label = u'R centrality')
	fontP = FontProperties()
	fontP.set_size('small')
	plt.xlabel('q', fontdict=font)
	plt.ylabel(r'R-index', fontdict=font)
	plt.title(u'R-index multifractality and robustness', fontdict=font)
	lgd = plt.legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))
	plt.grid(True)
	plt.savefig('output/graphics/'+"R-index"+fileOutput+timestr+'.svg', bbox_extra_artists=(lgd,),bbox_inches='tight',format="svg")	
	
def saveFiles(data,fileOutput):
	
	RTqA = data[0]
	RTqB = data[1]
	RTqC = data[2]
	
	measureGCA = data[3]
	measureAPLA = data[4]
	
	measureGCB = data[4]
	measureAPLB = data[5]
	
	measureGCC = data[6]
	measureAPLC = data[7]
		
	timestr = time.strftime("%Y%m%d_%H%M%S")
	file_object = open("output/files/"+fileOutput+timestr, 'w') 
	
	r = np.arange(0.0, 0.95, 0.05)
	
	file_object.write("PercentOfNodes\n")
	file_object.write(np.array2string(r , precision=8, separator=','))
	
	file_object.write("\n\nRandomAttack\n")
	file_object.write("Tq\n")	
	file_object.write(np.array2string(RTqA, precision=8, separator=','))
	file_object.write("\nmeasureGC\n")	
	file_object.write(np.array2string(measureGCA, precision=8, separator=','))
	file_object.write("\nmeasureAPL\n")	
	file_object.write(np.array2string(measureAPLA, precision=8, separator=','))


	file_object.write("\n\nDegree\n")
	file_object.write("Tq\n")	
	file_object.write(np.array2string(RTqB, precision=8, separator=','))
	file_object.write("\nmeasureGC\n")	
	file_object.write(np.array2string(measureGCB, precision=8, separator=','))
	file_object.write("\nmeasureAPL\n")	
	file_object.write(np.array2string(measureAPLB, precision=8, separator=','))
	
	file_object.write("\n\nCentrality\n")
	file_object.write("Tq\n")	
	file_object.write(np.array2string(RTqC, precision=8, separator=','))
	file_object.write("\nmeasureGC\n")	
	file_object.write(np.array2string(measureGCC, precision=8, separator=','))
	file_object.write("\nmeasureAPL\n")	
	file_object.write(np.array2string(measureAPLC, precision=8, separator=','))

	file_object.close()
