#!/usr/bin/python3
# -*- coding: utf-8 -*- 

#Author: Carlos Andres Delgado
#Creation date 20th December 2020
#Last edition date 20th December 2020
#Description: Generate testing networks
import snap
import numpy as np

def saveResults(graph, nameFile):
	snap.PrintInfo(graph, "Python type PUNGraph", "descriptions/"+nameFile, False)
	result_degree = snap.TIntV()
	snap.GetDegSeqV(graph, result_degree)

	file_object = open("descriptions/"+nameFile,'a') 
	deg = np.array([], dtype=int)
	file_object.write("\n")
	file_object.write("Degree\n")

	for i in range(0, result_degree.Len()):
		deg = np.append(deg, result_degree[i])
			
	file_object.write(np.array2string(deg, precision=8, separator=','))
	file_object.close()

Rnd = snap.TRnd()

###Scale Free
ScaleFree20 = snap.GenPrefAttach(2000, 20, Rnd)
snap.SaveEdgeList(ScaleFree20, 'ScaleFree20.txt')
saveResults(ScaleFree20, "ScaleFree20")

ScaleFree100 = snap.GenPrefAttach(2000, 100, Rnd)
snap.SaveEdgeList(ScaleFree100, 'ScaleFree100.txt')
saveResults(ScaleFree100, "ScaleFree100")

ScaleFree200 = snap.GenPrefAttach(2000,200, Rnd)
snap.SaveEdgeList(ScaleFree200, 'ScaleFree200.txt')
saveResults(ScaleFree200, "ScaleFree200")

ScaleFree500 = snap.GenPrefAttach(2000,500, Rnd)
snap.SaveEdgeList(ScaleFree500, 'ScaleFree500.txt')
saveResults(ScaleFree500, "ScaleFree500")

#SmallWorld

SmallWorld1 = snap.GenSmallWorld(2000, 500, 0, Rnd)
snap.SaveEdgeList(SmallWorld1, 'SmallWorldRewire00.txt')
saveResults(SmallWorld1, "SmallWorldRewire00")

SmallWorld2 = snap.GenSmallWorld(2000, 500, 0.1, Rnd)
snap.SaveEdgeList(SmallWorld2, 'SmallWorldRewire01.txt')
saveResults(SmallWorld2, "SmallWorldRewire01")

SmallWorld3 = snap.GenSmallWorld(2000, 500, 0.5, Rnd)
snap.SaveEdgeList(SmallWorld2, 'SmallWorldRewire05.txt')
saveResults(SmallWorld2, "SmallWorldRewire05")

SmallWorld4 = snap.GenSmallWorld(2000, 500, 0.7, Rnd)
snap.SaveEdgeList(SmallWorld2, 'SmallWorldRewire07.txt')
saveResults(SmallWorld2, "SmallWorldRewire07")

#Random

Random1 =snap.GenRndGnm(snap.PUNGraph, 2000, 4000)
snap.SaveEdgeList(Random1, 'Random4000.txt')
saveResults(Random1, "Random4000")

Random2 =snap.GenRndGnm(snap.PUNGraph, 2000, 8000)
snap.SaveEdgeList(Random2, 'Random8000.txt')
saveResults(Random2, "Random8000")

Random3 =snap.GenRndGnm(snap.PUNGraph, 2000, 16000)
snap.SaveEdgeList(Random3, 'Random16000.txt')
saveResults(Random3, "Random16000")

Random4 =snap.GenRndGnm(snap.PUNGraph, 2000, 64000)
snap.SaveEdgeList(Random3, 'Random64000.txt')
saveResults(Random4, "Random64000")

