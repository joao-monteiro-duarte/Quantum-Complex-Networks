from random import seed
from random import randint
seed(1)

class Heap:
    
    def __init__(self, N):
        self.pq=[]
        self.heapNodeFinder=[]

        for i in range(N):
            self.pq.append([float('inf'),i])
            self.heapNodeFinder.append(i)
        self.lastIndex=N-1         #Index on heap where last node is
        
    def isEmpty(self):

        if self.pq[0][0]==float('inf'):
            return True

        else:
            return False

#Equivale ao heappop: retira o primeiro elemento, substitui o ultimo pelo primeiro e reorganiza a arvore

    def extractMin(self):          
        min=self.pq[0]
        nodeOfmin=min[1]
        self.pq[0]=self.pq[self.lastIndex]
        self.pq[self.lastIndex]=[float('inf'),nodeOfmin]
       
        while self.pq[self.lastIndex]==float('inf'):
            self.lastIndex-=self.lastIndex

        currentTuple=self.pq[0]
        currentIndex=0
        Continue=True
        print(self.pq)
        while Continue:
            leftChildIndex=currentIndex*2+1
            rightChildIndex=currentIndex*2+2
            print(rightChildIndex)
            if rightChildIndex > len(self.pq)-1 or leftChildIndex > len(self.pq): break
            leftChild=self.pq[leftChildIndex]
            rightChild=self.pq[rightChildIndex]
            #Não existe nós onde o filho à esquerda devia estar                         
            if leftChildIndex>self.lastIndex:
                Continue=False

            #Nao exite nós onde o filho à direita devia estar (logo ha à esquerda)
            elif rightChildIndex > self.lastIndex: 

                #Verificar se esse filho é menor que o nó atual
                if leftChild<self.pq[currentIndex]:   
                    
                    #HeapFinder Change

                    self.heapNodeFinder[leftChild[1]]=currentIndex 
                    self.heapNodeFinder[currentTuple[1]]=leftChildIndex

                    #Heap Change
                    temp=leftChild
                    leftChild=currentTuple
                    currentTuple=temp

                    Continue=False
                
            #Existem filhos desse nó na árvore
            else:
                #Substitui o nó atual com o menor dos filhos caso seja menor que o actual
                if leftChild <= rightChild and leftChild < currentTuple:           
                    
                    #HeapFinder Change

                    self.heapNodeFinder[leftChild[1]]=currentIndex 
                    self.heapNodeFinder[currentTuple[1]]=leftChildIndex


                    #Heap Change
                    temp=leftChild
                    leftChild=currentTuple
                    currentTuple=temp


                    #for the algorithm to proceed
                
                    currentIndex=leftChildIndex
         
                elif leftChild>rightChild and rightChild < currentTuple:
                   #HeapFinder Change

                    self.heapNodeFinder[rightChild[1]]=currentIndex       #No heapfinder com índice igual ao nó que está no tuplo filho do indice atual (que mudou) passa a ser o indice atual (indice da heap)
                    self.heapNodeFinder[currentTuple[1]]=rightChildIndex


                    #Heap Change
                    temp=rightChild
                    rightChild=currentTuple
                    currentTuple=temp


                    #for the algorithm to proceed
                
                    currentIndex=rightChildIndex

                #Case the two childs are larger or equal to current                    
                else: Continue=False

        
        return min

    def updateHeap(self, w, n):
        '''
        if self.heapNodeFinder[n] == float('inf'):      #o nó n não está na heap
            print("n not in heap")
            self.pq[self.lastIndex]=[w,n]
            print("heapNodeFinder updated to ")
            self.heapNodeFinder[n]=self.lastIndex
            print(self.heapNodeFinder)
            currentIndex=self.lastIndex
            self.lastIndex+=1
            Continue=True
            #se o nó estiver num indice maior do que 0, o indice do pai é calculado
            if currentIndex>0:             
                parentIndex=((currentIndex+1)//2)-1
            #Nó é 0
            else:
                Continue=False       

            # se o pai for maior do que o filho trocam
            while Continue and self.pq[parentIndex] > self.pq[currentIndex]:     
                temp=self.pq[parentIndex]
                self.pq[parentIndex]=self.pq[currentIndex]
                self.pq[currentIndex]=temp
                self.heapNodeFinder[self.pq[parentIndex][1]]=parentIndex 
                self.heapNodeFinder[self.pq[currentIndex][1]]=currentIndex
                currentIndex=parentIndex

                #se o nó estiver num indice maior do que 0, o indice do pai é calculado
                if currentIndex>0:            
                    parentIndex=((currentIndex+1)//2)-1

                else:
                    Continue=False '''
    
        currentIndex=self.heapNodeFinder[n]

        if w < self.pq[currentIndex][0]:
            self.pq[currentIndex][0]=w
            Continue=True
            
            #se o nó estiver num indice maior do que 0, o indice do pai é calculado
            if currentIndex>0:             
                parentIndex=((currentIndex+1)//2)-1

            else:
                Continue=False         
            
            while Continue and self.pq[parentIndex] > self.pq[currentIndex]:
                
                vSon = self.pq[currentIndex][1]
                vParent = self.pq[parentIndex][1]

                #Heap changing
                
                temp = self.pq[parentIndex]               
                self.pq[parentIndex]=self.pq[currentIndex]
                self.pq[currentIndex]=temp
            
                #HeapFinder Change

                temp = self.heapNodeFinder[vParent]               
                self.heapNodeFinder[vParent]=self.heapNodeFinder[vSon]
                self.heapNodeFinder[vSon]=temp
                


                self.heapNodeFinder[self.pq[parentIndex][1]]=currentIndex       #No heapfinder com índice igual ao nó que está no tuplo pai do indice atual (que mudou) passa a ser o indice atual
                currentIndex=parentIndex
                self.heapNodeFinder[n]=currentIndex

                #se o nó estiver num indice maior do que 0, o indice do pai é calculado
                if currentIndex > 0:             
                    parentIndex=((currentIndex+1)//2)-1

                else:
                    Continue=False

def dijkstra(Graph, startingNode):
    Dist=[(float('inf'))] * Graph.size()
    Parent=[None] * Graph.size()
    Visited=[False] * Graph.size()
    pq=Heap(Graph.size())
    Dist[startingNode]=0
    # adjNode = tuple (n,w)
    for adjNode in Graph.get()[startingNode]:  
        print(Graph.get()[startingNode])                
        pq.updateHeap(adjNode[1], adjNode[0])
        Dist[adjNode[0]]=adjNode[1]
        Parent[adjNode[0]]=startingNode
    Visited[startingNode]=True

    if not pq.isEmpty():
        heapNotEmpty=True

    else:
        heapNotEmpty=False

    while heapNotEmpty:
        currentTuple = pq.extractMin()
        currentNode=currentTuple[1]
        
        for adjNode in Graph.get()[currentNode]:
            if Visited[adjNode[0]]: continue
            neighbour=adjNode[0]
            weightToNeighbour = adjNode[1]
            currentNodeMinDistance=Dist[currentNode]
            possibleNewDistance = currentNodeMinDistance + weightToNeighbour 
            currentMinDistanceToneighbour = Dist[neighbour]
            
            if possibleNewDistance < currentMinDistanceToneighbour:
                Parent[neighbour]=currentNode
                Dist[neighbour] = possibleNewDistance
                pq.updateHeap(possibleNewDistance,neighbour)
                
        if pq.isEmpty():
            heapNotEmpty=False
        print (Dist)
        print (Parent)
        
 #G generate random self.G which is a list of adjencies where N-number of nodes and E-number of edges   
class G:    
    def __init__(self, N, E):
        self.Graph=[]

        for _ in range(N):
            self.Graph.append([])

        for _ in range(E-1):
            n1=randint(0,N-1)
            n2=randint(0,N-1)

            while n1==n2:
                n2 = randint(0,N-1)
            
            while len(self.Graph[n1])==N-1:
                n1=randint(0,N-1)
            
            while n2 in self.Graph[n1]:
                n2=randint(0,N-1)
            
            w=randint(1,E)

            self.Graph[n1].append((n2,w))
            self.Graph[n2].append((n1,w))

        self.Graph=[[(1,7),(2,9),(5,14)],[(0,7),(2,10),(3,15)], [(0,9),(1,10),(3,11),(5,2)], [(1,15),(2,11),(4,6)], [(3,6),(5,9)], [(0,14),(2,2),(4,9)]]
        print(self.Graph)

    def get(self):
        return self.Graph
    
    def size(self):
        length=len(self.Graph)
        return length

graphTest=G(5,9)
dijkstra(graphTest, 0)
