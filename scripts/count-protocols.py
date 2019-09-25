#!/usr/bin/env python

import sys
import re

def main():
    file = open(sys.argv[1], 'r')
    dump = file.read().split('\n')
    
    # find all of the protocols being used
    protodict = {}
    for line in dump:
        proto = ''
        proto = re.findall(r"PROTO=\w+", line)
        print proto
        if len(proto) > 0: count += 1

            
main()
