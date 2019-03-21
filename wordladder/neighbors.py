#! /usr/bin/python3

import sys

def read_dictall():
    dict_f = open("dictall.txt", "r")
    dict_f_cont = dict_f.read()
    words = dict_f_cont.split('\n')
    subdict = set()
    for i in range(len(words)):
        if len(words[i])==4:
            subdict.add(words[i])
    return subdict

def read_input():
    req_f = open(sys.argv[1], "r")
    req_f_cont = req_f.read()
    requests = req_f_cont.split('\n')
    req_f.close()
    index = len(requests)-1
    while requests[index]=='':
        del requests[index]
        index-=1
    return requests

def makeDict(subdict):
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

def find_num_nbors(requests, subdict):
    nbors = makeDict(subdict)
    result = []
    for x in range(len(requests)):
        result.append([requests[x],len(nbors[requests[x]])])
    return result

def write_output(array):
    ans_f = open(sys.argv[2], 'w')
    for x in range(len(array)):
        ans_f.write(array[x][0] + ',' + str(array[x][1]) + '\n')
    ans_f.close()

def main():
    requests = read_input()
    words = read_dictall()
    #start = time.time()
    answers = find_num_nbors(requests, words)
    #print(str(time.time() - start))
    write_output(answers)
    #print(words)

main()
