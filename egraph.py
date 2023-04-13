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

  def removeLineBreaks(self, name):
    res = name
    res = res.replace("\r", "")
    res = res.replace("\n", "")
    return res

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

    os.system('clear')

    print("Welcome to EfficientGraph!")
    a = input("Do you want to import existing graphs? (Y/N to create new) ")
    if (str.lower(a) == 'y'):
      ex = input("What is the name of this file (x.egph)? ")
      if (ex != None):
        ex = ex+".egph"
        isy = False
        sl = ''
        print("Opening {}".format(ex))
        with open(ex, 'r') as re:
          sl = re.readline()
          if (sl.startswith("DIRECTED") == True):
            sll = sl.split('=')[1]
            sll = self.removeLineBreaks(sll)
            if (sll != None):
              if (sll == 'True'):
                self.isDirect = True
              elif (sll == 'False'):
                self.isDirect = False
              else:
                print("EGPH Syntax Error: The valid values are 'True' or 'False'. (Line 1)")
                return
            else:
              print("EGPH Syntax Error: The valid values are 'True' or 'False'. (Line 1)")
              return
          else:
            print("EGPH Syntax Error: Must start with 'DIRECTED' to read. (Line 1)")
            return

          print("Directed = {}".format(self.isDirect))
          
          sl = re.readline()
          if (sl.startswith("VALUED") == True):
            sll = sl.split('=')[1]
            sll = self.removeLineBreaks(sll)
            if (sll != None):
              if (sll == 'True'):
                self.isValue = True
              elif (sll == 'False'):
                self.isValue = False
              else:
                print("EGPH Syntax Error: The valid values are 'True' or 'False'. (Line 2)")
                return
            else:
              print("EGPH Syntax Error: The valid values are 'True' or 'False'. (Line 2)")
              return
          else:
            print("EGPH Syntax Error: Must start with 'VALUED' to read. (Line 2)")
            return

          print("Value = {}".format(self.isValue))

          sl = re.readline()
          sl = self.removeLineBreaks(sl)
          if (sl == "VERTICES"):
            sll = ''
            while (sll != 'ENDVERTICES'):
              sll = re.readline()
              sll = self.removeLineBreaks(sll)
              if (sll == 'ENDVERTICES'):
                break
              elif (sll != ''):
                self.createNewVertice(sll)
          else:
            print("EGPH Syntax Error: Must start with 'VERTICES' to read. (Line 3)")
            return

          print("VERTICES: {}".format(self.vertice))
          
          sl = re.readline()
          sl = self.removeLineBreaks(sl)
          if (sl.startswith("EDGES") == True):
            sll = ''
            while (sll != 'ENDEDGES'):
              sll = ''
              sll = re.readline()
              sll = self.removeLineBreaks(sll)
              if (sll == 'ENDEDGES'):
                break
              elif (sll != ''):
                sll = sll.split(',')
                if (sll[0] != None and sll[1] != None and sll[2] != None):
                  self.createNewEdge(sll[0], sll[1], sll[2])
                else:
                  print("EGPH Syntax Error: Must have two commas, separated with From, To, Value.")
          else:
            print("EGPH Syntax Error: Must start with 'EDGES' to read. (Line 4)")
            return

          print("EDGES: {}".format(self.vertice))
          
        re.close()

        input("Done reading file! Press 'ENTER' to proceed...")

    else:
      a = input("Do you want to create directed graphs? (Y/N) ")
      if (str.lower(a) == 'y'):
        self.isDirect = True

      a = input("Do you want to create value of edges? (Y/N) ")
      if (str.lower(a) == 'y'):
        self.isValue = True

    os.system('clear')

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

      # C - Listing vertices and edges.
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

      # E - Getting value of TAMANHO e ORDEM.
      elif (inp == 'e'):
        print("ORDEM is {} (Number of vertices)\nTAMANHO is {} (Number of edges)".format(self.vertice,self.edge))
      
      # F - Checking vertice's grau
      elif (inp == 'f'):
        va = ''
        va = input('What is the vertice?')
        va = self.checkIfVerticeIsGraph(va)
        resf = []
        rest = []
        if (va != None):
          for i in self.edges:
            if (self.isDirect == False):
              if (i.fr.name == va.name):
                resf.append(i.to.name)
              elif (i.to.name == va.name):
                resf.append(i.fr.name)
            elif (self.isDirect == True):
              if (i.fr.name == va.name):
                resf.append(i.to.name)
              elif (i.to.name == va.name):
                rest.append(i.fr.name)
          
          if (resf[0] != None):
            if (self.isDirect == False):
              print("The vertice's grau is: ", end='')
              for i in resf:
                print(i, end=' ')
            else:
              print("The vertice's previous (entrada) grau is: ", end='')
              for i in resf:
                print(i, end=' ')
              print("\nThe vertice's next (saida) grau is: ", end='')
              for i in rest:
                print(i, end=' ')
            print('\n')
          
        else:
          print("The vertice's name you inputted is not on a graph. List vertices by typing 'B'.")
          continue

      # G - Checking if two vertices are adjacent.
      elif (inp == 'g'):
        va = ''
        va = input("What is the vertice from? ")
        va = self.checkIfVerticeIsGraph(va)
        if (va == None):
          print("The vertice from is not on a graph. List vertices by typing 'B'.")
          continue
        
        vb = ''
        vb = input("What is the vertice to? ")
        vb = self.checkIfVerticeIsGraph(vb)
        if (vb == None):
          print("The vertice to is not on a graph. List vertices by typing 'B'.")
          continue

        isadj = False

        for i in self.edges:
          if (i.fr.name == va.name and i.to.name == vb.name):
            isadj = True
          elif (i.fr.name == vb.name and i.to.name == va.name):
            if (self.isDirect == False):
              isadj = True

        if (isadj == False):
          print("The vertices from {} to {} are not adjacent.".format(va.name, vb.name))
        elif (isadj == True):
          print("The vertices from {} to {} are adjacent.".format(va.name, vb.name))




    print("Thank you for using EfficientGraph!")

if __name__ == '__main__':
  e = EGraph()