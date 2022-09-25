class node:
  def __init__(self,value=None):
    self.right=None
    self.left=None
    self.value=value
class bTree:
  def __init__(self,root=None):
    self.root=root
  def insert(self,value):
    if self.root==None:
      self.root=node(value)
    else:
      current=self.root
      while current.left!=current.right:
        if value<current.value and current.left!=None:
          current=current.left
        elif value>current.value and current.right!=None:
          current=current.right
        else:
          break
      if value<current.value:
        current.left=node(value)
      else:
        current.right=node(value)
  def search(self,value):
    current=self.root
    while current.left!=current.right:
      if value<current.value and current.left!=None:
        current=current.left
      elif value>current.value and current.right!=None:
        current=current.right
      else:
        break
    if value==current.value:
      return(True)
    return(False)
  def BFS(self):
    current=self.root
    lst=[]
    que=Queue()
    que.push(current)
    while len(que)>0:
      current=que.pop()
      lst.append(current.value)
      if current.left:
        que.push(current.left)
      if current.right:
        que.push(current.right)
    return(lst)
  def BFSr(self,queue,lst):
      if len(queue)==0:
        return(lst)
      current=queue.pop()
      lst.append(current.value)
      if current.left:
        queue.push(current.left)
      if current.right:
        queue.push(current.right)
      return self.BFSr(queue,lst)
  def DFS(self,option):
    if option=='in':
      return self.inOrder(self.root,[])
    elif option=='pre':
      return self.preOrder(self.root,[])
    elif option=='post':
      return self.postOrder(self.root,[])

  def preOrder(self,node,lst):
    lst.append(node.value)
    if node.left!=None:
      self.preOrder(node.left,lst)
    if node.right!=None:
      self.preOrder(node.right,lst)
    return lst

  def postOrder(self,node,lst):
    if node.left!=None:
      self.postOrder(node.left,lst)
    if node.right!=None:
      self.postOrder(node.right,lst)
    lst.append(node.value)
    return lst
  def inOrder(self,node,lst):
    if node.left:
      self.inOrder(node.left,lst)
    lst.append(node.value)
    if node.right:
      self.inOrder(node.right,lst)
    return lst
