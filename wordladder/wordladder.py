#! /usr/bin/python3

import sys

explored = []
frontier = []
unexplored = []

def read_input():
    req_f = open(sys.argv[1], "r")
    req_f_cont = req_f.read()
    requests = req_f_cont.split('\n')
    req_f.close()
    index = len(requests)-1
    while requests[index]=='':
        del requests[index]
        index-=1
    print(requests)
    return requests

def main():
    requests = read_input()
