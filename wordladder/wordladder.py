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

class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == []

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

class Node:
    def __init__(self, value):
        self.word = value
        self.dist = NULL
        self.path = []

def my_cmp(node1, node2):
    for x in range(len(node1.word)):
        if node1.word[x]!=node2.word[x]:
            return False
    return True

def search(input):
    nbors = makeDict()
    #print(nbors)
    output = ""
    for x in input:
        explored = []
        frontier = PriorityQueue()
        frontier.append(Node(x.split(',')[0]))
        current = frontier.delete()
        for x in nbors[current.word]:
            frontier.insert(Node(x))
        while !my_cmp(Node(current), Node(x.split(',')[1])):

        output.append(','.join(current.path) + "\n")
    return output

def main():
    requests = read_input()
    search(requests)

main()
