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
	
	
def generateGraphics(data,fileOutput):

	timestr = time.strftime("%Y%m%d_%H%M%S")
	font = {'weight': 'normal', 'size': 8}

	fig1, axs = plt.subplots(3, sharex=True)

	#fig3.suptitle("Differential fractal in "+fileOutput+" networks")
	
	names = ["4000 nodes","8000 nodes","16000 nodes","64000 nodes"]
	attack = ["a) random","b) degree","c) centrality"]
	color = ["r","b","g","k"]
	statusA = ["r--","r-","r--","r-"]
	statusB = ["b--","b-","b--","b-"]
	
	ax2 = []
	for k in range(0,3):
		ax2.append(axs[k].twinx())	
		
	for k in range(0,3):
		ax2[k].set_ylabel(r'$\Delta D_q$',color='blue')	
		ax2[k].tick_params(axis='y', labelcolor='blue')	
		#ax2[k].yaxis.set_major_locator(MultipleLocator(0.5))		
	
	#File1, file2, file3, file4
	for i in range(0,2):
		Dq = data[:][i]
		
		#Random, #Degree, #centrality
		for k in range(0,3):
			element = Dq[k]
			rindex  = np.sum(element,axis=1)/element.shape[1]
			differential = np.abs(np.amax(element,axis=1)-np.amin(element,axis=1))
			
			#axs[k].plot(percentNodes,rindex,color[i]+'--' , label = u'R '+names[i])		
			axs[k].plot(percentNodes,rindex,statusA[i], label = u'R '+names[i])		
			axs[k].set_ylabel('R',color='red')
			axs[k].tick_params(axis='y', labelcolor='red')			
					
			#ax2.plot(percentNodes,differential,color[i]+':' , label = r'$\Delta D_q$ '+names[i])
			ax2[k].plot(percentNodes,differential,statusB[i] , label = r'$\Delta D_q$ '+names[i])
			
			axs[k].set_xlabel('% nodes', fontdict=font)


	for k in range(0,3):
		#axs[k].yaxis.set_major_locator(MultipleLocator(0.5))
		axs[k].set_xlim(0,95)
		axs[k].xaxis.set_major_locator(MultipleLocator(5))
		axs[k].set_title(attack[k], fontdict=font)
		#axs[k].grid()		
	fig1.tight_layout()		
	lgd = axs[0].legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1.2,1))	
	lgd2 = ax2[0].legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1.2,0.6))	
	fig1.savefig('4000-8000'+fileOutput+'.svg',bbox_extra_artists=(lgd,lgd2),bbox_inches='tight',format="svg")	
	
	#fig1.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
	#fig1.savefig('50-100'+fileOutput+'.svg',format="svg")	
	##SECOND
	
	timestr = time.strftime("%Y%m%d_%H%M%S")
	font = {'weight': 'normal', 'size': 8}

	fig2, axs = plt.subplots(3, sharex=True)

	#fig3.suptitle("Differential fractal in "+fileOutput+" networks")
	
	attack = ["a) random","b) degree","c) centrality"]
	color = ["r","b","g","k"]
	
	ax2 = []
	for k in range(0,3):
		ax2.append(axs[k].twinx())	
		
	for k in range(0,3):
		ax2[k].set_ylabel(r'$\Delta D_q$',color='blue')	
		ax2[k].tick_params(axis='y', labelcolor='blue')	
		#ax2[k].yaxis.set_major_locator(MultipleLocator(0.5))		
		ax2[k].legend()
		
	#File1, file2, file3, file4
	for i in range(2,4):
		Dq = data[:][i]
		
		#Random, #Degree, #centrality
		for k in range(0,3):
			element = Dq[k]
			rindex  = np.sum(element,axis=1)/element.shape[1]
			differential = np.abs(np.amax(element,axis=1)-np.amin(element,axis=1))
			
			#axs[k].plot(percentNodes,rindex,color[i]+'--' , label = u'R '+names[i])		
			axs[k].plot(percentNodes,rindex,statusA[i], label = u'R '+names[i])	
			axs[k].set_ylabel('R',color='red')
			axs[k].tick_params(axis='y', labelcolor='red')			
					
			#ax2.plot(percentNodes,differential,color[i]+':' , label = r'$\Delta D_q$ '+names[i])
			ax2[k].plot(percentNodes,differential,statusB[i] , label = r'$\Delta D_q$ '+names[i])
			
			axs[k].set_xlabel('% nodes', fontdict=font)



	for k in range(0,3):
		#axs[k].yaxis.set_major_locator(MultipleLocator(0.5))
		axs[k].set_xlim(0,95)
		axs[k].xaxis.set_major_locator(MultipleLocator(5))
		axs[k].set_title(attack[k], fontdict=font)
		#axs[k].grid()				
	fig2.tight_layout()	
	lgd = axs[0].legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1.1,1))	
	lgd2 = ax2[0].legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1.1,0.6))	
	fig2.savefig('16000-64000'+fileOutput+'.svg',bbox_extra_artists=(lgd,lgd2),bbox_inches='tight',format="svg")	
	#fig2.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
	#fig2.savefig('200-500'+fileOutput+'.svg',format="svg")	
	# DqRandom 

	# RRandomA = np.nansum(DqRandomA,axis=1)/(DqRandomA.shape[1])
	# RRandomB = np.nansum(DqRandomB,axis=1)/(DqRandomB.shape[1])
	# RRandomC = np.nansum(DqRandomC,axis=1)/(DqRandomC.shape[1])
	
	# DeltaRandomA 
	# DeltaRandomB
	# DeltaRandomC
	
	# deltaA = np.append(deltaA, np.abs(np.max(DqRandom[k])-np.min(DqRandom[i])))
	# #Degree
	
	# #Centrality
	
	
	
	# for i in range(0,4):	
		# dataIn = data[i]

		# deltaA = np.array([])
		# deltaB = np.array([])
		# deltaC = np.array([])

		# DqRandom = dataIn[0]
		# DqDegree = dataIn[1]
		# DqCentrality = dataIn[2]
		
		# RRandom = np.nansum(DqRandom,axis=1)/(DqRandom.shape[1])
		# RDegree = np.nansum(DqDegree,axis=1)/(DqDegree.shape[1])
		# RCentrality = np.nansum(DqCentrality,axis=1)/(DqDegree.shape[1])
		
		# De
				
		# for k in range(0,DqRandom.shape[0]):
			# if k < DqRandom.shape[0]:
				# deltaA = np.append(deltaA, np.abs(np.max(DqRandom[k])-np.min(DqRandom[i])))
			# if k < DqDegree.shape[0]:
				# deltaB = np.append(deltaB, np.abs(np.max(DqDegree[k])-np.min(DqDegree[i])))
			# if k < DqCentrality.shape[0]:
				# deltaC = np.append(deltaC, np.abs(np.max(DqCentrality[k])-np.min(DqCentrality[i])))
		# axs[i].plot(percentNodes,deltaA,'ro' , label = r'$\Delta D_q$ random')
		# axs[i].plot(percentNodes,deltaB,'go' , label = r'$\Delta D_q$ degree')
		# axs[i].plot(percentNodes,deltaC,'bo' , label = r'$\Delta D_q$ centrality')
		# axs[i].plot(percentNodes,RRandom,'r.' , label = u'R random')
		# axs[i].plot(percentNodes,RDegree,'g.' , label = u'R degree')
		# axs[i].plot(percentNodes,RCentrality,'b.' , label = u'R centrality')
		# #fontP = FontProperties()
		# #fontP.set_size('small')
		
		# axs[i].set_xlabel('Lost nodes (%)', fontdict=font)
		# axs[i].set_ylabel(r'$\Delta D_q$', fontdict=font)
		# axs[i].yaxis.set_major_locator(MultipleLocator(1))
		# axs[i].set_xlim(0,95)
		# axs[i].xaxis.set_major_locator(MultipleLocator(5))
		# #plt.title(u'Multifractality and robustness', fontdict=font)
		# #axs[i,j].xticks(np.arange(min(percentNodes), max(percentNodes)+1, 10))
		# #lgd = axs[i,j].legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))
		# axs[i].grid(True)
		# #plt.savefig('output/graphics/'+"Dq"+fileOutput+timestr+'.svg', bbox_extra_artists=(lgd,),bbox_inches='tight',format="svg")	
	# #plt.savefig(fileOutput+timestr+'.svg', bbox_extra_artists=(lgd,),bbox_inches='tight',format="svg")
	# axs[0].set_title(names[0], y=0, pad=-70, verticalalignment="top", fontdict=font)
	# axs[1].set_title(names[1], y=0, pad=-70, verticalalignment="top", fontdict=font)
	# axs[2].set_title(names[2], y=0, pad=-70, verticalalignment="top", fontdict=font)
	# axs[3].set_title(names[3], y=0, pad=-85, verticalalignment="top", fontdict=font)
	# lgd = axs[0].legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))
	# fig1.savefig(fileOutput+'.svg',bbox_extra_artists=(lgd,),bbox_inches='tight',format="svg")	


	# fig2, axs = plt.subplots(4, sharex=True, sharey=True)
	# fig2.tight_layout(h_pad=2)
	# for i in range(0,4):	
		# dataIn = data[i]

		# deltaA = np.array([])
		# deltaB = np.array([])
		# deltaC = np.array([])

		# DqRandom = dataIn[0]
		# DqDegree = dataIn[1]
		# DqCentrality = dataIn[2]
		# font = {'weight': 'normal', 'size': 8}

		# RRandom = np.nansum(DqRandom,axis=1)/(DqRandom.shape[1])
		# RDegree = np.nansum(DqDegree,axis=1)/(DqDegree.shape[1])
		# RCentrality = np.nansum(DqCentrality,axis=1)/(DqDegree.shape[1])
		
		
		# axs[i].plot(percentNodes,RRandom,'r-' , label = u'R random')
		# axs[i].plot(percentNodes,RDegree,'g-' , label = u'R degree')
		# axs[i].plot(percentNodes,RCentrality,'b-' , label = u'R centrality')
		
		
		# axs[i].set_xlabel('% nodes', fontdict=font)
		# axs[i].set_ylabel(r'R-index', fontdict=font)
		# axs[i].yaxis.set_major_locator(MultipleLocator(1))
		# axs[i].set_xlim(0,95)
		# axs[i].xaxis.set_major_locator(MultipleLocator(5))
		# #axs[i,j].xticks(np.arange(min(percentNodes), max(percentNodes)+1, 10))
		# #lgd = axs[i,j].legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))
		# axs[i].grid(True)
		# #plt.savefig('output/graphics/'+"Dq"+fileOutput+timestr+'.svg', bbox_extra_artists=(lgd,),bbox_inches='tight',format="svg")	
	# #plt.savefig(fileOutput+timestr+'.svg', bbox_extra_artists=(lgd,),bbox_inches='tight',format="svg")
	# axs[0].set_title(names[0], y=0, pad=-70, verticalalignment="top", fontdict=font)
	# axs[1].set_title(names[1], y=0, pad=-70, verticalalignment="top", fontdict=font)
	# axs[2].set_title(names[2], y=0, pad=-70, verticalalignment="top", fontdict=font)
	# axs[3].set_title(names[3], y=0, pad=-85, verticalalignment="top", fontdict=font)
	# lgd = axs[0].legend(loc='upper left', prop={'size':8}, bbox_to_anchor=(1,1))
	# fig2.savefig("R-index"+fileOutput+timestr+'.svg', bbox_extra_artists=(lgd,),bbox_inches='tight',format="svg")	
	

archivoA = sys.argv[1]
archivoB = sys.argv[2]
archivoC = sys.argv[3]
archivoD = sys.argv[4]
fileOutput = sys.argv[5]

data = generateArrays(archivoA, archivoB, archivoC,archivoD)

generateGraphics(data,fileOutput)
