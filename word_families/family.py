#! /usr/bin/python3

'''
DG and AD
AI Period 9
'''
class Pqueue:

    def OrdinaryComparison(a,b):
        #print("a",a)
        #print("b",b)
        if a < b: return -1
        if a == b: return 0
        return 1

    def __init__(self, comparator = OrdinaryComparison):
        self.cmpfunc = comparator
        self.queue = [None]
        self.end = None

    def swap(self,index1,index2):
        temp = self.queue[index1]
        self.queue[index1]=self.queue[index2]
        self.queue[index2]=temp

    def push(self,data):

        # if nothing in the 1st slot
        if self.end == None or self.end == 0:
            self.queue.append(data)
            self.end = 1
            return

        else:
            self.queue.append(data)
            self.end += 1
            #print(self.queue)

            # Bubble up


            dataIndex = self.end
            #print("dataIndex",dataIndex)
            parentIndex = int(dataIndex/2)
            #print("parentIndex",parentIndex)
            #print(self.queue[parentIndex])
            #print(self.queue[1])

            # Initial check if data appended is in wrong place. 1 if True
            wrongPlace = self.cmpfunc( self.queue[parentIndex] , data)


            # while the data is smaller than the parent
            while wrongPlace == 1:

              # swap parent and child
              self.swap(dataIndex,parentIndex)
              dataIndex = parentIndex
              parentIndex = int(dataIndex/2)

              if (parentIndex > 0 ):
                wrongPlace = self.cmpfunc( self.queue[parentIndex] , data)
              else:
                return



    def peek(self):
        if self.end >= 1:
          return self.queue[1]
        return None

    def pop(self):
        # if queue has no data
        if self.end == 0:
            return None
        # if only 1 elem
        elif self.end == 1:
            self.end -= 1
            return self.queue.pop(1)

        else:
            return self.bubbleDown()

    def bubbleDown(self):

      #Inital
      result = self.queue[1]

      trackIndex = 1
      result = self.queue[1]
      self.queue[1] = self.queue[self.end]
      self.queue.pop(self.end)
      self.end -= 1

      trackNode = self.queue[trackIndex]
      leftIndex = 2
      rightIndex = 3

      #**********CHOOSING WHICH CHILD TO SWAP WITH************************

      #if left smaller than right

      if (leftIndex > self.end):
        return result

      elif (rightIndex > self.end and leftIndex <= self.end):
        childIndex = leftIndex

      elif self.cmpfunc( self.queue[leftIndex] , self.queue[rightIndex] ) == -1:
        childIndex = leftIndex
      elif self.cmpfunc( self.queue[leftIndex] , self.queue[rightIndex] ) == 0:
        childIndex = leftIndex
      else:
        childIndex = rightIndex
      #********************************************************************

      # wrongPlace = 1 if trackNode > node at childIndex
      wrongPlace = self.cmpfunc( trackNode, self.queue[childIndex] )

      #while node being tracked is in the wrong place
      while wrongPlace == 1:

        self.swap( trackIndex , childIndex )

        trackIndex = childIndex
        leftIndex = trackIndex * 2
        rightIndex = trackIndex * 2 + 1


        if (leftIndex >= self.end):
          break

        if self.cmpfunc( self.queue[leftIndex] , self.queue[rightIndex] ) == -1:
          childIndex = leftIndex
        elif self.cmpfunc( self.queue[leftIndex] , self.queue[rightIndex] ) == 0:
          childIndex = leftIndex
        else:
          childIndex = rightIndex

        wrongPlace = self.cmpfunc( trackNode, self.queue[childIndex] )
      return result

    def tolist(self):
        lout = []
        if self.end == None:
            return lout
        for x in range(self.end):
            lout.append( self.pop() )
        return lout

class Word:
    def __init__(self,word,cost,path):
        self.word = word
        self.cost = cost
        self.path = path

    '''Edit comparison operators for a Word object'''

    def __lt__(self, other):
        return self.cost < other.cost
    def __gt__(self, other):
        return self.cost > other.cost
    def __eq__(self, other):
        if other == None: return False
        return self.cost == other.cost
    def __str__(self):
        return str([self.word,self.cost])

import sys

'''processed = set()
test1 = Word("hear",2,"hean")
test2 = Word("head",1,"heal")
test3 = Word("heaf",3,"heap")
frontier = Pqueue()
frontier.push(test1)
frontier.push(test2)
frontier.push(test3)
print( frontier.peek() ) #head
#frontier.push(7)
#print(frontier.peek())'''

def makeDict(length, words):
    '''Makes dictionary of word:[]'''
    d = {}
    for str in words:
        #if length of the word in dictall matches length of input word
        if (len(str) == length):
            d[str] = []
    return d

