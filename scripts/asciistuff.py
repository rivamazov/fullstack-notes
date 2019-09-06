#!/usr/bin/env python

import sys

def main():
    
    file = open(sys.argv[1], 'r')
    numlist = file.read().split(' ')
    retstr = ''
    for number in numlist:
        retstr += chr(int(number, 16))
        
    print retstr
    return 9000
    
main()

    