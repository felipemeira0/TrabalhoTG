# EFFICIENTGRAPH
# GRAPH THEORY SYSTEM
# MADE BY FELIPE MEIRA

import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

class Vertice:
  def __init__(self, name):
    self.name = name

class Edge:
  def __init__(self, fr, to, val):
    self.fr = fr
    self.to = to
    self.val = val

class EGraph:
  isValue = False
  isDirect = False

  def removeLineBreaks(self, name):
    res = name
    res = res.replace("\r", "")
    res = res.replace("\n", "")
    return res

  def removeSpacesinNames(self, name):
    res = name
    if (type(name) == str):
      res = res.lstrip()
      res = res.rstrip()
      res = res.strip()
      res = res.replace("\u0020", "")
      return res
    else:
      return name

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
    ex = self.removeSpacesinNames(name)
    if (ex != name):
      return "Spaces for vertice names not allowed."
    ex = self.checkIfVerticeIsGraph(ex)
    if (ex == None):
      v = Vertice(name)
      self.vertices.append(v)
      self.vertice = self.vertice + 1
      return "OK"
    else:
      return "Vertice '{}' already exists. ".format(ex)

  def createNewEdge(self, v1, v2, val):
    vb1 = self.checkIfVerticeIsGraph(v1)
    vb2 = self.checkIfVerticeIsGraph(v2)
    try:
      val = int(val)
    except:
      return "The value for the new edge must be numeric."
    if (vb1 == None):
      return "Vertice '{}' not found on this graph.\nRemember that it is case SeNsItIvE.".format(v1)
    elif (vb2 == None):
      return "Vertice '{}' not found on this graph.\nRemember that it is case SeNsItIvE.".format(v2)
    else:
      if (vb1.name == vb2.name):
        return "Same vertices on this edge not allowed for reasons. (Simple Graph)"
      elif (val < 0):
        return "Negative values for this edge not allowed."
      vl = self.checkIfEdgeAlready(v1, v2)
      if (vl == True):
        return "Edge with the specified vertices already exists."

      e = Edge(vb1, vb2, val)
      self.edges.append(e)
      self.edge = self.edge + 1
      return "OK"

  def createNewVerticeDialog(self):
    if (self.inuse == True):
      return
    self.inuse = True
    global guist
    va = ''
    va = simpledialog.askstring(title="EfficientGraph", prompt="What is the name of a vertice? (Case SeNsItIvE)")
    if (va != None and va != ''):
      mm = self.createNewVertice(va)
      if (mm != "OK"):
        messagebox.showerror(title="EfficientGraph", message=mm)
      else:
        guist.forget()
        guist = Label(self.guiroot, text="ORDEM: {} TAMANHO: {}".format(self.vertice, self.edge), font="Arial")
        guist.pack()
        messagebox.showinfo(title="EfficientGraph", message="Vertice '{}' created succesfully!".format(va))
    else:
      messagebox.showerror(title="EfficientGraph", message="Specify a valid name for the vertice.")
    self.inuse = False

  def createNewEdgeDialog(self):
    if (self.inuse == True):
      return
    self.inuse = True
    global guist
    va = ''
    va = simpledialog.askstring(title="EfficientGraph", prompt="What is the name of a vertice sender? (Case SeNsItIvE)")
    if (va == None or va == ''):
      messagebox.showerror(title="EfficientGraph", message="Specify a valid name for the vertice.")
      self.inuse = False
      return
    va = self.checkIfVerticeIsGraph(va)
    if (va == None):
      messagebox.showerror(title="EfficientGraph", message="The vertice's name you inputted is not on a graph. Try listing vertices.\nRemember that it is case SeNsItIvE.")
      self.inuse = False
      return
    vb = ''
    vb = simpledialog.askstring(title="EfficientGraph", prompt="What is the name of a vertice destination? (Case SeNsItIvE)")
    if (vb == None or vb == ''):
      messagebox.showerror(title="EfficientGraph", message="Specify a valid name for the vertice.")
      self.inuse = False
      return
    vb = self.checkIfVerticeIsGraph(vb)
    if (vb == None):
      messagebox.showerror(title="EfficientGraph", message="The vertice's name you inputted is not on a graph. Try listing vertices.\nRemember that it is case SeNsItIvE.")
      self.inuse = False
      return
    vc = 0
    if (self.isValue == True):
      vc = simpledialog.askstring(title="EfficientGraph", prompt="What is the value of the edge from vertice to vertice?")
      try:
        int(vc)
      except:
        messagebox.showerror(title="EfficientGraph", message="Specify a valid numeric value.")
        self.inuse = False
        return
    mm = self.createNewEdge(va.name, vb.name, vc)
    if (mm != "OK"):
      messagebox.showerror(title="EfficientGraph", message=mm)
    else:
      guist.forget()
      guist = Label(self.guiroot, text="ORDEM: {} TAMANHO: {}".format(self.vertice, self.edge), font="Arial")
      guist.pack()
      messagebox.showinfo(title="EfficientGraph", message="Edge from '{}' to '{}' created succesfully!".format(va.name, vb.name))
    self.inuse = False

  def listVerticesEdges(self):
    if (self.inuse == True):
      return
    self.inuse = True
    global top
    top = Toplevel()
    top.title("List of Adjacent Vertices")
    frm = ttk.Frame(top, padding=10)
    frm.grid()
    aa = "{} VERTICES\n".format(self.vertice)
    if (self.vertice > 0):
      for i in self.vertices:
        aa = aa + "({})\n".format(i.name)
    else:
      aa = aa + "No vertices on this graph..."
    Label(top, text=aa, font=("Monospace", 12)).grid(column=0, row=0)
    aa = "{} EDGES\n".format(self.edge)
    if (self.edge > 0):
      for i in self.edges:
        if (self.isDirect == True and self.isValue == True):
          aa = aa + "({})--[{}]-->({})\n".format(i.fr.name, i.val, i.to.name)
        elif (self.isDirect == True and self.isValue == False):
          aa = aa + "({})-------->({})\n".format(i.fr.name, i.to.name)
        elif (self.isDirect == False and self.isValue == True):
          aa = aa + "({})--[{}]--({})\n".format(i.fr.name, i.val, i.to.name)
        elif (self.isDirect == False and self.isValue == False):
          aa = aa + "({})--------({})\n".format(i.fr.name, i.to.name)
    else:
      aa = aa + "No edges on this graph..."
    Label(top, text=aa, font=("Monospace", 12)).grid(column=2, row=0)
    Button(top, text="OK", font="Arial", command=lambda: self.closeListDialog()).grid(column=1, row=1)

  def listVerticeAdjactives(self):
    if (self.inuse == True):
      return
    global top
    self.inuse = True
    kl = False
    co = 0
    ro = 0
    aa = ''
    if (self.vertice == 0):
      messagebox.showerror(title="EfficientGraph", message="No vertices on your graph. Try adding it!")
      return
    top = Toplevel()
    top.title("List of Adjacent Vertices")
    frm = ttk.Frame(top, padding=10)
    frm.grid()
    for i in self.vertices:
      aa = '\n'
      kl = False
      if (self.isDirect == True):
        for j in self.edges:
          if (j.to.name == i.name):
            kl = True
            if (self.isValue == True):
              aa = aa + "({})\u2501[{}]\u2501\u252b         \n".format(j.fr.name, j.val)
            else:
              aa = aa + "   ({})\u2501\u2501\u252b         \n".format(j.fr.name)
      if (kl == True):
        aa = aa + "       v        \n"
      aa = aa + "      ({})       \n".format(i.name)
      for j in self.edges:
        if (j.fr.name == i.name):
          if (self.isValue == False):
            if (self.isDirect == True):
              aa = aa + "       \u2523\u2501\u2501>({})\n".format(j.to.name)
            else:
              aa = aa + "     \u2523\u2501\u2501({})\n".format(j.to.name)
          else:
            if (self.isDirect == True):
              aa = aa + "         \u2523\u2501[{}]\u2501\u2501>({})\n".format(j.val, j.to.name)
            else:
              aa = aa + "        \u2523\u2501[{}]\u2501\u2501({})\n".format(j.val, j.to.name)
        elif (self.isDirect == False and j.to.name == i.name):
          if (self.isValue == False):
            aa = aa + "     \u2523\u2501\u2501({})\n".format(j.fr.name)
          else:
            aa = aa + "        \u2523\u2501[{}]\u2501\u2501({})\n".format(j.val, j.fr.name)
      Label(top, text=aa, font=("Monospace", 10)).grid(column=co, row=ro)
      co = co + 1
      if (co >= 5):
        co = 0
        ro = ro + 1

    ro = ro + 1
    if ((ro-1) > 0):
      co = 2
    else:
      co = 0
    Button(top, text="OK", font="Arial", command=lambda: self.closeListDialog()).grid(column=co, row=ro)
    
  def checkVerticeGrau(self):
    if (self.inuse == True):
      return
    self.inuse = True
    va = ''
    va = simpledialog.askstring(title="EfficientGraph", prompt="What is the name of a vertice sender? (Case SeNsItIvE)")
    if (va == None or va == ''):
      messagebox.showerror(title="EfficientGraph", message="Specify a valid name for the vertice.")
      self.inuse = False
      return
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
      aa = ''
      if (self.isDirect == False):
        aa = "The vertice's grau is {} (".format(len(resf))
        for i in resf:
          aa = aa + str(i) + " "
        aa = aa + ")"
      else:
        aa = "The vertice's next (saida) grau is {} (".format(len(resf))
        for i in resf:
          aa = aa + str(i) + " "
        aa = aa + ")\nThe vertice's previous (entrada) grau is {} (".format(len(rest))
        for i in rest:
          aa = aa + str(i) + " "
        aa = aa + ")"
      messagebox.showinfo(title="EfficientGraph", message=aa)
    else:
      messagebox.showerror(title="EfficientGraph", message="The vertice's name you inputted is not on a graph. Try listing vertices.\nRemember that it is case SeNsItIvE.")
    self.inuse = False

  def checkOrdemTamanho(self):
    if (self.inuse == True):
      return
    self.inuse = True
    messagebox.showinfo(title="EfficientGraph", message="ORDEM is {} (Number of vertices)\nTAMANHO is {} (Number of edges)".format(self.vertice,self.edge))
    self.inuse = False

  def checkIfVerticesAreAdjacent(self):
    if (self.inuse == True):
      return
    self.inuse = True
    va = ''
    va = simpledialog.askstring(title="EfficientGraph", prompt="What is the name of a vertice from? (Case SeNsItIvE)")
    if (va == None or va == ''):
      messagebox.showerror(title="EfficientGraph", message="Specify a valid name for the vertice.")
      self.inuse = False
      return
    va = self.checkIfVerticeIsGraph(va)
    if (va == None):
      messagebox.showerror(title="EfficientGraph", message="The vertice's name you inputted is not on a graph. Try listing vertices.\nRemember that it is case SeNsItIvE.")
      self.inuse = False
      return
    vb = ''
    vb = simpledialog.askstring(title="EfficientGraph", prompt="What is the name of a vertice to? (Case SeNsItIvE)")
    if (vb == None or vb == ''):
      messagebox.showerror(title="EfficientGraph", message="Specify a valid name for the vertice.")
      self.inuse = False
      return
    vb = self.checkIfVerticeIsGraph(vb)
    if (vb == None):
      messagebox.showerror(title="EfficientGraph", message="The vertice's name you inputted is not on a graph. Try listing vertices.\nRemember that it is case SeNsItIvE.")
      self.inuse = False
      return
    if (va.name == vb.name):
      messagebox.showerror(title="EfficientGraph", message="You inputted the same vertices and is invalid. Try using different vertices.")
      self.inuse = False
      return
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
    aa = ''
    if (isadj == False):
      aa = "The vertices from {} to {} are not adjacent.".format(va.name, vb.name)
    elif (isadj == True):
      if (self.isValue == True):
        aa = "The vertices from {} to {} are adjacent with {} costs.".format(va.name, vb.name, adjv)
      else:
        aa = "The vertices from {} to {} are adjacent.".format(va.name, vb.name)
    messagebox.showinfo(title="EfficientGraph", message=aa)
    self.inuse = False

  def findShortestAlgorithm(self):
    if (self.inuse == True):
      return
    self.inuse = True
    global top
    va = ''
    va = simpledialog.askstring(title="EfficientGraph", prompt="What is the vertice to go through other vertices?")
    if (va == None or va == ''):
      messagebox.showerror(title="EfficientGraph", message="Specify a valid name for the vertice.")
      self.inuse = False
      return
    va = self.checkIfVerticeIsGraph(va)
    if (va == None):
      messagebox.showerror(title="EfficientGraph", message="The vertice's name you inputted is not on a graph. Try listing vertices.\nRemember that it is case SeNsItIvE.")
      self.inuse = False
      return
    vb = ''
    vb = simpledialog.askstring(title="EfficientGraph", prompt="What is the vertice of destination?")
    if (vb == None or vb == ''):
      messagebox.showerror(title="EfficientGraph", message="Specify a valid name for the vertice.")
      self.inuse = False
      return
    vb = self.checkIfVerticeIsGraph(vb)
    if (vb == None):
      messagebox.showerror(title="EfficientGraph", message="The vertice's name you inputted is not on a graph. Try listing vertices.\nRemember that it is case SeNsItIvE.")
      self.inuse = False
      return
    if (va.name == vb.name):
      messagebox.showerror(title="EfficientGraph", message="You inputted the same vertices and is invalid. Try using different vertices.")
      self.inuse = False
      return

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
      for i in self.edges:
        if (i.fr.name == cv):
          if (i.to.name not in visi):
            if (i.to.name == vb.name):
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
            if (i.fr.name == vb.name):
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
      aa = ''
      top = Toplevel()
      top.title("EfficientGraph")
      frm = ttk.Frame(top, padding=10)
      frm.grid()
      if (self.isValue == False):
        Label(top, text="Vertices from {} to {} calculated {} steps. See vertice steps:".format(va.name, vb.name, ste), font="Arial").grid(column=0, row=0)
        for i in stea:
          if (i.endswith(cv) and i.startswith(va.name)):
            aa = aa + "{} -> {}".format(i, vb.name)
        Label(top, text=aa, font="Monospace").grid(column=0, row=1)
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
        Label(top, text="Vertices from {} to {} calculated {} steps with {} costs. See vertice steps:".format(va.name, vb.name, (len(stt)+1), sdv[vb.name]), font="Arial").grid(column=0, row=0)
        Label(top, text=sts, font="Monospace").grid(column=0, row=1)
      Button(top, text="OK", font="Arial", command=lambda: self.closeListDialog()).grid(column=0, row=2)
    else:
      messagebox.showinfo(title="EfficientGraph", message="Vertices from {} to {} have no edges connected between from and to.".format(va.name, vb.name))
      self.inuse = False

  def closeListDialog(self):
    global top
    top.destroy()
    self.inuse = False

  def importGraph(self, exa):
    ex = exa+".egph"
    isy = False
    sl = ''
    sln = 0
    try:
      re = open(ex, 'r')
    except:
      return "File {} not found on this disk.".format(ex)
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
            return "EGPH Syntax Error: The valid values are 'True' or 'False'. (Line 1)"
        else:
          return "EGPH Syntax Error: The valid values are 'True' or 'False'. (Line 1)"
      else:
        return "EGPH Syntax Error: Must start with 'DIRECTED' to read. (Line 1)"
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
            return "EGPH Syntax Error: The valid values are 'True' or 'False'. (Line 2)"
        else:
          return "EGPH Syntax Error: The valid values are 'True' or 'False'. (Line 2)"
      else:
        return "EGPH Syntax Error: Must start with 'VALUED' to read. (Line 2)"
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
            return "EGPH Syntax Error: Missing 'ENDVERTICES' to finish reading name of vertices. (Line {})".format(sln)
          elif (sll == ''):
            return "EGPH Syntax Error: Vertice name cannot be empty. (Line {})".format(sln)
          elif (sll != ''):
            if (self.checkIfVerticeIsGraph(sll) == None):
              mm = self.createNewVertice(sll)
              if (mm != "OK"):
                return mm + " (Line {})".format(sln)
            else:
              return "EGPH Syntax Error: Specified vertice {} already exists. (Line {})".format(sll, sln)
      else:
        return "EGPH Syntax Error: Must start with 'VERTICES' to read. (Line 3)"
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
            return "EGPH Syntax Error: No information found, maybe End Of File or missing 'ENDEDGES'? (Line {})".format(sln)
          elif (sll != ''):
            sll = sll.split(',')
            if (len(sll) == 3):
              try:
                int(sll[2])
              except:
                return "EGPH Syntax Error: The value of the edge must be integral number (int). (Line {})".format(sln)
              else:
                if (int(sll[2]) < 0):
                  return "EGPH Syntax Error: Negative values not allowed. (Line {})".format(sln)
                else:
                  if (self.checkIfEdgeAlready(sll[0], sll[1]) == True):
                    return "EGPH Syntax Error: Specified edge from {} to {} already exists. (Line {})".format(sll[0], sll[1], sln)
                  mm = self.createNewEdge(sll[0], sll[1], int(sll[2]))
                  if (mm != "OK"):
                    return mm + " (Line {})".format(sln)
            else:
              return "EGPH Syntax Error: Must have two commas, separated with From, To, Value. (Line {})".format(sln)
      else:
        return "EGPH Syntax Error: Must start with 'EDGES' to read. (Line {})".format(sln)

    re.close()
    return "OK"

  def __init__(self):
    self.inuse = False
    self.vertices = list()
    self.edges = list()
    self.vertice = 0
    self.edge = 0
    os.system('clear')
    self.guiroot = Tk()
    self.guiroot.title("EfficientGraph")
    global guist
    a = messagebox.askyesno(title="EfficientGraph", message="Welcome! Do you want to import existing graphs?")
    if (a == 1):
      ex = simpledialog.askstring(title='EfficientGraph', prompt='What is the file name (x.egph)?')
      if (ex != '' and ex != None):
        mm = self.importGraph(ex)
        if (mm != "OK"):
          messagebox.showerror(title="EfficientGraph", message=mm)
          self.guiroot.destroy()
          return
      else:
        messagebox.showerror(title="EfficientGraph", message="Specify a valid file name.")
        self.guiroot.destroy()
        return
    elif (a == 0):
      a = messagebox.askyesno(title="EfficientGraph", message="Do you want to create directed graphs?")
      if (a == 1):
        self.isDirect = True
      elif (a == 0):
        self.isDirect = False
      else:
        messagebox.showerror(title="EfficientGraph", message="Specify a valid input (Yes or No).")
        self.guiroot.destroy()
        return
      a = messagebox.askyesno(title="EfficientGraph", message="Do you want to create value of edges?")
      if (a == 1):
        self.isValue = True
      elif (a == 0):
        self.isValue = False
      else:
        messagebox.showerror(title="EfficientGraph", message="Specify a valid input (Yes or No).")
        self.guiroot.destroy()
        return
    else:
      messagebox.showerror(title="EfficientGraph", message="Specify a valid input (Yes or No).")
      self.guiroot.destroy()
      return

    # Gui Init
    Label(self.guiroot, text='EfficientGraph', font=('Arial', 32)).pack()
    Button(self.guiroot, text='Create new Vertice', font='Arial', command=self.createNewVerticeDialog).pack()
    Button(self.guiroot, text='Create new Edge', font='Arial', command=self.createNewEdgeDialog).pack()
    Button(self.guiroot, text='List Vertices and Edges', font='Arial', command=self.listVerticesEdges).pack()
    Button(self.guiroot, text='View list of Adjacentives of Vertices', font='Arial', command=self.listVerticeAdjactives).pack()
    Button(self.guiroot, text='Get information about Ordem and Tamanho', font='Arial', command=self.checkOrdemTamanho).pack()
    Button(self.guiroot, text="Check Vertice's Grau", font='Arial', command=self.checkVerticeGrau).pack()
    Button(self.guiroot, text='Check if Vertices are Adjacent', font='Arial', command=self.checkIfVerticesAreAdjacent).pack()
    Button(self.guiroot, text='Find Shortest Vertices', font='Arial', command=self.findShortestAlgorithm).pack()
    Button(self.guiroot, text='Quit Program', font='Arial', command=self.guiroot.destroy).pack()
    guist = Label(self.guiroot, text="ORDEM: {} TAMANHO: {}".format(self.vertice, self.edge), font='Arial')
    guist.pack()

    self.guiroot.mainloop()

    print("Thank you for using EfficientGraph!")

if __name__ == '__main__':
  e = EGraph()