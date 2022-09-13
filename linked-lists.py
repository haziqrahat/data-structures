class node:
  def __init__(self,data):
    self.data=data
    self.next=None
class linkedList:
  def __init__(self,values=None):
    self.head=None
    self.tail=None
    if values!=None:
      for x in values:
        self.append(x)
  def append(self,value):
    if self.head==None:
      self.head=self.tail=node(value)
    else:
      self.tail.next=node(value)
      self.tail=self.tail.next
  def __str__(self):
    return '->'.join([str(x) for x in self])
  def __iter__(self):
    current=self.head
    while current:
      yield current
      current=current.next
  def __len__(self):
    cnt=0
    current=self.head
    while current:
      cnt+=1
      current=current.next
    return(cnt)
  def insert(self,loc,value):
    if loc!=0:
      cnt=0
      current=self.head
      while cnt<loc-1:
        current=current.next
        cnt+=1
      newNode=node(value)
      newNode.next=current.next
      current.next=newNode
    else:
      newNode=node(value)
      newNode.next=self.head
      self.head=newNode
  def delete(self,loc):
    if loc!=0:
      cnt=0
      current=self.head
      while cnt<loc-1:
        current=current.next
        cnt+=1
      tmp=current.next.next
      current.next.next=None
      current.next=tmp
    else:
      temp=self.head.next
      self.head.next=None
      self.head=temp
  def reverse(self):
    prev=None
    current=self.head
    next=current.next
    while current:
      current.next=prev
      prev=current
      current=next
      if next:
        next=next.next
    tmp=self.head
    self.head=self.tail
    self.tail=tmp
