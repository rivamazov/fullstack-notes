#!/usr/bin/env python

import sys
import re

def main():

    file = open(sys.argv[1], 'r')
    dump = file.read().split('\n')

    protoarr = []
    for line in dump:
        proto = re.findall(r"PROTO=\w+", line)
        # use proto[0] because re returns a list not a string
        if proto: protoarr.append(proto[0])
        
    protodict = {}
    for proto in protoarr:
        if proto not in protodict:
            protodict[proto] = 1
        else:
            protodict[proto] += 1

    print protodict
if __name__ == main():
    main()
