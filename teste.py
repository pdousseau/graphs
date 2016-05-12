from grafos import grafos
import unittest

class TesteGrafos(unittest.TestCase):
    
    def testeOrdem(self):
        grafo = grafos()
        grafo.adicionarVertice("A",10)
        grafo.adicionarVertice("B",15)
        grafo.adicionarVertice("C",20)
        self.assertEqual(grafo.ordem(),3)
        grafo.removerVertice("A")
        self.assertEqual(grafo.ordem(),2)
        grafo.adicionarVertice("D", 15)
        self.assertEqual(grafo.ordem(),3)
        grafo.adicionarAresta("B", "C", 10)
        self.assertEqual(grafo.ordem(),3)
        grafo.removerAresta("B", "C")
        self.assertEqual(grafo.ordem(),3)
    
    def testeGrau(self):
        grafo = grafos()
        grafo.adicionarVertice("A",10)
        grafo.adicionarVertice("B",15)
        grafo.adicionarVertice("C",20)
        grafo.adicionarVertice("D",20)
        grafo.adicionarVertice("E",20)
        grafo.adicionarAresta("A", "B", 10)
        grafo.adicionarAresta("A", "C", 10)
        grafo.adicionarAresta("A", "D", 10)
        grafo.adicionarAresta("B", "D", 10)
        grafo.adicionarAresta("B", "C", 10)
        self.assertEqual(grafo.grau("A"),3)
        self.assertEqual(grafo.grau("B"),3)
        self.assertEqual(grafo.grau("C"),2)
        self.assertEqual(grafo.grau("D"),2)
        self.assertEqual(grafo.grau("E"),0)
        grafo.removerAresta("A", "B")
        self.assertEqual(grafo.grau("A"),2)
        self.assertEqual(grafo.grau("B"),2)
        self.assertEqual(grafo.grau("C"),2)
        self.assertEqual(grafo.grau("D"),2)
        self.assertEqual(grafo.grau("E"),0)
        grafo.removerVertice("A")
        self.assertFalse(grafo.grau("A"))
        self.assertEqual(grafo.grau("B"),2)
        self.assertEqual(grafo.grau("C"),1)
        self.assertEqual(grafo.grau("D"),1)
        self.assertEqual(grafo.grau("E"),0)
        grafo.adicionarVertice("A",10)
        self.assertEqual(grafo.grau("B"),2)
        self.assertEqual(grafo.grau("C"),1)
        self.assertEqual(grafo.grau("D"),1)
        self.assertEqual(grafo.grau("E"),0)
    
    def testeRetornarVertices(self):
        grafo = grafos()
        grafo.adicionarVertice("A",1)
        grafo.adicionarVertice("B",2)
        grafo.adicionarVertice("C",3)
        grafo.adicionarVertice("D",4)
        grafo.adicionarVertice("E",5)
        vert = {'A': 1, 'C': 3, 'B': 2, 'E': 5, 'D': 4}
        self.assertEqual(grafo.retornarVertices(),vert)
        grafo.removerVertice("A")
        vert = {'C': 3, 'B': 2, 'E': 5, 'D': 4}
        self.assertEqual(grafo.retornarVertices(),vert)
        
    def testeRetornarArestas(self):
        grafo = grafos()
        grafo.adicionarVertice("A",1)
        grafo.adicionarVertice("B",2)
        grafo.adicionarVertice("C",3)
        grafo.adicionarVertice("D",4)
        grafo.adicionarVertice("E",5)
        grafo.adicionarAresta("A", "B",6)
        grafo.adicionarAresta("A", "C",7)
        grafo.adicionarAresta("A", "D",8)
        grafo.adicionarAresta("B", "D",9)
        grafo.adicionarAresta("B", "C",10)
        arest = {'B':6,'C':7,'D':8}
        self.assertEqual(grafo.retornarArestas("A"),arest)
        arest = {'B':10,'A':7}
        self.assertEqual(grafo.retornarArestas("C"),arest)
        grafo.removerAresta("A", "B")
        arest = {'C':7,'D':8}
        self.assertEqual(grafo.retornarArestas("A"),arest)
        arest = {'C':10,'D':9}
        self.assertEqual(grafo.retornarArestas("B"),arest)
        grafo.removerVertice("A")
        self.assertFalse(grafo.retornarArestas("A"))
        grafo.adicionarVertice("A",10)
        arest = {}
        self.assertEqual(grafo.retornarArestas("A"),arest)
    
    def testVerticeAleatorio(self):
        grafo = grafos()
        grafo.adicionarVertice("A",1)
        grafo.adicionarVertice("B",2)
        grafo.adicionarVertice("C",3)
        grafo.adicionarVertice("D",4)
        grafo.adicionarVertice("E",5)
        
    def testAdjacentes(self):
        grafo = grafos()
        grafo.adicionarVertice("A",1)
        grafo.adicionarVertice("B",2)
        grafo.adicionarVertice("C",3)
        grafo.adicionarVertice("D",4)
        grafo.adicionarVertice("E",5)
        grafo.adicionarAresta("A", "B",6)
        grafo.adicionarAresta("A", "C",7)
        grafo.adicionarAresta("A", "D",8)
        grafo.adicionarAresta("B", "D",9)
        grafo.adicionarAresta("B", "C",10)
        adj = {'B':6,'C':7,'D':8}
        self.assertEqual(grafo.adjacentes("A"),adj)
        grafo.removerAresta("A", "B")
        adj = {'C':7,'D':8}
        self.assertEqual(grafo.adjacentes("A"),adj)
    
    def testMenorCaminhoSimples(self):
        g = grafos()
        
        #simple graph with just one path
        g.adicionarVertice("A",1)
        g.adicionarVertice("B",2)
        g.adicionarVertice("C",3)
        g.adicionarVertice("D",4)
        g.adicionarVertice("E",5)
        g.adicionarVertice("F",6)
        g.adicionarVertice("G",7)
        g.adicionarVertice("H",8)
        g.adicionarAresta("A", "B", 1)
        g.adicionarAresta("B","C",2)
        g.adicionarAresta("C","D",3)
        
        #reachs through one single direct path
        caminho = ['A','B','C','D']
        self.assertEqual(g.buscaMenorCaminho("A", "D"),caminho)
        
        #impossible to reach
        self.assertEqual(g.buscaMenorCaminho("A", "F"),None)
        
        #destiny doesnt exist
        self.assertEqual(g.buscaMenorCaminho("F","G"),None)
        
        #source doesnt exist
        self.assertEqual(g.buscaMenorCaminho("M","N"),None)
        
        #reachs through two paths
        g.adicionarAresta("A","E",1)
        g.adicionarAresta("A","H",8)
        g.adicionarAresta("F","H",10)
        caminho = ['A', 'B','C', 'D']
        self.assertEqual(g.buscaMenorCaminho("A","D"),caminho)
        
        caminho = ['A', 'E']
        self.assertEqual(g.buscaMenorCaminho("A","E"),caminho)
        
        caminho = ['A', 'H', 'F']
        self.assertEqual(g.buscaMenorCaminho("A","F"),caminho)
        g.adicionarAresta("F","D",100)
        caminho = ['A', 'H', 'F']
        self.assertEqual(g.buscaMenorCaminho("A","F"),caminho)
        

if __name__ == '__main__':
    unittest.main() 
