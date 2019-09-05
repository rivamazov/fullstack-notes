#!/usr/bin/env python


# TODO fix this

import sys

def filterftpclients(filename):
	"""
	take in a filename
	return all of the lines that pertain to ftp clients
		- dest port == 21
	"""
	f = open(filename)
	lines = f.readlines()

	output = []
	for line in lines:
		print line
		# add this to my output iff dest port == 21
		destport = line[5]

		line = line.split(';')

		if destport == '21':
			output.append(line.strip())

	return output


def extractsrcip(packets):
	"""
	take a list of lines
	return only the dictionary of source IPs and counts
	"""

	output = dict()
	for p in packets:
		srcip = p.split[3]
		if p in output:
			output[srcip] = output[srcip] + 1
		else:
			output[srcip] = 1
	return output

def mostfrequentip(ipcounts):
    # freq = max([(value, key)] for key, value in ipcouts.items()])[1])

def main():
	filename = sys.argv[1]
	ftpclients = filterftpclients(filename)
	srcips = extractsrcip(ftpclients)
	print srcip
	mostfrequent = mostfrequentips(srcips)
	print mostfrequent

main()
