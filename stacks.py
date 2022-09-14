class Node:
  def __init__(self,value=None,next=None,prev=None): 
    self.next=next
    self.prev=prev
    self.value=value

class Stack:
  def __init__(self,values=None):
    self.bottom=None
    self.top=None
    if values!=None:
      for i in values:
        self.push(i)
  def push(self,value):
    if self.bottom==None:
      self.bottom=self.top=Node(value)
    else:
      current=Node(value)
      current.next=self.top
      self.top=current
  def pop(self):
    pop='null'
    if self.top!=None:
      pop=self.top.value
      back=self.top.next
      self.top.next=None
      self.top=back
    else:
      self.top=self.bottom=None
      pop='null'
    return(pop)
  def peek(self):
    print(self.top.value)
  def __iter__(self):
    current=self.top
    while current:
      yield current
      current=current.next
  def __str__(self):
    x=[str(x.value) for x in self]
    for i in x:
      print(str(i))
    return ''

