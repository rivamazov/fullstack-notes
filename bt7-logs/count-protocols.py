#/usr/bin/env python

import sys
import re

def main():
    file = open(sys.argv[1], 'r')
    dump = file.read().split('\n')
    
    # TODO find all PROTO= lines and count them
    tmparr = []
    for line in dump:
        proto = re.findall(r"PROTO+", line)
        if proto: tmparr.append(proto)

if __name__ == main():
    main()