def fillDict(word, dictionary, length):
    '''Fills dict with words of desired length and their neighbors'''
    for pos in range(length):
        for char in "abcdefghijklmnopqrstuvwxyz":
            if (char != word[pos]):
                new_word = word[:pos] + char + word[pos+1:]
                if new_word in dictionary:
                    #fill list
                    dictionary[word].append(new_word)

def num_diff(word, curr):
    '''Returns number of different letters current word has from other word'''
    counter = 0
    for i in range( len(curr) ):
        if(curr[i] != word[i]):
            counter += 1
    return counter

def total_cost(start,curr,target):
    '''Returns f (g+h) found in A*'''
    g = num_diff(start,curr)
    h = num_diff(curr,target)
    return g + h

def getLadder(start, end, dictionary):
    #print(start)
    #print(end)
    frontier = Pqueue()
    explored = set()
    origin = Word( start, total_cost(start,start,end), [] )
    frontier.push(origin)
    curr = None
    while(frontier.peek() != None) :
        curr = frontier.pop()
        #print("Current word",curr.word)

        # If we have reached the end (target)
        if (curr.word == end) :
            curr.path.append(curr.word)
            return curr.path
        # Skip current word if already explored
        if (curr.word in explored):
            continue
        # Add current word to explored
        # Add its neighbors to frontier
        for word in dictionary[curr.word]:
            if (word in explored):
                continue
            temp = Word(word, curr.cost + num_diff(word,start), curr.path + [curr.word])
            frontier.push(temp)
        # Add current word to explored once we pushed neighbors onto frontier
        explored.add(curr.word)
    return None


def main():
    dict_all = open("dictall.txt","r").read().strip().split()
    #print(dict_all)
    input_words = open(sys.argv[1],"r").read().strip().split()
    for i in range(len(input_words)):
        input_words[i] = input_words[i].split(",")
    #print(input_words)

    #length of input words
    length = len(input_words[0][0])
    dictionary = makeDict(length, dict_all)
    #print(dictionary)
    for word in dictionary:
        fillDict(word, dictionary, length)
    #print(dictionary)
    #print(input_words)
    #print(dict_all)
    f = open(sys.argv[2],"a")
    #print(len(dictionary.get('love')))

    #loop through input words and output answer path
    for pair in input_words:
        #print("the word",word)
        l = getLadder(pair[0],pair[1],dictionary)
        #print(l)
        if l:
            result = ",".join(l)
        else:
            result = pair[0] + "," + pair[1]
        f.write(result + "\n")

    f.close()

#main()

def completeDict(length):
    '''combines functions makeDict and fillDict'''
    # list of all words in dictall file
    dict_all = open("dictall.txt","r").read().strip().split()
    #print(dict_all)

    # make dictionary and fill it with neighbors
    dictionary = makeDict(length, dict_all)
    for word in dictionary:
        fillDict(word, dictionary, length)
    #print(dictionary)
    return dictionary



def getAllNeighborsWrapper(l,lenList):
    '''Wrapper for getAllNeighbors so dictionary of words is only made once
       instead of multiple times based on recursive calls'''
    dict_words = completeDict( len(l[0]) )
    #print(dict_words)
    return getAllNeighbors(l,lenList,dict_words)

def getAllNeighbors(l,lenList,dict_words):
    '''Gets all the neighbors of the words in a list
       and the length of the provided list.
       Should use a list of length 1. '''
    #print("the list",l)
    result = l
    for word in result:
        #print("word",word)
        #print(dict_words)
        l.extend(dict_words[word])
        l = set(l)
        l = list(l)

    #print( "lenList",lenList )
    #print( "len(l)",len(l) )
    if(lenList == len(l)):
        return l
    return getAllNeighbors(l,len(l),dict_words)

#print( getAllNeighbors(["alps"],1))

def findFamilies(length):
    '''returns a list of families provided length of words'''
    family = []
    families = []
    dictionary = completeDict(length)
    #print(dictionary)
    for word in dictionary:

        #  if the word isnt in any family we made
        if not any(word in sublist for sublist in families):
                family = getAllNeighborsWrapper([word],1)
                if len(family) > len(dictionary)/2:
                    print("Length: " + str(len(family)))
                    return family
                #print("family",family)
        else:
            #print("*************CONTINUE*************")
            continue
        #print("family before append",family)
        families.append(family)
        #print("families:",families)
        family = []

    print("Length: " + str(len(max(families, key=len))))
    return max(families, key=len)

#print( findFamilies(4) )
#findFamilies(5)
#findFamilies(6)
#findFamilies(7)
print(findFamilies(8))
