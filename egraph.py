# EFFICIENTGRAPH
# GRAPH THEORY SYSTEM
# MADE BY FELIPE MEIRA

import os # Biblioteca para interação com o SO
from tkinter import * # Pacote de interface gráfica
from tkinter import ttk # Subpacote de widgets
from tkinter import messagebox # Subpacote de caixas de diálogo
from tkinter import simpledialog # Subpacote de caixas de diálogo com inserção

class Vertice:
  def __init__(self, name):
    self.name = name # Nomear vértice

class Edge:
  def __init__(self, fr, to, val):
    self.fr = fr # From -> DE
    self.to = to # To -> PARA
    self.val = val # Peso da aresta

class EGraph:
  isValue = False # Valorado (NÃO)
  isDirect = False # Direcionado (NÃO)

  def removeLineBreaks(self, name): # Função para normalizar
    res = name
    res = res.replace("\r", "") # Substituir o começo da linha por vazio
    res = res.replace("\n", "") # Substituir a quebra de linha por vazio
    return res

  def removeSpacesinNames(self, name): # Função que impossibilita usar espaço na nomeiação do vértice
    res = name
    if (type(name) == str):
      res = res.lstrip() 
      res = res.rstrip()
      res = res.strip()
      res = res.replace("\u0020", "") # Substitui todos os espaços em brancos por uma string vazia
      return res
    else:
      return name

  def checkIfVerticeIsGraph(self, name): # Função de verificação do vértice
    for i in self.vertices: # Em todos os vértices existentes
      if (i.name == name): # Verificar se o parâmetro passado corresponde ao vértice existente
        return i # Existe
    return None # Caso não exista

  def checkIfEdgeAlready(self, v1, v2): # Função de verificação da aresta
    for i in self.edges: # Em todos as arestas existentes
      if (i.fr.name == v1 and i.to.name == v2):
        return True # Existe uma ligação de A para B
      elif (i.fr.name == v2 and i.to.name == v1):
        return True # Existe uma ligação de B para A
    return False # Caso não exista a aresta

  def createNewVertice(self, name): # Função para criar o vértice
    ex = self.removeSpacesinNames(name)
    if (ex != name): # O input foi espaço
      return "Spaces for vertice names not allowed."
    ex = self.checkIfVerticeIsGraph(ex)
    if (ex == None): # Vértice não existe
      v = Vertice(name) # Cria o vértice com o parâmetro passado
      self.vertices.append(v) # Adiciona o vértice na lista de vértices existentes
      self.vertice = self.vertice + 1 # Incrementa o número total de vértices
      return "OK"
    else:
      return "Vertice '{}' already exists. ".format(ex) # Vértice já existe com o parâmetro que foi passado

  def createNewEdge(self, v1, v2, val): # Função para criar a aresta
    vb1 = self.checkIfVerticeIsGraph(v1)
    vb2 = self.checkIfVerticeIsGraph(v2)
    try:
      val = int(val) # Verificar se o parâmetro passado é um inteiro
    except:
      return "The value for the new edge must be numeric."
    if (vb1 == None): # Vértice A não existe
      return "Vertice '{}' not found on this graph.\nRemember that it is case SeNsItIvE.".format(v1)
    elif (vb2 == None): # Vértice B não existe
      return "Vertice '{}' not found on this graph.\nRemember that it is case SeNsItIvE.".format(v2)
    else:
      if (vb1.name == vb2.name): # Acontece um laço
        return "Same vertices on this edge not allowed for reasons. (Simple Graph)"
      elif (val < 0): # O valor da aresta não pode ser negativo
        return "Negative values for this edge not allowed."
      vl = self.checkIfEdgeAlready(v1, v2)
      if (vl == True): # Essa ligação ja existe
        return "Edge with the specified vertices already exists."

      e = Edge(vb1, vb2, val)
      self.edges.append(e) # Adiciona a aresta na lista de arestas existentes
      self.edge = self.edge + 1 # Incrementa o número total de arestas
      return "OK"

  def createNewVerticeDialog(self): # Função da caixa de diálogo da interface para a criação do vértice
    if (self.inuse == True):
      return
    self.inuse = True # Uma caixa de diálogo (execução) por vez para não causar conflito
    global guist
    va = '' # Input do usuário
    va = simpledialog.askstring(title="EfficientGraph", prompt="What is the name of a vertice? (Case SeNsItIvE)") # Caixa de diálogo para inserção
    if (va != None and va != ''):
      mm = self.createNewVertice(va)
      if (mm != "OK"): # O vértice já existe
        messagebox.showerror(title="EfficientGraph", message=mm)
      else: # O vértice foi criado com sucesso
        guist.forget() # Remove o widget da contagem anterior
        guist = Label(self.guiroot, text="ORDEM: {} TAMANHO: {}".format(self.vertice, self.edge), font="Arial", bg='#EDFFCC') # Cria um novo widget da nova contagem
        guist.pack(pady=20) # Implementa essa atualização na interface
        messagebox.showinfo(title="EfficientGraph", message="Vertice '{}' created succesfully!".format(va))
    else: # Nenhum input colocado pelo usuário
      messagebox.showerror(title="EfficientGraph", message="Specify a valid name for the vertice.")
    self.inuse = False # Para poder executar novamente

  def createNewEdgeDialog(self): # Função da caixa de diálogo da interface para a criação da aresta
    if (self.inuse == True):
      return
    self.inuse = True # Uma caixa de diálogo (execução) por vez para não causar conflito
    global guist
    va = '' # Input do vétice A do usuário
    va = simpledialog.askstring(title="EfficientGraph", prompt="What is the name of a vertice sender? (Case SeNsItIvE)") # Caixa de diálogo para inserção (FROM)
    if (va == None or va == ''): # Nenhum input colocado pelo usuário
      messagebox.showerror(title="EfficientGraph", message="Specify a valid name for the vertice.")
      self.inuse = False # Para poder executar novamente
      return
    va = self.checkIfVerticeIsGraph(va)
    if (va == None): # O vétice A não existe
      messagebox.showerror(title="EfficientGraph", message="The vertice's name you inputted is not on a graph. Try listing vertices.\nRemember that it is case SeNsItIvE.")
      self.inuse = False # Para poder executar novamente
      return
    vb = '' # Input do vétice B do usuário
    vb = simpledialog.askstring(title="EfficientGraph", prompt="What is the name of a vertice destination? (Case SeNsItIvE)") # Caixa de diálogo para inserção (TO)
    if (vb == None or vb == ''): # Nenhum input colocado pelo usuário
      messagebox.showerror(title="EfficientGraph", message="Specify a valid name for the vertice.")
      self.inuse = False # Para poder executar novamente
      return
    vb = self.checkIfVerticeIsGraph(vb)
    if (vb == None): # O vétice B não existe
      messagebox.showerror(title="EfficientGraph", message="The vertice's name you inputted is not on a graph. Try listing vertices.\nRemember that it is case SeNsItIvE.")
      self.inuse = False # Para poder executar novamente
      return
    vc = 0 # Inicializa o peso com zero
    if (self.isValue == True): # Caso sera valorado
      vc = simpledialog.askstring(title="EfficientGraph", prompt="What is the value of the edge from vertice to vertice?") # Caixa de diálogo para inserção do peso
      try:
        int(vc) # Verificar se o parâmetro passado é um inteiro
      except:
        messagebox.showerror(title="EfficientGraph", message="Specify a valid value.")
        self.inuse = False # Para poder executar novamente
        return
    mm = self.createNewEdge(va.name, vb.name, vc)
    if (mm != "OK"): # A ligação já existe
      messagebox.showerror(title="EfficientGraph", message=mm)
    else: # A aresta foi criada com sucesso
      guist.forget() # Remove o widget da contagem anterior
      guist = Label(self.guiroot, text="ORDEM: {} TAMANHO: {}".format(self.vertice, self.edge), font="Arial", bg='#EDFFCC') # Cria um novo widget da nova contagem
      guist.pack(pady=20) # Implementa essa atualização na interface
      messagebox.showinfo(title="EfficientGraph", message="Edge from '{}' to '{}' created succesfully!".format(va.name, vb.name))
    self.inuse = False # Para poder executar novamente

  def listVerticesEdges(self): # Função para listar os vértices e as arestas existentes
    if (self.inuse == True): # Caso tenha algum diálogo aberto de outra função
      return # Encerra a função atual
    self.inuse = True # Sinaliza que está função está em execução (uma caixa de diálogo por vez para não causar conflito)
    global top
    top = Toplevel() # Aparecerá uma nova janela acima da principal
    top.title("List of Adjacent Vertices")
    frm = ttk.Frame(top, padding=10)
    frm.grid()
    aa = "{} VERTICES\n".format(self.vertice) # Número (quantidade) existente de vértices
    if (self.vertice > 0): # Existe algum vértice
      for i in self.vertices:
        aa = aa + "({})\n".format(i.name) # Lista o nome de cada vértice
    else: # Nenhum vértice existe
      aa = aa + "No vertices on this graph..."
    Label(top, text=aa, font=("Monospace", 12)).grid(column=0, row=0)
    aa = "{} EDGES\n".format(self.edge) # Número existente de arestas
    if (self.edge > 0): # Existe algum aresta
      for i in self.edges: # Lista o nome de cada vértice em sua perpectiva formatação
        if (self.isDirect == True and self.isValue == True): # É direcionado e valorado
          aa = aa + "({})--[{}]-->({})\n".format(i.fr.name, i.val, i.to.name)
        elif (self.isDirect == True and self.isValue == False): # É direcionado e não é valorado
          aa = aa + "({})-------->({})\n".format(i.fr.name, i.to.name)
        elif (self.isDirect == False and self.isValue == True): # Não é direcionado e valorado
          aa = aa + "({})--[{}]--({})\n".format(i.fr.name, i.val, i.to.name)
        elif (self.isDirect == False and self.isValue == False): # Não é direcionado e não é valorado
          aa = aa + "({})--------({})\n".format(i.fr.name, i.to.name)
    else: # Nenhum aresta existe
      aa = aa + "No edges on this graph..."
    Label(top, text=aa, font=("Monospace", 12)).grid(column=2, row=0)
    Button(top, text="OK", font="Arial", command=lambda: self.closeListDialog()).grid(column=1, row=1) # Fecha o pop-up e o estado de inuse fica falso

  def listVerticeAdjactives(self): # Função para listar os vértices adjacentes
    if (self.inuse == True): # Caso tenha algum diálogo aberto de outra função
      return # Encerra a função atual
    global top
    self.inuse = True # Sinaliza que está função está em execução (uma caixa de diálogo por vez para não causar conflito)
    kl = False # Indicar que há uma conexão entre o vértice atual a um vértice adjacente
    co = 0 # Coluna de exibição e organização
    ro = 0 # Linha de exibição e organização
    aa = '' # Lista dos vértices adjacentes
    if (self.vertice == 0): # Nenhum vértice existe
      messagebox.showerror(title="EfficientGraph", message="No vertices on your graph. Try adding it!")
      return
    top = Toplevel() # Aparecerá uma nova janela acima da principal
    top.title("List of Adjacent Vertices")
    frm = ttk.Frame(top, padding=10)
    frm.grid()
    for i in self.vertices: # Verifica em cada vértice existente
      aa = '\n'
      kl = False
      if (self.isDirect == True): # É direcionado
        for j in self.edges: # Verifica em cada aresta existente
          if (j.to.name == i.name): # Se o vértice atual é o extremo de destino
            kl = True
            if (self.isValue == True): # É valorado
              aa = aa + "({})\u2501[{}]\u2501\u252b         \n".format(j.fr.name, j.val) # Nome do vértice adjacente com peso
            else: # Não é valorado
              aa = aa + "   ({})\u2501\u2501\u252b         \n".format(j.fr.name) # Nome do vértice adjacente
      if (kl == True):
        aa = aa + "       v        \n" # Vértice adjacente de entrada
      aa = aa + "      ({})       \n".format(i.name) # Nome do vértice atual
      for j in self.edges: # Verifica em cada aresta existente
        if (j.fr.name == i.name): # Se o vértice atual é o extremo de origem
          if (self.isValue == False): # Não é valorado
            if (self.isDirect == True): # É direcionado
              aa = aa + "       \u2523\u2501\u2501>({})\n".format(j.to.name) # Nome do vértice adjacente
            else: # Não é direcionado
              aa = aa + "     \u2523\u2501\u2501({})\n".format(j.to.name) # Nome do vértice adjacente
          else: # É valorado
            if (self.isDirect == True): # É direcionado
              aa = aa + "         \u2523\u2501[{}]\u2501\u2501>({})\n".format(j.val, j.to.name) # Nome do vértice adjacente com peso
            else: # Não é direcionado
              aa = aa + "        \u2523\u2501[{}]\u2501\u2501({})\n".format(j.val, j.to.name) # Nome do vértice adjacente com peso
        elif (self.isDirect == False and j.to.name == i.name): # Não é direcionado e o vértice atual é o extremo de destino
          if (self.isValue == False): # Não é valorado
            aa = aa + "     \u2523\u2501\u2501({})\n".format(j.fr.name) # Nome do vértice adjacente
          else: # É valorado
            aa = aa + "        \u2523\u2501[{}]\u2501\u2501({})\n".format(j.val, j.fr.name) # Nome do vértice adjacente com peso
      Label(top, text=aa, font=("Monospace", 10)).grid(column=co, row=ro)
      co = co + 1 # Vai para a próxima coluna na exibição da interface gráfica
      if (co >= 5):
        co = 0 # Reseta a posição da coluna na exibição da interface gráfica
        ro = ro + 1 # Incrementa mais uma linha na exibição da interface gráfica

    ro = ro + 1 # Incrementa mais uma linha na exibição da interface gráfica
    if ((ro-1) > 0): # Caso tenha mais que 4 vértices
      co = 2 # Botão é exibido no meio
    else:  # Caso tenha menos que 4 vértices
      co = 0 # Botão é exibido no começo
    Button(top, text="OK", font="Arial", command=lambda: self.closeListDialog()).grid(column=co, row=ro) # Fecha o pop-up e o estado de inuse fica falso
    
  def checkVerticeGrau(self): # Função para identificar o grau do vértice
    if (self.inuse == True): # Caso tenha algum diálogo aberto de outra função
      return # Encerra a função atual
    self.inuse = True # Sinaliza que está função está em execução (uma caixa de diálogo por vez para não causar conflito)
    va = '' # Input do vétice pelo usuário
    va = simpledialog.askstring(title="EfficientGraph", prompt="What is the name of a vertice sender? (Case SeNsItIvE)") # Caixa de diálogo para inserção (FROM)
    if (va == None or va == ''): # Nenhum input colocado pelo usuário
      messagebox.showerror(title="EfficientGraph", message="Specify a valid name for the vertice.")
      self.inuse = False # Para poder executar novamente
      return # Encerra a função atual
    va = self.checkIfVerticeIsGraph(va)
    resf = [] # Lista dos vértices quando o vértice escolhido atua como saída
    rest = [] # Lista dos vértices quando o vértice escolhido atua como entrada
    if (va != None):
      for i in self.edges: # Verifica em cada aresta existente
        if (self.isDirect == False): # Não é direcionado
          if (i.fr.name == va.name): # Se o vértice escolhido é o extremo de origem
            resf.append(i.to.name) # Adiciona o vértice de destino na lista "resf"
          elif (i.to.name == va.name): # Se o vértice escolhido é o extremo de destino
            resf.append(i.fr.name) # Adiciona o vértice de origem na lista "resf"
        elif (self.isDirect == True): # É direcionado
          if (i.fr.name == va.name): # Se o vértice escolhido é o extremo de origem
            resf.append(i.to.name) # Adiciona o vértice de destino na lista "resf"
          elif (i.to.name == va.name): # Se o vértice escolhido é o extremo de destino
            rest.append(i.fr.name) # Adiciona o vértice de origem na lista "rest"
      aa = '' # Número (quantidade) existente do grau do vértice
      if (self.isDirect == False): # Não é direcionado
        aa = "The vertice's grau is {} (".format(len(resf))
        for i in resf: # Para cada vértice armazenado
          aa = aa + str(i) + " " # Printar
        aa = aa + ")"
      else: # É direcionado
        aa = "The vertice's next (saida) grau is {} (".format(len(resf))
        for i in resf: # Para cada vértice armazenado
          aa = aa + str(i) + " " # Printar
        aa = aa + ")\nThe vertice's previous (entrada) grau is {} (".format(len(rest))
        for i in rest: # Para cada vértice armazenado
          aa = aa + str(i) + " " # Printar
        aa = aa + ")"
      messagebox.showinfo(title="EfficientGraph", message=aa) # Exibição da caixa de diálogo com a mensagem
    else:
      messagebox.showerror(title="EfficientGraph", message="The vertice's name you inputted is not on a graph. Try listing vertices.\nRemember that it is case SeNsItIvE.")
    self.inuse = False # Para poder executar novamente

  def checkOrdemTamanho(self): # Função para identificar a ordem e o tamanho do grafo
    if (self.inuse == True): # Caso tenha algum diálogo aberto de outra função
      return # Encerra a função atual
    self.inuse = True # Sinaliza que está função está em execução (uma caixa de diálogo por vez para não causar conflito)
    messagebox.showinfo(title="EfficientGraph", message="ORDEM is {} (Number of vertices)\nTAMANHO is {} (Number of edges)".format(self.vertice,self.edge)) # Exibição da caixa de diálogo com o número da ordem e tamanho
    self.inuse = False # Para poder executar novamente

  def checkIfVerticesAreAdjacent(self): # Função para verificar se dois vértices são adjacentes entre si
    if (self.inuse == True): # Caso tenha algum diálogo aberto de outra função
      return # Encerra a função atual
    self.inuse = True # Sinaliza que está função está em execução (uma caixa de diálogo por vez para não causar conflito)
    va = '' # Input do vétice A pelo usuário
    va = simpledialog.askstring(title="EfficientGraph", prompt="What is the name of a vertice from? (Case SeNsItIvE)") # Caixa de diálogo para inserção (FROM)
    if (va == None or va == ''): # Nenhum input colocado pelo usuário para o vértice A
      messagebox.showerror(title="EfficientGraph", message="Specify a valid name for the vertice.")
      self.inuse = False # Para poder executar novamente
      return # Encerra a função atual
    va = self.checkIfVerticeIsGraph(va)
    if (va == None): # O vétice A não existe
      messagebox.showerror(title="EfficientGraph", message="The vertice's name you inputted is not on a graph. Try listing vertices.\nRemember that it is case SeNsItIvE.")
      self.inuse = False # Para poder executar novamente
      return # Encerra a função atual
    vb = '' # Input do vétice B pelo usuário
    vb = simpledialog.askstring(title="EfficientGraph", prompt="What is the name of a vertice to? (Case SeNsItIvE)") # Caixa de diálogo para inserção (TO)
    if (vb == None or vb == ''): # Nenhum input colocado pelo usuário para o vértice B
      messagebox.showerror(title="EfficientGraph", message="Specify a valid name for the vertice.")
      self.inuse = False # Para poder executar novamente
      return # Encerra a função atual
    vb = self.checkIfVerticeIsGraph(vb)
    if (vb == None): # O vétice B não existe
      messagebox.showerror(title="EfficientGraph", message="The vertice's name you inputted is not on a graph. Try listing vertices.\nRemember that it is case SeNsItIvE.")
      self.inuse = False # Para poder executar novamente
      return # Encerra a função atual
    if (va.name == vb.name): # Mesmo vértice (laço)
      messagebox.showerror(title="EfficientGraph", message="You inputted the same vertices and is invalid. Try using different vertices.")
      self.inuse = False # Para poder executar novamente
      return # Encerra a função atual
    isadj = False # A conexão é ou não adjacente
    adjv = 0 # Peso da conexão
    for i in self.edges: # Verifica em cada aresta existente
      if (i.fr.name == va.name and i.to.name == vb.name): # Se o vértice A é o extremo de origem e o vértice B é o extremo de destino
        isadj = True
        if (self.isValue == True): # É valorado
          adjv = i.val # Pega o peso dessa ligação
      elif (self.isDirect == False and i.fr.name == vb.name and i.to.name == va.name): # Não é direcionado, se o vértice B é o extremo de origem e o vértice A é o extremo de destino
        isadj = True
        if (self.isValue == True): # É valorado
          adjv = i.val # Pega o peso dessa ligação
    aa = ''
    if (isadj == False): # Não é adjacente
      aa = "The vertices from {} to {} are not adjacent.".format(va.name, vb.name)
    elif (isadj == True): # É adjacente
      if (self.isValue == True): # É valorado
        aa = "The vertices from {} to {} are adjacent with {} costs.".format(va.name, vb.name, adjv)
      else: # Não é valorado
        aa = "The vertices from {} to {} are adjacent.".format(va.name, vb.name)
    messagebox.showinfo(title="EfficientGraph", message=aa) # Exibição da caixa de diálogo com a mensagem
    self.inuse = False # Para poder executar novamente

  def findShortestAlgorithm(self): # Função para achar o caminho mais curto entre dois vértices
    if (self.inuse == True): # Caso tenha algum diálogo aberto de outra função
      return # Encerra a função atual
    self.inuse = True # Sinaliza que está função está em execução (uma caixa de diálogo por vez para não causar conflito)
    global top
    va = '' # Input do vétice A pelo usuário
    va = simpledialog.askstring(title="EfficientGraph", prompt="What is the vertice to go through other vertices?") # Caixa de diálogo para inserção (FROM)
    if (va == None or va == ''): # Nenhum input colocado pelo usuário para o vértice A
      messagebox.showerror(title="EfficientGraph", message="Specify a valid name for the vertice.")
      self.inuse = False # Para poder executar novamente
      return # Encerra a função atual
    va = self.checkIfVerticeIsGraph(va)
    if (va == None): # O vétice A não existe
      messagebox.showerror(title="EfficientGraph", message="The vertice's name you inputted is not on a graph. Try listing vertices.\nRemember that it is case SeNsItIvE.")
      self.inuse = False # Para poder executar novamente
      return # Encerra a função atual
    vb = '' # Input do vétice B pelo usuário
    vb = simpledialog.askstring(title="EfficientGraph", prompt="What is the vertice of destination?") # Caixa de diálogo para inserção (TO)
    if (vb == None or vb == ''): # Nenhum input colocado pelo usuário para o vértice B
      messagebox.showerror(title="EfficientGraph", message="Specify a valid name for the vertice.")
      self.inuse = False # Para poder executar novamente
      return # Encerra a função atual
    vb = self.checkIfVerticeIsGraph(vb)
    if (vb == None): # O vétice B não existe
      messagebox.showerror(title="EfficientGraph", message="The vertice's name you inputted is not on a graph. Try listing vertices.\nRemember that it is case SeNsItIvE.")
      self.inuse = False # Para poder executar novamente
      return # Encerra a função atual
    if (va.name == vb.name): # Mesmo vértice (laço)
      messagebox.showerror(title="EfficientGraph", message="You inputted the same vertices and is invalid. Try using different vertices.")
      self.inuse = False # Para poder executar novamente
      return # Encerra a função atual

    cv = '' # Current Vertice to find adjacent vertices. | Vértice atual em busca dos seus adjacentes
    visi = [] # Lista dos vértices visitados
    qu = [] # Fila
    qun = [] # Próxima fila
    quo = [] # Next vertice every run. | Lista dos vétices para cada execução
    ste = 1 # True if the vertice is found on the path. | Se um vértice foi encontrado no caminho
    stea = [] # Array of Steps | Lista de etapas do caminho
    fou = False # True if vertice is found. | Se o vértice foi encontrado
    isnex = False # True if next vertice is found. | Se o próximo vértice foi encontrado
    sdv = {} # For valued graphs to calculate. |
    sdp = {} # Previous graphs. | Dicionário dos grafos anteriores
    sev = '' # NÃO UTILIZADO

    if (self.isValue == True): # É valorado
      for i in self.vertices: # Em todos os vértices existentes
        sdv[i.name] = -1 # Cada vértices definido com valor infinito
        sdp[i.name] = ''

    qu.append(va.name) # Adiciona o vértice de partida na fila
    if (self.isValue == True): # É valorado
      sdv[va.name] = 0 # Define o vértice de partida como 0
      sdp[va.name] = va.name # Nome do vértice de partida

    while (cv != vb.name): # Enquando o vértice atual for diferente do vértice de chegada
      if (self.isValue == False): # Não é valorado
        if (len(qu) == 0): # Comprimento da fila é 0
          if (len(qun) == 0): # Comprimento da próxima fila é 0
            break # Para
          else:
            qu = qun[:] # Cria uma copia
            qun = [] # Limpa
            ste = ste + 1 # Incrementa nos passos

      isnex = False # Próximo vértice não encontrado
      quo = [] # Limpa
      if (self.isValue == True): # É valorado
        loo = -1
        for i, l in sdv.items(): # Para cada valor de cada vértice
          if (i not in visi and l != -1): # O vértice atual não está na lista dos vértices visitados e seu valor é diferente de infinito
            if (loo == -1):
              loo = l # Atualiza com o valor
              cv = i # Atualiza o vértice atual
            else:
              if (l <= loo):
                loo = l
                cv = i
        if (loo == -1):
          break # Pare
      elif (self.isValue == False): # Não é valorado
        cv = qu[0] # O vértice atual é o primeiro da fila
        qu.remove(qu[0]) # Remove o primeiro elemento da fila

      stea.append(cv) # Adiciona o vértice nas etapas
      for i in self.edges: # Verifica em cada aresta existente
        if (i.fr.name == cv): # O vértice de origem é igual ao vértice atual
          if (i.to.name not in visi): # O vértice de destino não está na lista dos vértices visitados
            if (i.to.name == vb.name): # O vértice de destino é igual ao vértice de chegada
              fou = True # Vértice encontrado
              if (self.isValue == False): # Não é valorado
                break # Para
            if (self.isValue == True): # É valorado
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

  def closeListDialog(self): # Função para fechar a caixa de diálogo
    global top
    top.destroy() # Destroi a janela atual que foi criada
    self.inuse = False # Para poder executar novamente

  def importGraph(self, exa): # Função para importar um grafo no sistema
    ex = exa+".egph" # Nome do arquivo no formato .egph
    isy = False # NÃO UTILIZADO
    sl = '' # String do arquivo
    sln = 0 # Posição da linha (usado para indicar em qual linha está o erro)
    try:
      re = open(ex, 'r') # Abre para ler o arquivo
    except:
      return "File {} not found on this disk.".format(ex) # Arquivo não foi encontrado
    else:
      re.close() # Fecha o arquivo
    with open(ex, 'r') as re: # Abre para ler o arquivo linha por linha
      sln = sln + 1 # Primeira linha
      sl = re.readline() # Lê a linha
      if (sl.startswith("DIRECTED") == True): # Começa com a palavra "DIRECTED"
        sll = sl.split('=')[1] # Acessa a segunda parte da string que fica a direita de "="
        sll = self.removeLineBreaks(sll) # Remove a quebra de linha e armazena a palavra
        if (sll != None): # Tem algo armazenado
          if (sll == 'True'):
            self.isDirect = True # É direcionado
          elif (sll == 'False'):
            self.isDirect = False # Não é direcionado
          else: # Mal formatado devido a não ser nem "True" ou "False"
            return "EGPH Syntax Error: The valid values are 'True' or 'False'. (Line 1)"
        else: # Mal formatado devido estar vazio
          return "EGPH Syntax Error: The valid values are 'True' or 'False'. (Line 1)"
      else: # Mal formatado devido a não começar com "DIRECTED"
        return "EGPH Syntax Error: Must start with 'DIRECTED' to read. (Line 1)"
      sln = sln + 1 # Segunda linha
      sl = re.readline() # Lê a linha
      if (sl.startswith("VALUED") == True): # Começa com a palavra "VALUED"
        sll = sl.split('=')[1] # Acessa a segunda parte da string que fica a direita de "="
        sll = self.removeLineBreaks(sll) # Remove a quebra de linha e armazena a palavra
        if (sll != None): # Tem algo armazenado
          if (sll == 'True'):
            self.isValue = True # É valorado
          elif (sll == 'False'):
            self.isValue = False # Não é valorado
          else: # Mal formatado devido a não ser nem "True" ou "False"
            return "EGPH Syntax Error: The valid values are 'True' or 'False'. (Line 2)"
        else: # Mal formatado devido estar vazio
          return "EGPH Syntax Error: The valid values are 'True' or 'False'. (Line 2)"
      else: # Mal formatado devido a não começar com "VALUED"
        return "EGPH Syntax Error: Must start with 'VALUED' to read. (Line 2)"
      sln = sln + 1 # Terceira linha
      sl = re.readline() # Lê a linha
      sl = self.removeLineBreaks(sl) # Remove a quebra de linha e armazena a palavra
      if (sl == "VERTICES"): # A palavra é "VERTICES"
        sll = ''
        while (sll != 'ENDVERTICES'):
          sln = sln + 1 # Quarta linha até chegar a linha com "ENDVERTICES"
          sll = re.readline() # Lê a linha
          sll = self.removeLineBreaks(sll) # Remove a quebra de linha e armazena a palavra
          if (sll == 'ENDVERTICES'):
            break # Para
          elif (sll == 'EDGES' or sll == 'ENDEDGES' or sll.find('.') != -1 or sll.find(',') != -1):
            return "EGPH Syntax Error: Missing 'ENDVERTICES' to finish reading name of vertices. (Line {})".format(sln)
          elif (sll == ''): # Mal formatado devido estar vazio o campo de vértices
            return "EGPH Syntax Error: Vertice name cannot be empty. (Line {})".format(sln)
          elif (sll != ''):
            if (self.checkIfVerticeIsGraph(sll) == None): # Vértice não existe
              mm = self.createNewVertice(sll) # Cria vértice
              if (mm != "OK"): # O vértice já existe
                return mm + " (Line {})".format(sln) # Indica em qual linha está o erro
            else: # O vértice já existe
              return "EGPH Syntax Error: Specified vertice {} already exists. (Line {})".format(sll, sln)
      else: # Mal formatado devido a não ter a palavra "VERTICES"
        return "EGPH Syntax Error: Must start with 'VERTICES' to read. (Line 3)"
      sln = sln + 1 # Vai para a proxima linha
      sl = re.readline() # Lê a linha
      sl = self.removeLineBreaks(sl) # Remove a quebra de linha e armazena a palavra
      if (sl.startswith("EDGES") == True): # Começa com a palavra "EDGES"
        sll = ''
        while (sll != 'ENDEDGES'):
          sll = ''
          sln = sln + 1 # Incrementa a posição da linha
          sll = re.readline() # Lê a linha
          sll = self.removeLineBreaks(sll) # Remove a quebra de linha e armazena a palavra
          if (sll == 'ENDEDGES'):
            break # Para
          elif (sll == ''): # Mal formatado devido estar vazio o campo de arestas
            return "EGPH Syntax Error: No information found, maybe End Of File or missing 'ENDEDGES'? (Line {})".format(sln)
          elif (sll != ''):
            sll = sll.split(',') # Separa em três substrings devido a ","
            if (len(sll) == 3):
              try:
                int(sll[2]) # Verificar se a terceira substring é um inteiro
              except: # Mal formatado devido estar o peso não ser um inteiro
                return "EGPH Syntax Error: The value of the edge must be integral number (int). (Line {})".format(sln)
              else:
                if (int(sll[2]) < 0): # Se a terceira substring é negativa
                  return "EGPH Syntax Error: Negative values not allowed. (Line {})".format(sln)
                else: # Se a terceira substring é positiva
                  if (self.checkIfEdgeAlready(sll[0], sll[1]) == True): # A aresta já existe
                    return "EGPH Syntax Error: Specified edge from {} to {} already exists. (Line {})".format(sll[0], sll[1], sln)
                  mm = self.createNewEdge(sll[0], sll[1], int(sll[2])) # Cria a aresta
                  if (mm != "OK"): # Erro na criação da aresta
                    return mm + " (Line {})".format(sln) # Indica em qual linha está o erro
            else: # # Mal formatado devido a não ter o vértice de origem e destino, além do peso dessa ligação
              return "EGPH Syntax Error: Must have two commas, separated with From, To, Value. (Line {})".format(sln)
      else: # Mal formatado devido a não começar com "EDGES"
        return "EGPH Syntax Error: Must start with 'EDGES' to read. (Line {})".format(sln)

    re.close() # Fecha o arquivo
    return "OK"

  def __init__(self): # Função incial e o menu do sistema
    self.inuse = False # Para poder executar novamente
    self.vertices = list() # Cria uma ista vazia para preencher com vértices
    self.edges = list() # Cria uma ista vazia para preencher com arestas
    self.vertice = 0
    self.edge = 0
    os.system('clear') # Limpa a tela do terminal
    self.guiroot = Tk() # Cria a janela principal da interface gráfica
    self.guiroot.title("EfficientGraph") # Define o título da janela
    global guist
    a = messagebox.askyesno(title="EfficientGraph", message="Welcome! Do you want to import existing graphs?") # Cria uma caixa de diálogo com um botão "sim" e outro "não"
    if (a == 1): # Clicou no botão "sim"
      ex = simpledialog.askstring(title='EfficientGraph', prompt='What is the file name (x.egph)?') # Cria uma janela de diálogo com um campo de inserção de texto
      if (ex != '' and ex != None):
        mm = self.importGraph(ex)
        if (mm != "OK"): # Erro na importação do grafo
          messagebox.showerror(title="EfficientGraph", message=mm)
          self.guiroot.destroy() # Destroi a janela atual que foi criada
          return # Encerra
      else: # Nenhum input colocado pelo usuário
        messagebox.showerror(title="EfficientGraph", message="Specify a valid file name.")
        self.guiroot.destroy() # Destroi a janela atual que foi criada
        return # Encerra
    elif (a == 0): # Clicou no botão "não"
      a = messagebox.askyesno(title="EfficientGraph", message="Do you want to create directed graphs?") # Cria uma caixa de diálogo com um botão "sim" e outro "não"
      if (a == 1): # Clicou no botão "sim"
        self.isDirect = True # É direcionado
      elif (a == 0): # Clicou no botão "não"
        self.isDirect = False # Não é direcionado
      else: # NÃO UTILIZADO NA PRÁTICA
        messagebox.showerror(title="EfficientGraph", message="Specify a valid input (Yes or No).")
        self.guiroot.destroy() # Destroi a janela atual que foi criada
        return # Encerra
      a = messagebox.askyesno(title="EfficientGraph", message="Do you want to create value of edges?") # Cria uma caixa de diálogo com um botão "sim" e outro "não"
      if (a == 1): # Clicou no botão "sim"
        self.isValue = True # É valorado
      elif (a == 0): # Clicou no botão "não"
        self.isValue = False # Não é valorado
      else: # NÃO UTILIZADO NA PRÁTICA
        messagebox.showerror(title="EfficientGraph", message="Specify a valid input (Yes or No).")
        self.guiroot.destroy() # Destroi a janela atual que foi criada
        return # Encerra
    else: # NÃO UTILIZADO NA PRÁTICA
      messagebox.showerror(title="EfficientGraph", message="Specify a valid input (Yes or No).")
      self.guiroot.destroy() # Destroi a janela atual que foi criada
      return # Encerra

    # Interface gráfica do menu principal
    self.guiroot.geometry("400x380") # Tamanho da janela
    self.guiroot.configure(bg='#EDFFCC') # Cor da janela
    Label(self.guiroot, text='Be welcome!', font=('Arial', 32, 'bold'), bg='#EDFFCC', fg='#3B5704').pack(pady=10)
    Button(self.guiroot, text='Create new Vertice', font='Arial', command=self.createNewVerticeDialog, bg='#90C2B3', fg='#495052', border=1).pack(pady=1)
    Button(self.guiroot, text='Create new Edge', font='Arial', command=self.createNewEdgeDialog, bg='#90C2B3', fg='#495052', border=1).pack(pady=1)
    Button(self.guiroot, text='List Vertices and Edges', font='Arial', command=self.listVerticesEdges, bg='#90C2B3', fg='#495052', border=1).pack(pady=1)
    Button(self.guiroot, text='View list of Adjacentives of Vertices', font='Arial', command=self.listVerticeAdjactives, bg='#90C2B3', fg='#495052', border=1).pack(pady=1)
    Button(self.guiroot, text='Get information about Ordem and Tamanho', font='Arial', command=self.checkOrdemTamanho, bg='#90C2B3', fg='#495052', border=1).pack(pady=1)
    Button(self.guiroot, text="Check Vertice's Grau", font='Arial', command=self.checkVerticeGrau, bg='#90C2B3', fg='#495052', border=1).pack(pady=1)
    Button(self.guiroot, text='Check if Vertices are Adjacent', font='Arial', command=self.checkIfVerticesAreAdjacent, bg='#90C2B3', fg='#495052', border=1).pack(pady=1)
    Button(self.guiroot, text='Find Shortest Vertices', font='Arial', command=self.findShortestAlgorithm, bg='#90C2B3', fg='#495052', border=1).pack(pady=1)
    Button(self.guiroot, text='Quit Program', font='Arial', command=self.guiroot.destroy, bg='#90C2B3', fg='#81B622', border=1).pack(pady=1)
    guist = Label(self.guiroot, text="ORDEM: {} TAMANHO: {}".format(self.vertice, self.edge), font='Arial', bg='#EDFFCC')
    guist.pack(pady=20) # Espaçamento

    self.guiroot.mainloop() # Mantem o menu principal para realizar ações

    print("Thank you for using EfficientGraph!")

if __name__ == '__main__': # Executado diretamente
  e = EGraph() # Cria o objeto