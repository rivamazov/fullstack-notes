#!/usr/bin/env python

import sys
import re

def main():

    def iptruthfullness(ip):
        ipbytes = ip.split('.')
        for octet in ipbytes:
            if int(octet) > 255 or len(octet) > 1 and octet[0] == '0': return False
        return True

    def drawhistogram(number):
        return '*' * (number / 50 + 1)

    file = open(sys.argv[1], 'r')
    dump = file.read().split('\n')
    
    # extract all IPs from every line in file
    tmparr = []
    for line in dump:
        ips = re.findall(r"\d+[.]\d+[.]\d+[.]\d+", line)
        if ips: tmparr.append(ips)

    # flatten any nested arrays (multiple IPs per line)
    iparr = reduce(lambda x, y: x+y, tmparr)

    # create dictionary of IPs with frequency as value
    ipdict = {}
    for ip in iparr:
        if ip not in ipdict:
            ipdict[ip] = 1
        else: ipdict[ip] += 1
    
    sortedip = sorted(ipdict.items(), key=lambda x: x[1])

    for tup in sortedip:
        print('(%03d) %5s:%18s %s' % (
                tup[1], 
                iptruthfullness(tup[0]),
                tup[0],
                drawhistogram(tup[1])))

if __name__ == main():
    main()
