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
      print("Vertice '{}' not found on this graph.\nRemember that it is case SeNsItIvE.".format(v1))
    elif (vb2 == None):
      print("Vertice '{}' not found on this graph.\nRemember that it is case SeNsItIvE.".format(v2))
    else:
      if (vb1.name == vb2.name):
        print("Same vertices on this edge not allowed for reasons. (Simple Graph)")
        return
      elif (val < 0):
        print("Negative values for this edge not allowed.")
        return
      vl = self.checkIfEdgeAlready(v1, v2)
      if (vl == True):
        print("Edge with the specified vertices already exists.")
        return

      # if (self.isValue == True):
        # if (val == 0):
        #  print("Error creating edge: Specify the value of the edge (not zero).")
        #  return

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
      if (ex != ''):
        ex = ex+".egph"
        isy = False
        sl = ''
        sln = 0
        print("Opening {}".format(ex))
        try:
          re = open(ex, 'r')
        except:
          print("File {} not found on this disk.".format(ex))
          return
        else:
          re.close()
        with open(ex, 'r') as re:
          sln = sln + 1
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
          sln = sln + 1
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
          sln = sln + 1
          sl = re.readline()
          sl = self.removeLineBreaks(sl)
          if (sl == "VERTICES"):
            sll = ''
            while (sll != 'ENDVERTICES'):
              sln = sln + 1
              sll = re.readline()
              sll = self.removeLineBreaks(sll)
              if (sll == 'ENDVERTICES'):
                break
              elif (sll == 'EDGES' or sll == 'ENDEDGES' or sll.find('.') != -1 or sll.find(',') != -1):
                print("EGPH Syntax Error: Missing 'ENDVERTICES' to finish reading name of vertices. (Line {})".format(sln))
                return
              elif (sll == ''):
                print("EGPH Syntax Error: Vertice name cannot be empty. (Line {})".format(sln))
                return
              elif (sll != ''):
                if (self.checkIfVerticeIsGraph(sll) == None):
                  self.createNewVertice(sll)
                else:
                  print("EGPH Syntax Error: Specified vertice {} already exists. (Line {})".format(sln))
                  return
          else:
            print("EGPH Syntax Error: Must start with 'VERTICES' to read. (Line 3)")
            return
          print("VERTICES: {}".format(self.vertice))
          sln = sln + 1
          sl = re.readline()
          sl = self.removeLineBreaks(sl)
          if (sl.startswith("EDGES") == True):
            sll = ''
            while (sll != 'ENDEDGES'):
              sll = ''
              sln = sln + 1
              sll = re.readline()
              sll = self.removeLineBreaks(sll)
              if (sll == 'ENDEDGES'):
                break
              elif (sll == ''):
                print("EGPH Syntax Error: No information found, maybe End Of File or missing 'ENDEDGES'? (Line {})".format(sln))
                return
              elif (sll != ''):
                sll = sll.split(',')
                if (len(sll) == 3):
                  try:
                    int(sll[2])
                  except:
                    print("EGPH Syntax Error: The value of the edge must be integral number (int). (Line {})".format(sln))
                    return
                  else:
                    if (int(sll[2]) < 0):
                      print("EGPH Syntax Error: Negative values not allowed. (Line {})".format(sln))
                      return
                    else:
                      if (self.checkIfEdgeAlready(sll[0], sll[1]) == True):
                        print("EGPH Syntax Error: Specified edge from {} to {} already exists. (Line {})".format(sll[0], sll[1], sln))
                        return
                      self.createNewEdge(sll[0], sll[1], int(sll[2]))
                else:
                  print("EGPH Syntax Error: Must have two commas, separated with From, To, Value. (Line {})".format(sln))
                  return
          else:
            print("EGPH Syntax Error: Must start with 'EDGES' to read. (Line {})".format(sln))
            return

          print("EDGES: {}".format(self.edge))
          
        re.close()
        input("Done reading file! Press 'ENTER' to proceed...")
      else:
        print("Specify a valid file name.")
        return

    elif (str.lower(a) == 'n'):
      a = input("Do you want to create directed graphs? (Y/N) ")
      if (str.lower(a) == 'y'):
        self.isDirect = True
      elif (str.lower(a) == 'n'):
        self.isDirect = False
      else:
        print("Specify a valid input (Y or N).")
        return

      a = input("Do you want to create value of edges? (Y/N) ")
      if (str.lower(a) == 'y'):
        self.isValue = True
      elif (str.lower(a) == 'n'):
        self.isValue = False
      else:
        print("Specify a valid input (Y or N)")
        return
    else:
      print("Specify a valid input (Y or N).")
      return

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
        if (va != None and va != ''):
          self.createNewVertice(va)
        else:
          print("Specify a valid name for the vertice.")
          continue

      # B - Creating a new edge.
      elif (inp == 'b'):
        va = ''
        va = input("What is the name of a vertice sender? (Case SeNsItIvE) ")
        if (va == None or va == ''):
          print("Specify a valid name for the vertice.")
          continue
        vb = ''
        vb = input("What is the name of a vertice destination? (Case SeNsItIvE) ")
        if (vb == None or vb == ''):
          print("Specify a valid name for the vertice.")
          continue
        vc = 0
        if (self.isValue == True):
          vc = input("What is the value of the edge from vertice to vertice? ")
          try:
            int(vc)
          except:
           print("Specify a valid integral number for the edge.")
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
              print("    ({})--[{}]-->({})".format(i.fr.name, i.val, i.to.name))
            elif (self.isDirect == True and self.isValue == False):
              print("    ({})-------->({})".format(i.fr.name, i.to.name))
            elif (self.isDirect == False and self.isValue == True):
              print("    ({})--[{}]--({})".format(i.fr.name, i.val, i.to.name))
            elif (self.isDirect == False and self.isValue == False):
              print("    ({})--------({})".format(i.fr.name, i.to.name))
        else:
          print("No edges on this graph...")

      # D - Getting list of adjactives.
      elif (inp == 'd'):
        kl = False
        print("List of Adjacent Vertices\n")
        for i in self.vertices:
          kl = False
          if (self.isDirect == True):
            for j in self.edges:
              if (j.to.name == i.name):
                kl = True
                if (self.isValue == True):
                  print("({})\u2501[{}]\u2501\u252b".format(j.fr.name, j.val))
                else:
                  print("   ({})\u2501\u2501\u252b".format(j.fr.name))

          if (kl == True):
            print("        v")
          print("       ({})".format(i.name))
          for j in self.edges:
            if (j.fr.name == i.name):
              if (self.isValue == False):
                if (self.isDirect == True):
                  print("        \u2523\u2501\u2501>({})".format(j.to.name))
                else:
                  print("        \u2523\u2501\u2501({})".format(j.to.name))
              else:
                if (self.isDirect == True):
                  print("        \u2523\u2501[{}]\u2501\u2501>({})".format(j.val, j.to.name))
                else:
                  print("        \u2523\u2501[{}]\u2501\u2501({})".format(j.val, j.to.name))
            elif (self.isDirect == False and j.to.name == i.name):
              if (self.isValue == False):
                print("        \u2523\u2501\u2501({})".format(j.fr.name))
              else:
                print("        \u2523\u2501[{}]\u2501\u2501({})".format(j.val, j.fr.name))

          print('\n')

      # E - Getting value of TAMANHO e ORDEM.
      elif (inp == 'e'):
        print("ORDEM is {} (Number of vertices)\nTAMANHO is {} (Number of edges)".format(self.vertice,self.edge))
      
      # F - Checking vertice's grau
      elif (inp == 'f'):
        va = ''
        va = input('What is the vertice? ')
        if (va == ''):
          print("Specify a valid name for the vertice.")
          continue
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
          
          if (self.isDirect == False):
            print("The vertice's grau is {} (".format(len(resf)), end='')
            for i in resf:
              print(i, end=' ')
            print(")\n")
          else:
            print("The vertice's next (saida) grau is {} (".format(len(resf)), end='')
            for i in resf:
              print(i, end=' ')
            print(")\nThe vertice's previous (entrada) grau is {} (".format(len(rest)), end='')
            for i in rest:
              print(i, end=' ')
            print(")\n")
          
        else:
          print("The vertice's name you inputted is not on a graph. List vertices by typing 'B'.")
          print("Remember that it is case SeNsItIvE.")
          continue

      # G - Checking if two vertices are adjacent.
      elif (inp == 'g'):
        va = ''
        va = input("What is the vertice from? ")
        if (va == ''):
          print("Specify a valid name for the vertice.")
          continue
        va = self.checkIfVerticeIsGraph(va)
        if (va == None):
          print("The vertice's sender is not on a graph. List vertices by typing 'B'.")
          print("Remember that it is case SeNsItIvE.")
          continue

        vb = ''
        vb = input("What is the vertice to? ")
        if (vb == ''):
          print("Specify a valid name for the vertice.")
          continue
        vb = self.checkIfVerticeIsGraph(vb)
        if (vb == None):
          print("The vertice's destination is not on a graph. List vertices by typing 'B'.")
          print("Remember that it is case SeNsItIvE.")
          continue

        isadj = False
        adjv = 0

        for i in self.edges:
          if (i.fr.name == va.name and i.to.name == vb.name):
            isadj = True
            if (self.isValue == True):
              adjv = i.val
          elif (self.isDirect == False and i.fr.name == vb.name and i.to.name == va.name):
            isadj = True
            if (self.isValue == True):
              adjv = i.val

        if (isadj == False):
          print("The vertices from {} to {} are not adjacent.".format(va.name, vb.name))
        elif (isadj == True):
          if (self.isValue == True):
            print("The vertices from {} to {} are adjacent with {} costs.".format(va.name, vb.name, adjv))
          else:
            print("The vertices from {} to {} are adjacent.".format(va.name, vb.name))

      # H - Find shortest path algorithm.
      elif (inp == 'h'):
        va = ''
        va = input("What is the vertice to go through other vertices? ")
        if (va == ''):
          print("Specify a valid name for the vertice.")
          continue
        va = self.checkIfVerticeIsGraph(va)
        if (va == None):
          print("The vertice doesn't exist. List vertices by typing 'B'.")
          print("Remember that it is case SeNsItIvE.")
          continue

        vb = ''
        vb = input("What is the vertice of destination? ")
        if (vb == ''):
          print("Specify a valid name for the vertice.")
          continue
        vb = self.checkIfVerticeIsGraph(vb)
        if (vb == None):
          print("The vertice destination doesn't exist. List vertices by typing 'B'.")
          print("Remember that it is case SeNsItIvE.")
          continue

        cv = '' # Current Vertice to find adjacent vertices.
        visi = [] # Visited vertices
        qu = [] # Queue
        qun = [] # Next Queue
        quo = [] # Next vertice every run.
        ste = 1 # True if the vertice is found on the path.
        stea = [] # Array of Steps
        fou = False # True if vertice is found.
        isnex = False # True if next vertice is found.
        sdv = {} # For valued graphs to calculate.
        sdp = {} # Previous graphs.
        sev = ''

        if (self.isValue == True):
          for i in self.vertices:
            sdv[i.name] = -1 # Infinity
            sdp[i.name] = ''

        qu.append(va.name)
        if (self.isValue == True):
          sdv[va.name] = 0
          sdp[va.name] = va.name

        while (cv != vb.name):
          if (self.isValue == False):
            if (len(qu) == 0):
              if (len(qun) == 0):
                break
              else:
                qu = qun[:]
                qun = []
                ste = ste + 1

          isnex = False
          quo = []
          if (self.isValue == True):
            loo = -1
            for i, l in sdv.items():
              if (i not in visi and l != -1):
                # print(i, l)
                if (loo == -1):
                  loo = l
                  cv = i
                else:
                  if (l <= loo):
                    loo = l
                    cv = i

            if (loo == -1):
              break

          elif (self.isValue == False):
            cv = qu[0]
            qu.remove(qu[0])

          stea.append(cv)
          # print("[ cv: {} ]".format(cv))

          for i in self.edges:
            if (i.fr.name == cv):
              if (i.to.name not in visi):
                # print(i.to.name)
                if (i.to.name == vb.name):
                  # print("Found vertice {}.".format(i.to.name))
                  fou = True
                  if (self.isValue == False):
                    break
                if (self.isValue == True):
                  if (sdv[i.to.name] != -1):
                    if (sdv[i.to.name] >= (int(sdv[cv]) + int(i.val))):
                      isnex = True
                      sdv[i.to.name] = int(sdv[cv]) + int(i.val)
                      sdp[i.to.name] = cv
                  else:
                    isnex = True
                    sdv[i.to.name] = int(sdv[cv]) + int(i.val)
                    sdp[i.to.name] = cv
                elif (i.to.name not in qun and i.to.name not in qu and i.to.name not in quo):
                  isnex = True
                  qun.append(i.to.name)
                  quo.append(i.to.name)
            elif (self.isDirect == False and i.to.name == cv):
              if (i.fr.name not in visi):
                # print(i.fr.name)
                if (i.fr.name == vb.name):
                  # print("Found vertice {}.".format(i.fr.name))
                  fou = True
                  if (self.isValue == False):
                    break
                if (self.isValue == True):
                  if (sdv[i.fr.name] != -1):
                    if (sdv[i.fr.name] >= (int(sdv[cv]) + int(i.val))):
                      isnex = True
                      sdv[i.fr.name] = int(sdv[cv]) + int(i.val)
                      sdp[i.fr.name] = cv
                  else:
                    isnex = True
                    sdv[i.fr.name] = int(sdv[cv]) + int(i.val)
                    sdp[i.fr.name] = cv
                elif (i.fr.name not in qun and i.fr.name not in qu and i.fr.name not in quo):
                  isnex = True
                  qun.append(i.fr.name)
                  quo.append(i.fr.name)
            
            for i, l in sdv.items():
            #  print("{}=({},{})".format(i, l, sdp[i]), end=' ')
            # print("")
              pass
            

          if (fou == True and self.isValue == False):
            break
              
          if (self.isValue == False):
            for i in quo:
              for j in stea:
                if (j.endswith(cv) and isnex == True):
                  k = j + " -> " + i
                  stea.append(k)

          visi.append(cv)

        if (fou == True):
          if (self.isValue == False):
            print("Vertices from {} to {} calculated {} steps. See vertice steps:".format(va.name, vb.name, ste))
            for i in stea:
              if (i.endswith(cv) and i.startswith(va.name)):
                print("{} -> {}".format(i, vb.name))
          elif (self.isValue == True):
            suu = vb.name
            stt = []
            while True:
              if (sdp[suu] == va.name):
                break
              else:
                stt.append(sdp[suu])
                suu = sdp[suu]
            
            stt = stt[::-1]
            sts = "{}".format(va.name)
            for i in range(len(stt)):
              sts = sts + " -> " + stt[i]
            
            sts = sts + " -> " + vb.name
            print("Vertices from {} to {} calculated {} steps with {} costs. See vertice steps:".format(va.name, vb.name, (len(stt)+1), sdv[vb.name]))
            print(sts)
        else:
          print("Vertices from {} to {} have no edges connected between from and to.".format(va.name, vb.name))




    print("Thank you for using EfficientGraph!")

if __name__ == '__main__':
  e = EGraph()