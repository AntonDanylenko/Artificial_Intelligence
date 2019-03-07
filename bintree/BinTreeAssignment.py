#! /usr/bin/python3

import math

class Node:
    def __init__(self, data):
        self.value = data
        self.smaller = None
        self.larger = None

    def __str__(self):
        return str(self.value)

class BinTree:
    def __init__(self, A = None):
        # A is an optional argument containing a list of values to be inserted into the binary tree just after cosntruction
        self.root = None
        for n in A:
          #print(n)
          self.insert(n)

    def insert(self, V):
        # inserts a new value
        #print("\nInsert V=" + str(V))
        if self.root==None:
          self.root = Node(V)
          return
        else:
          node = self.root
          #print("node: " + str(node.value))
          while node.smaller or node.larger:
            #print("node.value: " + str(node.value) + " vs V: " + str(V))
            if V==node.value:
              return
            if V>node.value:
              if node.larger:
                #print("node.larger: " + str(node.larger.value))
                node = node.larger
              else:
                #print("mklarger")
                #print("node.larger: " + str(node.larger.value))
                node.larger = Node(V)
                return
            else:
              if node.smaller:
                #print("node.smaller: " + str(node.smaller.value))
                node = node.smaller
              else:
                #print("mksmaller")
                #print("node.smaller: " + str(node.smaller.value))
                node.smaller = Node(V)
                return
          if V>node.value and node.larger==None:
            #print("mklargerend")
            node.larger = Node(V)
            return
          elif V<node.value and node.smaller==None:
            #print("mksmallerend")
            node.smaller = Node(V)
            return

    def has(self, V):
        # returns True if V is in the list, else False
        #print("\nHas? V=" + str(V))
        node = self.root
        while node:
          if V==node.value:
            #print(str(V) + " found!")
            return True
          if node.larger and V>node.value:
            node = node.larger
          elif node.smaller and V<node.value:
            node = node.smaller
          else:
            return False
        return False

    def get_ordered_list(self):
        # returns a list of all values in ordered sequence
        return self.help_order(self.root)

    def help_order(self, node):
        #if node:
        #    print("node: " + str(node.value))
        if node==None:
          return []
        else:
          list = []
          temp = self.help_order(node.smaller)
          #print("tempA: " + str(temp))
          if temp:
            list.extend(temp)
          list.append(node.value)
          temp = self.help_order(node.larger)
          #print("tempB: " + str(temp))
          if temp:
            list.extend(temp)
          #print("list: " + str(list))
          return list

    def clear(self):
        # clears the list of all nodes
        self.help_clear(self.root)
        #print(self.get_ordered_list())
        self.root = None

    def help_clear(self, node):
        if node.smaller and node.smaller.smaller==None and node.smaller.larger==None:
          #print("node.smaller.value: " + str(node.smaller.value))
          node.smaller = None
        elif node.smaller:
          self.help_clear(node.smaller)
          node.smaller = None
        if node.larger and node.larger.smaller==None and node.larger.larger==None:
          #print("node.larger.value: " + str(node.larger.value))
          node.larger = None
        elif node.larger:
          self.help_clear(node.larger)
          node.larger = None

    def has_depth(self, V):
        node = self.root
        depth = 1
        while node:
          if V==node.value:
            #print(str(V) + " found!")
            return depth
          if node.larger and V>node.value:
            node = node.larger
            #print("Depth+=1(larger)")
            depth+=1
          elif node.smaller and V<node.value:
            node = node.smaller
            #print("Depth+=1(smaller)")
            depth+=1
          else:
            return depth
        return depth


def Process(infilename, outfilename):
  try:
    f=open(infilename,'rU')
    lines = f.read().split('\n')
    f.close()
  except:
    print('infile not read')
    return
  input_words = lines[0].split(',')
  input_ints = [int(x) for x in input_words]
  tree = BinTree(input_ints)
  find_words = lines[1].split(',')
  find_ints = [int(x) for x in find_words]
  output = ','.join(find_ints)
  try:
    f.open(outfilename,'w')
    f.write(output + "\n")
    f.close
  except:
    print('outfile not written to')
    return
  return

tree = BinTree([5,2,4,2,10,8,1,16,5,1])
avg_sum = 0
for n in [4,8,7,5,16,1,9,2,10]:
  print("Has " + str(n) + "? " + str(tree.has(n)))
  print("Depth of " + str(n) + ": " + str(tree.has_depth(n)) + "\n")
  avg_sum+=tree.has_depth(n)
print("avg: " + str(avg_sum/9))
print(math.log(7,2))
print(tree.get_ordered_list())
tree.clear()
