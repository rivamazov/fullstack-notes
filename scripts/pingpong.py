#!/usr/bin/env python

import sys
import requests

def main():

    PINGURL = sys.argv[1]
    PONGURL = sys.argv[2]

    teststr = sys.argv[3]
    teststr = 'hashme'

    flag = ''

    def isflag(string):
        if '}' in string:
            return True
        else: return False
    
    def pingorpong(url, food, inflag):
        print food
        if '}' in food:
            return
        else:
            response = requests.post(url, {'food': food})
            rdata = response.text
            print response.text
            rdata = rdata.split()[2]
            return rdata
        
    while len(flag) < 5 :

        teststr = pingorpong(PINGURL, teststr, flag)
        teststr = pingorpong(PONGURL, teststr, flag)

    print flag

main()