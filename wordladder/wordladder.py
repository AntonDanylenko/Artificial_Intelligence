#! /usr/bin/python3

import sys

def makeDict():
    dict_f = open("dictall.txt", "r")
    dict_f_cont = dict_f.read()
    words = dict_f_cont.split('\n')
    subdict = set()
    for i in range(len(words)):
        if len(words[i])==4:
            subdict.add(words[i])
    result = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for x in subdict:
        result[x] = []
        word = x
        for i in range(len(x)):
            for s in alphabet:
                word = x[:i] + s + x[i+1:]
                if word in subdict and word != x:
                    result[x].append(word)
    #print(result)
    return result

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

def write_output(array):
    ans_f = open(sys.argv[2], 'w')
    for x in range(len(array)):
        ans_f.write(array[x][0] + ',' + str(array[x][1]) + '\n')
    ans_f.close()

class Node:
    def __init__(self, value):
        self.word = value
        self.dist = Null
        self.path = Null

def my_cmp(string1, string2):
    for x in range(len(string1)):
        if string1[x]!=string2[x]:
            return False
    return True

def search(input):
    nbors = makeDict()
    #print(nbors)
    for x in input:
        explored = []
        frontier = []
        unexplored = []
        unexplored.append(x.split(',')[0])
        frontier.append(unexplored[0])
        current = frontier[0]
        while !my_cmp(current, x.split(',')[1]):
            

def main():
    requests = read_input()
    search(requests)

main()
