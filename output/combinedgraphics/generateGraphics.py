#!/usr/bin/python
# -*- coding: utf-8 -*- 

#Author: Carlos Andres Delgado
#Creation date 19th December 2020
#Last edition date 19th December 2020
#Description: Save and generate graphics
import numpy as np
#np.set_printoptions(threshold=np.inf)
import matplotlib.pyplot as plt
import time
import math
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
minq = -10
maxq = 10
IndexZero = 0
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
	
	
def generateGraphics(data,fileOutput, names):

	timestr = time.strftime("%Y%m%d_%H%M%S")
	font = {'weight': 'normal', 'size': 8}

	fig1, axs = plt.subplots(4, sharex=True, sharey=True)
	fig1.tight_layout(h_pad=2)
	#fig3.suptitle("Differential fractal in "+fileOutput+" networks")
	for i in range(0,4):	
		dataIn = data[i]

		deltaA = np.array([])
		deltaB = np.array([])
		deltaC = np.array([])

		DqRandom = dataIn[0]
		DqDegree = dataIn[1]
		DqCentrality = dataIn[2]
		
		print(type(DqRandom))
		for k in range(0,DqRandom.shape[0]):
			if k < DqRandom.shape[0]:
				deltaA = np.append(deltaA, np.abs(np.max(DqRandom[k])-np.min(DqRandom[i])))
			if k < DqDegree.shape[0]:
				deltaB = np.append(deltaB, np.abs(np.max(DqDegree[k])-np.min(DqDegree[i])))
			if k < DqCentrality.shape[0]:
				deltaC = np.append(deltaC, np.abs(np.max(DqCentrality[k])-np.min(DqCentrality[i])))
		axs[i].plot(percentNodes,deltaA,'r-' , label = r'$\Delta D_q$ random')
		axs[i].plot(percentNodes,deltaB,'g-' , label = r'$\Delta D_q$ degree')
		axs[i].plot(percentNodes,deltaC,'b-' , label = r'$\Delta D_q$ centrality')
		#fontP = FontProperties()
		#fontP.set_size('small')
		
		axs[i].set_xlabel('Lost nodes (%)', fontdict=font)
		axs[i].set_ylabel(r'$\Delta D_q$', fontdict=font)
		axs[i].yaxis.set_major_locator(MultipleLocator(1))
		axs[i].set_xlim(0,95)
		axs[i].xaxis.set_major_locator(MultipleLocator(5))
		#plt.title(u'Multifractality and robustness', fontdict=font)
		#axs[i,j].xticks(np.arange(min(percentNodes), max(percentNodes)+1, 10))
		#lgd = axs[i,j].legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))
		axs[i].grid(True)
		#plt.savefig('output/graphics/'+"Dq"+fileOutput+timestr+'.svg', bbox_extra_artists=(lgd,),bbox_inches='tight',format="svg")	
	#plt.savefig(fileOutput+timestr+'.svg', bbox_extra_artists=(lgd,),bbox_inches='tight',format="svg")
	axs[0].set_title(names[0], y=0, pad=-70, verticalalignment="top", fontdict=font)
	axs[1].set_title(names[1], y=0, pad=-70, verticalalignment="top", fontdict=font)
	axs[2].set_title(names[2], y=0, pad=-70, verticalalignment="top", fontdict=font)
	axs[3].set_title(names[3], y=0, pad=-85, verticalalignment="top", fontdict=font)
	lgd = axs[0].legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))
	fig1.savefig(fileOutput+timestr+'.svg',bbox_extra_artists=(lgd,),bbox_inches='tight',format="svg")	


	fig2, axs = plt.subplots(4, sharex=True, sharey=True)
	fig2.tight_layout(h_pad=2)
	for i in range(0,4):	
		dataIn = data[i]

		deltaA = np.array([])
		deltaB = np.array([])
		deltaC = np.array([])

		DqRandom = dataIn[0]
		DqDegree = dataIn[1]
		DqCentrality = dataIn[2]
		font = {'weight': 'normal', 'size': 8}

		RRandom = np.nansum(DqRandom,axis=1)/(DqRandom.shape[1])
		RDegree = np.nansum(DqDegree,axis=1)/(DqDegree.shape[1])
		RCentrality = np.nansum(DqCentrality,axis=1)/(DqDegree.shape[1])
		
		
		axs[i].plot(percentNodes,RRandom,'r-' , label = u'R random')
		axs[i].plot(percentNodes,RDegree,'g-' , label = u'R degree')
		axs[i].plot(percentNodes,RCentrality,'b-' , label = u'R centrality')
		
		
		axs[i].set_xlabel('% nodes', fontdict=font)
		axs[i].set_ylabel(r'R-index', fontdict=font)
		axs[i].yaxis.set_major_locator(MultipleLocator(1))
		axs[i].set_xlim(0,maxq)
		axs[i].xaxis.set_major_locator(MultipleLocator(5))
		#axs[i,j].xticks(np.arange(min(percentNodes), max(percentNodes)+1, 10))
		#lgd = axs[i,j].legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))
		axs[i].grid(True)
		#plt.savefig('output/graphics/'+"Dq"+fileOutput+timestr+'.svg', bbox_extra_artists=(lgd,),bbox_inches='tight',format="svg")	
	#plt.savefig(fileOutput+timestr+'.svg', bbox_extra_artists=(lgd,),bbox_inches='tight',format="svg")
	axs[0].set_title(names[0], y=0, pad=-70, verticalalignment="top", fontdict=font)
	axs[1].set_title(names[1], y=0, pad=-70, verticalalignment="top", fontdict=font)
	axs[2].set_title(names[2], y=0, pad=-70, verticalalignment="top", fontdict=font)
	axs[3].set_title(names[3], y=0, pad=-85, verticalalignment="top", fontdict=font)
	lgd = axs[0].legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))
	fig2.savefig("R-index"+fileOutput+timestr+'.svg', bbox_extra_artists=(lgd,),bbox_inches='tight',format="svg")	
	

archivoA = sys.argv[1]
archivoB = sys.argv[2]
archivoC = sys.argv[3]
archivoD = sys.argv[4]
fileOutput = sys.argv[5]

data = generateArrays(archivoA, archivoB, archivoC,archivoD)
names = ["a)hub degree 50","b)hub degree 100","c)hub degree 200","d)hub degree 500"]
generateGraphics(data,fileOutput,names)
