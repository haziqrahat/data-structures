class Node:
  def __init__(self,value=None,next=None,prev=None): 
    self.next=next
    self.value=value

class Queue:
  def __init__(self,values=None):
    self.first=None
    self.last=None
    if values!=None:
      for i in values:
        self.enqueue(i)
  def enqueue(self,value):
    if self.first==None:
      self.first=self.last=Node(value)
    else:
      current=Node(value)
      self.last.next=current
      self.last=current
  def dequeue(self):
    pop='null'
    if self.first!=None:
      pop=self.first.value
      front=self.first.next
      self.first.next=None
      self.first=front
    else:
      self.last=self.first=None
      pop='null'
    return(pop)
  def peek(self):
    if self.first!=None:
      print(self.first.value)
  def __iter__(self):
    current=self.first
    while current:
      yield current
      current=current.next
  def __str__(self):
    x=[str(x.value) for x in self]
    return ' '.join(x)

