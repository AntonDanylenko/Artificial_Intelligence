#! /usr/bin/python3

import sys
#import time

def read_dictall():
    dict_f = open("dictall.txt", "r")
    dict_f_cont = dict_f.read()
    words = dict_f_cont.split('\n')
    return words

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

def find_num_nbors(requests, words):
    result = []
    for x in range(len(requests)):
        subdict = []
        for i in range(len(words)):
            if len(words[i])==len(requests[x]):
                subdict.append(words[i])
        nbors = []
        for i in range(len(subdict)):
            num_equal = 0
            for s in range(len(requests[x])):
                if subdict[i][s]==requests[x][s]:
                    num_equal+=1
            if num_equal==len(requests[x])-1:
                nbors.append(subdict[i])
        result.append([requests[x],len(nbors)])
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
