#!/usr/bin/env python

import sys

def main():

    onecount = 0
    for arg in sys.argv[1:]:
        if '1' in arg: onecount += 1

    print 'There are %s fish in the sea!' % onecount

main()