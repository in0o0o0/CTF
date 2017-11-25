#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import chain
from os import sys

if __name__ == "__main__":
	N =  map(int,raw_input().split())
	coordinate = [[] for x in range(4)] 

	pattern=["010010010111","010010011110","010011010110","011010010110","010010111100","010011110100","011010110100","001011110100","010010111010","010011110010"]
	pattern2=["0101111010"]	

	x_min = min(N[0::2]) 
	y_min = min(N[1::2])

	length = sorted(set(N[0::2]))[1]-x_min 
	
	for x in range(0,len(N)-1,2):
		coordinate[0].append([((N[x]-x_min)/length),((N[x+1]-y_min)/length)]) 


	if max(N[0::2])-min(N[0::2]) > max(N[1::2])-min(N[1::2]):  
		for i,v in enumerate(coordinate[0]):
			coordinate[0][i] = [v[1],v[0]]

	for v in coordinate[0]:
		coordinate[1].append([abs(v[0]-2),abs(v[1])])
		coordinate[2].append([abs(v[0]),abs(v[1]-3)])
		coordinate[3].append([abs(v[0]-2),abs(v[1]-3)])
		
	for a in coordinate:
		binary = [[0 for x in range(3)] for y in range(4)]
		for b in a:
			try:
				binary[b[1]][b[0]]=1
			except:
				pass

		if "".join(map(str,list(chain.from_iterable(binary)))) in pattern:
			print  "1"
			sys.exit()


	for x in range(1,4):
		coordinate[x]=[]

	for v in coordinate[0]: 
		coordinate[1].append([abs(v[0]-1),abs(v[1])])
		coordinate[2].append([abs(v[0]),abs(v[1]-4)])
		coordinate[3].append([abs(v[0]-1),abs(v[1]-4)])

	for a in coordinate:
		binary = [[0 for x in range(2)] for y in range(5)]
		for b in a:
			try:
				binary[b[1]][b[0]]=1
			except:
				pass

		if "".join(map(str,list(chain.from_iterable(binary)))) in pattern2:
			print  "1"
			sys.exit()

	print 0












	