class graph:
  def __init__(self):
    self.nodes=0
    self.adList={}
  def addVertex(self,vertex):
    if self.adList.get(vertex)==None:
      self.adList[vertex]=[]
      self.nodes+=1
    else:
      return('Node does not exit')
  def addEdge(self,node1,node2):
    if self.adList.get(node1)!=None and self.adList.get(node2)!=None:
      self.adList[node1].append(node2)
      self.adList[node2].append(node1)
    else:
      return('Node does not exit')
  def __str__(self):
    for i in self.adList:
      print(i,'-->',self.adList[i])
    return('')
