#!/usr/bin/python
# -*- coding: utf-8 -*- 
import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.font_manager import FontProperties
import sys
import tokenize

def getData(fileName):
	archivo = fileName
	#Random
	fileInput = open(archivo,"r")
	fileInput.readline() 

	numbers = np.array([])
	while True:
		aux = fileInput.readline()
		if aux=="RandomAttack\n":
			break
		
		aux = aux.replace("[","")
		aux = aux.replace("]","")
		aux = aux.replace("\n","")
		listaS = aux.split(",")
		if '' in listaS:
			listaS.remove('')
		numbers = np.append(numbers, ([float(x) for x in listaS]))

	percentNodes = numbers

	fileInput.readline() 

	numbers = np.array([])
	while True:
		aux = fileInput.readline()
		if aux=="measureGC\n":
			break
		aux = aux.replace("[","")
		aux = aux.replace("]","")
		aux = aux.replace("\n","")
		listaS = aux.split(",")
		if '' in listaS:
			listaS.remove('')
		numbers = np.append(numbers, ([float(x) for x in listaS]))
	TqRandom = numbers.reshape(-1,11)

	numbers = np.array([])
	while True:
		aux = fileInput.readline()
		if aux=="measureAPL\n":
			break
		aux = aux.replace("[","")
		aux = aux.replace("]","")
		aux = aux.replace("\n","")
		listaS = aux.split(",")
		if '' in listaS:
			listaS.remove('')
		numbers = np.append(numbers, ([float(x) for x in listaS]))
		
	GCRandom = numbers

	numbers = np.array([])
	while True:
		aux = fileInput.readline()
		if aux=="Degree\n":
			break
		aux = aux.replace("[","")
		aux = aux.replace("]","")
		aux = aux.replace("\n","")
		listaS = aux.split(",")
		if '' in listaS:
			listaS.remove('')
		numbers = np.append(numbers, ([float(x) for x in listaS]))

	APLRandom = numbers

	#Degree
	fileInput.readline() 

	numbers = np.array([])
	while True:
		aux = fileInput.readline()
		if aux=="measureGC\n":
			break
		aux = aux.replace("[","")
		aux = aux.replace("]","")
		aux = aux.replace("\n","")
		listaS = aux.split(",")
		if '' in listaS:
			listaS.remove('')
		numbers = np.append(numbers, ([float(x) for x in listaS]))
	TqDegree = numbers.reshape(-1,11)

	numbers = np.array([])
	while True:
		aux = fileInput.readline()
		if aux=="measureAPL\n":
			break
		aux = aux.replace("[","")
		aux = aux.replace("]","")
		aux = aux.replace("\n","")
		listaS = aux.split(",")
		if '' in listaS:
			listaS.remove('')
		numbers = np.append(numbers, ([float(x) for x in listaS]))
		
	GCDegree = numbers


	numbers = np.array([])
	while True:
		aux = fileInput.readline()
		if aux=="Centrality\n":
			break
		aux = aux.replace("[","")
		aux = aux.replace("]","")
		aux = aux.replace("\n","")
		listaS = aux.split(",")
		if '' in listaS:
			listaS.remove('')
		numbers = np.append(numbers, ([float(x) for x in listaS]))

	APLDegree= numbers
	#Centrality

	fileInput.readline() 


	numbers = np.array([])
	while True:
		aux = fileInput.readline()
		if aux=="measureGC\n":
			break
		aux = aux.replace("[","")
		aux = aux.replace("]","")
		aux = aux.replace("\n","")
		listaS = aux.split(",")
		if '' in listaS:
			listaS.remove('')
		numbers = np.append(numbers, ([float(x) for x in listaS]))
	TqCentrality = numbers.reshape(-1,11)


	numbers = np.array([])
	while True:
		aux = fileInput.readline()
		if aux=="measureAPL\n":
			break
		aux = aux.replace("[","")
		aux = aux.replace("]","")
		aux = aux.replace("\n","")
		listaS = aux.split(",")
		if '' in listaS:
			listaS.remove('')
		numbers = np.append(numbers, ([float(x) for x in listaS]))
		
	GCCentrality = numbers

	numbers = np.array([])
	while True:
		aux = fileInput.readline()
		if aux=="":
			break
		aux = aux.replace("[","")
		aux = aux.replace("]","")
		aux = aux.replace("\n","")
		listaS = aux.split(",")
		if '' in listaS:
			listaS.remove('')
		numbers = np.append(numbers, ([float(x) for x in listaS]))

	APLCentrality = numbers
	
	
	fileInput.close()
	return [TqRandom, TqDegree, TqCentrality, GCRandom, APLRandom, GCDegree, APLDegree, GCCentrality, APLCentrality]
