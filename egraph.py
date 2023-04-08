import os

class Vertice:
  def __init__(self, name):
    self.name = name
    print("Created new vertice name '{}'".format(name))

class Edge:
  def __init__(self, fr, to, val):
    self.fr = fr
    self.to = to
    self.val = val
    print("Created new edge between {} to {} with value {}"
      .format(fr.name, to.name, val))

class EGraph:
  isValue = False
  isDirect = False

  def checkIfVerticeIsGraph(self, name):
    for i in self.vertices:
      if (i.name == name):
        return i

    return None

  def checkIfEdgeAlready(self, v1, v2):
    for i in self.edges:
      if (i.fr.name == v1 and i.to.name == v2):
        return True
      elif (i.fr.name == v2 and i.to.name == v1):
        return True
      
    return False

  def createNewVertice(self, name):
    ex = self.checkIfVerticeIsGraph(name)
    if (ex == None):
      v = Vertice(name)
      self.vertices.append(v)
      self.vertice = self.vertice + 1
    else:
      print("Vertice '{}' already exists. ".format(name))
    
  def createNewEdge(self, v1, v2, val):
    vb1 = self.checkIfVerticeIsGraph(v1)
    vb2 = self.checkIfVerticeIsGraph(v2)
    if (vb1 == None):
      print("Vertice '{}' not found on this graph.".format(v1))
    elif (vb2 == None):
      print("Vertice '{}' not found on this graph.".format(v2))
    else:
      vl = self.checkIfEdgeAlready(v1, v2)
      if (vl == True):
        print("Error creating edge: Edge with the specified vertice already exists.")
        return
        
      if (self.isValue == True):
        if (val == 0):
          print("Error creating edge: Specify the value of the edge (not zero).")
          return

      e = Edge(vb1, vb2, val)
      self.edges.append(e)
      self.edge = self.edge + 1

  def __init__(self):
    self.vertices = list()
    self.edges = list()
    self.vertice = 0
    self.edge = 0

    print("Welcome to EfficientGraph!")
    a = input("Do you want to import existing graphs? (Y/N to create new) ")
    if (str.lower(a) == 'y'):
      ex = input("Paste your strings following import graph syntax. >")
      if (ex != None):
        # TODO Import string to graph.
        pass
    
    a = input("Do you want to create directed graphs? (Y/N) ")
    if (str.lower(a) == 'y'):
      self.isDirect = True

    a = input("Do you want to create value of edges? (Y/N) ")
    if (str.lower(a) == 'y'):
      self.isValue = True

    inp = ''
    while (inp != 'quit' and inp != 'q'):
      print("\n================= EFFICIENTGRAPH =================")
      print("(A) Create new vertice.")
      print("(B) Create new edge.")
      print("(C) List vertices and edges.")
      print("(D) View list of adjacentives of vertices.")
      print("(E) Get information about 'ORDEM' e 'TAMANHO'.")
      print("(F) Get the 'grau' of vertice.")
      print("(G) Check whatever two vertices are adjacent.")
      print("(H) Find shortest path from vertice to vertice.")
      print("(Q/QUIT) Finish program.")
      print("\nORDEM: {} TAMANHO: {}".format(self.vertice, self.edge))
      print("==================================================")
      inp = input('Input > ')
      inp = str.lower(inp)
      os.system('clear')

      # Input Methods
      # A - Creating a new graph.
      if (inp == 'a'):
        va = ''
        va = input("What is the name of a vertice? (Case SeNsItIvE) ")
        if (va != None):
          self.createNewVertice(va)
        else:
          print("Specify a valid name for the vertice.")

      # B - Creating a new edge.
      elif (inp == 'b'):
        va = ''
        va = input("What is the name of a vertice sender? (Case SeNsItIvE) ")
        if (va == None):
          print("Specify a valid name for the vertice.")
          continue

        vb = ''
        vb = input("What is the name of a vertice destination? (Case SeNsItIvE) ")
        if (vb == None):
          print("Specify a valid name for the vertice.")
          continue

        vc = 0
        if (self.isValue == True):
          vc = int(input("What is the value of the edge from vertice to vertice? "))
          if (type(vc) != type(int)):
            print("Specify a valid number for the edge.")
            continue

        self.createNewEdge(va, vb, vc)

      elif (inp == 'c'):
        print("{} VERTICES".format(self.vertice))
        if (self.vertice > 0):
          for i in self.vertices:
            print("    ({})".format(i.name), end=' ')
        else:
          print("No vertices on this graph...")

        print("\n\n{} EDGES".format(self.edge))
        if (self.edge > 0):
          for i in self.edges:
            if (self.isDirect == True and self.isValue == True):
              print("    ({})--[{}]-->({})".format(i.fr.name, i.to.name, i.val))
            elif (self.isDirect == True and self.isValue == False):
              print("    ({})-------->({})".format(i.fr.name, i.to.name))
            elif (self.isDirect == False and self.isValue == True):
              print("    ({})--[{}]--({})".format(i.fr.name, i.to.name, i.val))
            elif (self.isDirect == False and self.isValue == False):
              print("    ({})--------({})".format(i.fr.name, i.to.name))
        else:
          print("No edges on this graph...")


    print("Thank you for using EfficientGraph!")

if __name__ == '__main__':
  e = EGraph()