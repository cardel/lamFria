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
import loadFile as loader
import sys


def generateArrays(archivoA, archivoB, archivoC,archivoD):
	dataA = loader.getData(archivoA)
	dataB = loader.getData(archivoB)
	dataC = loader.getData(archivoC)
	dataD = loader.getData(archivoD)
	
	return [dataA, dataB,dataC, dataD]
	
	
def generateGraphics(data,fileOutput):

	timestr = time.strftime("%Y%m%d_%H%M%S")
	font = {'weight': 'normal', 'size': 8}

	fig3, axs = plt.subplots(2, 2)

	for i in range(0,2):
		for j in range(0,2):			
			dataIn = data[2*i+j]

			deltaA = np.array([])
			deltaB = np.array([])
			deltaC = np.array([])

			DqRandom = dataIn[0]
			DqDegree = dataIn[1]
			DqCentrality = dataIn[2]
			
			print(type(DqRandom))
			for k in range(0,DqRandom.shape[0]):
				if k < DqRandom.shape[0]:
					deltaA = np.append(deltaA, np.max(DqRandom[k][IndexZero:-1])-np.min(DqRandom[i][IndexZero:-1]))
				if k < DqDegree.shape[0]:
					deltaB = np.append(deltaB, np.max(DqDegree[k][IndexZero:-1])-np.min(DqDegree[i][IndexZero:-1]))
				if k < DqCentrality.shape[0]:
					deltaC = np.append(deltaC, np.max(DqCentrality[k][IndexZero:-1])-np.min(DqCentrality[i][IndexZero:-1]))
			axs[i,j].plot(percentNodes,deltaA,'r-' , label = r'$\Delta D_q$ random')
			axs[i,j].plot(percentNodes,deltaB,'g-' , label = r'$\Delta D_q$ degree')
			axs[i,j].plot(percentNodes,deltaC,'b-' , label = r'$\Delta D_q$ centrality')
			fontP = FontProperties()
			fontP.set_size('small')
			#axs[i,j].xlabel('Lost nodes (%)', fontdict=font)
			#axs[i,j].ylabel(r'Differential $\Delta D_q$', fontdict=font)
			#plt.title(u'Multifractality and robustness', fontdict=font)
			#axs[i,j].xticks(np.arange(min(percentNodes), max(percentNodes)+1, 10))
			lgd = axs[i,j].legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))
			axs[i,j].grid(True)

			#plt.savefig('output/graphics/'+"Dq"+fileOutput+timestr+'.svg', bbox_extra_artists=(lgd,),bbox_inches='tight',format="svg")	
	plt.savefig(fileOutput+timestr+'.svg', bbox_extra_artists=(lgd,),bbox_inches='tight',format="svg")	


			# font = {'weight': 'normal', 'size': 8}
			# fig4 = plt.figure()
			# ax = fig4.add_subplot(111)
			# RRandom = np.nansum(DqRandom,axis=0)/(DqRandom.shape[0])
			# RDegree = np.nansum(DqDegree,axis=0)/(DqDegree.shape[0])
			# RCentrality = np.nansum(DqCentrality,axis=0)/(DqDegree.shape[0])
			# plt.plot(range(0,maxq),RRandom[IndexZero:-1],'r-' , label = u'R random')
			# plt.plot(range(0,maxq),RDegree[IndexZero:-1],'g-' , label = u'R degree')
			# plt.plot(range(0,maxq),RCentrality[IndexZero:-1],'b-' , label = u'R centrality')
			# fontP = FontProperties()
			# fontP.set_size('small')
			# plt.xlabel('q', fontdict=font)
			# plt.ylabel(r'R-index', fontdict=font)
			# plt.title(u'R-index multifractality and robustness', fontdict=font)
			# lgd = plt.legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))
			# plt.grid(True)
			# plt.savefig('output/graphics/'+"R-index"+fileOutput+timestr+'.svg', bbox_extra_artists=(lgd,),bbox_inches='tight',format="svg")	
	

archivoA = sys.argv[1]
archivoB = sys.argv[2]
archivoC = sys.argv[3]
archivoD = sys.argv[4]
fileOutput = sys.argv[5]

data = generateArrays(archivoA, archivoB, archivoC,archivoD)
generateGraphics(data,fileOutput)
