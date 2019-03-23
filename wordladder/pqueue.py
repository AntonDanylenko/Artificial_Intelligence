class PQueue:

  def OrdinaryComparison(self,a,b):
    if a < b: return -1
    if a == b: return 0
    return 1

  def __init__(self, comparator = None):
    if comparator == None:
      comparator = self.OrdinaryComparison
    self.queue = [0]
    self.length = 1
    self.cmpfunc = comparator

  def __str__(self):
    return "[[[" + '\n'.join([str(i) for i in self.queue]) + "]]]"

  def switch(self, a, b):
    temp = self.queue[a]
    self.queue[a] = self.queue[b]
    self.queue[b] = temp

  def push(self, data):
    if len(self.queue)>self.length:
      self.queue[self.length] = data
    else:
      self.queue.append(data)
    self.length+=1
    index = self.length-1
    while (index//2!=0 and self.cmpfunc(data, self.queue[index//2])==-1):
      self.switch(index, index//2)
      index = index//2

  def pop(self):
    if self.length>1:
      root = self.queue[1]
      #print("self.length: " + str(self.length))
      #print("len(self.queue): " + str(len(self.queue)))
      if self.length>2:
        self.queue[1] = self.queue[self.length-1]
        self.length-=1
        index = 1
        while(index*2<self.length):
          #print("index: " + str(index))
          if (index*2+1<self.length):
            if (self.cmpfunc(self.queue[index],self.queue[index*2+1])==1 and
                self.cmpfunc(self.queue[index*2+1],self.queue[index*2])==-1):
              self.switch(index, index*2+1)
              index = index*2+1
            elif (self.cmpfunc(self.queue[index],self.queue[index*2])==1):
              self.switch(index, index*2)
              index = index*2
            else:
              index = self.length
          elif (self.cmpfunc(self.queue[index],self.queue[index*2])==1):
            #print("index: " + str(index))
            self.switch(index, index*2)
            index = index*2
          else:
            index = self.length
      else:
        self.queue[1] = None
        self.length-=1
      return root
    return None

  def peek(self):
    if len(self.queue)>1:
      return self.queue[1]

  def tolist(self):
    list = []
    while (self.peek()!=None):
      list.append(self.pop())
    return list

  def push_all(self, list):
    for x in range(len(list)):
        self.push(list[x])

  def internal_list(self):
    list = []
    index = 1
    while (index<self.length):
        list.append(self.queue[index])
        index+=1
    return list

def main():
    p=PQueue()
    p.push_all(list('PETERBR'[::-1]))
    print(p.internal_list())
    p.pop()
    p.pop()
    print(p.internal_list())
