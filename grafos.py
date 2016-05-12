import copy
import random
class grafos:
    
    #dictionary where the key is the name of the vertex and the value is the value of the vertex
    global vertice
    
    #dictionary where the key is the vertex and the value is another dictionary where they key is the name of the vertex
    # and the value is the value of the edge
    global arestas
    
    def __init__(self):
        
        self.vertice = {}
        self.arestas = {}
    
    #method that adds a vertex in the graph
    def adicionarVertice(self,chave,valor=0):
        
        self.vertice[chave] = valor
        
        self.arestas[chave] = {}
        
    #method that removes a vertex from the graph
    def removerVertice(self,chave):
        
        #check if this vertex really exists
        if(self.vertice.has_key(chave)):
            
            #if so, deletes it
            del self.vertice[chave]
            
            #check if this edge really exists
            if(self.arestas.has_key(chave)):
                
                #copy the edges of this vertex
                copiaArestas = copy.copy(self.arestas[chave])
                
                #delete every edge
                for i in copiaArestas:
                    self.removerAresta(chave,i)
        
    #method that connects two vertex creating an edge
    def adicionarAresta(self,vertice1,vertice2,valor=0):
        
        if (self.vertice.has_key(vertice1) and self.vertice.has_key(vertice2)):
        
            self.arestas[vertice1][vertice2] = valor
            self.arestas[vertice2][vertice1] = valor
            return True
        
        else:
            return False
               
    #method that removes the connection between  two vertex, ie, deletes an edge
    def removerAresta(self,vertice1,vertice2):
        
        if(self.arestas.has_key(vertice1)):
            
            if(self.arestas[vertice1].has_key(vertice2)):
               
               del self.arestas[vertice1][vertice2]
        
        if(self.arestas.has_key(vertice2)):
            
            if(self.arestas[vertice2].has_key(vertice1)):
                
                del self.arestas[vertice2][vertice1]
          
    #method that returns the vertex dictionary
    def retornarVertices(self):
        return self.vertice
    
    #method that returns the edges dictionary
    def retornarArestas(self,vertice):
        
        if(self.arestas.has_key(vertice)):
            return self.arestas[vertice]
        else:
            return False
    
    #method that returns the range of the graph
    def ordem(self):
        return len(self.vertice)
    
    #method that returns a random vertex
    def verticeAleatorio(self):
        return random.choice(self.vertice.keys())
    
    #method that returns every adjacent vertex of a specific vertex
    def adjacentes(self, chave):
        
        if(self.arestas.has_key(chave)):
            return self.arestas[chave]
    
    #method that returns the lenght of a specific vertex
    def grau(self,chave):
        if(self.arestas.has_key(chave)):
            return len(self.arestas[chave])
        return False
        
    #depth-first search
    def buscaEmProfundidade(self,origem,destino,visitados=[],caminho=[]):
        
        caminho.append(origem)
        
        visitados.append(origem)
        
        if (origem==destino):
            return True
        else:
            
            #return the adjacent vertex of the source, to know where you can go
            adjacentes = self.arestas.get(origem)
            
            #for each adjacent vertex, verify if it reaches the destiny
            for adj in adjacentes.keys():
                
                #check if this vertex wasn't visited yet
                if(visitados.count(adj)==0):
                    
                    #check if it reaches the destiny
                    if (self.buscaEmProfundidade(adj,destino,visitados,caminho)):
                        return caminho
                    
                    #it means it is not possible to reach the destiny, removes it from the path
                    caminho.remove(adj)
                
    #method used for the depth search to find the shortest path
    def selecionarMenorCaminho(self,caminhos):
        
        if caminhos!={}:
            
            chave = min(caminhos.keys())
            
            return caminhos[chave]
        else:
            return None
    
    def verticesSozinhos(self):
        cont=0
        for i in self.vertice.keys():
            if self.arestas[i] == {}:
                cont+=1
        return cont
    
    def buscaMenorCaminho(self, origem, destino, visitados = None ,caminho = None, valor = 0, todosCaminhos = None):
        if caminho is None:
            caminho = []
        if visitados is None:
            visitados = []
        if todosCaminhos is None:
            todosCaminhos = {}
        
        caminho.append(origem)
                
        visitados.append(origem)
        
        if (origem==destino):
            todosCaminhos[valor] = copy.copy(caminho) 
            valor = 0
            
        #check if every vertex was already visited
        if (len(visitados)<len(self.vertice) - self.verticesSozinhos() ):
            
            #get the adjacent vertex of the source, to check where you can go
            adjacentes = self.arestas.get(origem)

            if adjacentes is not None:
            
                #verify if this vertex reaches the destiny
                for adj in adjacentes.keys():

                    if(visitados.count(adj)==0 or adj==destino):

                        valor += self.arestas[origem][adj]

                        if (self.buscaMenorCaminho(adj,destino,visitados,caminho,valor,todosCaminhos)):
                            return self.selecionarMenorCaminho(todosCaminhos) 
                        else:
                            caminho.remove(adj)
           
        #if every vertex was already visited
        else:
            return True 
    
            
    
    #method that searches for the shortest path from a vertex to another taking in account the edges' values
    def buscaEmProfundidadeMenorCaminho(self, origem, destino, visitados = None ,caminho = None, valor = 0, todosCaminhos = None):

        if caminho is None:
            caminho = []
        if visitados is None:
            visitados = []
        if todosCaminhos is None:
            todosCaminhos = {}
        
        caminho.append(origem)
                
        visitados.append(origem)
        
        if (origem==destino):
            
            todosCaminhos[valor] = copy.copy(caminho) 
            valor = 0

            origem = caminho[0]
            
            del caminho[:]

            visitados.remove(origem)
            
            return self.buscaEmProfundidadeMenorCaminho(origem,destino,visitados,caminho,valor,todosCaminhos)  
        
        #verify if every vertex was visited
        if (len(visitados)<=len(self.vertice) - self.verticesSozinhos() ):
            
            adjacentes = self.arestas.get(origem)

            if adjacentes is not None:
            
                for adj in adjacentes.keys():
                   
                    #check if this vertex wasn't already visited
                    if(visitados.count(adj)==0 or adj==destino):

                        #increase the value of this vertex in the total value
                        valor += self.arestas[origem][adj]

                        #check this vertex
                        return self.buscaEmProfundidadeMenorCaminho(adj,destino,visitados,caminho,valor,todosCaminhos) 
            
            return self.selecionarMenorCaminho(todosCaminhos) 
            return self.buscaEmProfundidadeMenorCaminho(caminho[0],destino,visitados,caminho,valor,todosCaminhos) 
        
        #if every vertex was already visited
        else:
            return self.selecionarMenorCaminho(todosCaminhos) 
