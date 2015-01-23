#!/usr/bin/env python

from os import listdir

def runProg():
	pia = '/home/pi/pia'
	files = listdir(pia)
	for f in files:
		if f[:4] == 'ovpn':
			print f
	
if __name__ == '__main__':
	runProg()
