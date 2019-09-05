#!/usr/bin/env python

import sys

def main():
    
    s = sys.argv[1]
    s_start = s[0]
    s_end = s[1:]
    s_end = s_end.replace(s_start, '*')
    retstr = s_start+s_end
    print retstr

main()