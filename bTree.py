class bTree:
  def __init__(self,root=None):
    self.root=root
  def insert(self,value):
    print(value)
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
