import networkx as nx
from EoN import hierarchy_pos



class PQ:

    """
    >>> pq = new()
    >>> pq.size()
    0
    """

    def __init__(self):
        self.data = []

    def __eq__(self, other):
        return self.data == other.data

    def size(self):
        return len(self.data)


def new():

    """
    >>> pq = new()
    >>> isinstance(pq, PQ)
    True
    >>> pq.size()
    0
    """


    return PQ()

def insert(pq, value, Append = True):
   
    '''
    >>> pq = new()
    >>> insert(pq, 7)
    [7]
    >>> pq.size()
    1
    >>> insert(pq, 6)
    [6, 7]
    >>> pq.size()
    2

    '''
    
    
    if Append:
        pq.data.append(value)
    
    valueI = pq.data.index(value)
    parent = pq.data[(pq.data.index(value)-1)//2]
    parentI = (pq.data.index(value)-1)//2
    
    if pq.data.index(value) == 0:
        return pq.data
    
    elif value <= parent:
        
        pq.data[parentI], pq.data[valueI] =  pq.data[valueI], pq.data[parentI]
        
        insert(pq, value, False)
    
    return pq.data


def dm(pq, value = -1, Assign = True):
    
   
    if len(pq.data) == 2:
        pq.data.pop()
        return pq.data
    if value == -1:
        value = pq.data[len(pq.data)-1]
    
    if Assign:
        pq.data[0] = value
        pq.data.pop()

    if len(pq.data) < 2:
        leftChild = (pq.data.index(value)*2)+1
    else:  
        leftChild = (pq.data.index(value)*2)+1
        rightChild = (pq.data.index(value)*2)+2
    
        
    if (rightChild) < len(pq.data):
        c1 = pq.data[leftChild]
        c2 = pq.data[rightChild]
    else:
        return pq.data
    
    left = c1<c2

    if value <= c1 and left:
        return pq.data
    elif rightChild < len(pq.data):
        if left:
            pq.data[leftChild], pq.data[pq.data.index(value)] = pq.data[pq.data.index(value)], pq.data[leftChild]
            dm(pq, value, False)
        elif not left:
            pq.data[rightChild], pq.data[pq.data.index(value)] = pq.data[pq.data.index(value)], pq.data[rightChild]
            dm(pq, value, False)
        else:
            return pq.data

    

def fm(pq):
    
    '''
    >>> pq = new()
    >>> insert(pq, 7)
    [7]
    >>> pq.size()
    1
    >>> insert(pq, 6)
    [6, 7]
    >>> insert(pq, 3)
    [3, 7, 6]
    >>> pq.size()
    3
    >>> dm(pq)
    [6, 7]
    >>> insert(pq, 3)
    [3, 7, 6]
    >>> fm(pq)
    3
    '''
    return pq.data[0]
    

def heapSort(list):
    for item in list:
        insert(pq, item)
    print(pq.data)
        
    

def make_dag(heap):
    """Make a NetworkX graph that represents the heap."""
    G = nx.DiGraph()
    
    for i in range(1, len(heap)):
        parent = (i-1)//2
        G.add_edge(parent, i)
    
    return G


def draw_heap(heap):
    G = make_dag(heap)
    pos = hierarchy_pos(G)
    labels = dict(enumerate(heap))
    nx.draw(G, pos, labels=labels, alpha=0.4)


##list = [2, 5, 6, 8, 7, 4, 3, 1, 9]
##pq = new()
##heapSort(list)
##draw_heap(pq.data)

pq = new()
insert(pq, 5)
insert(pq, 6)
insert(pq, 7)

dm(pq)
dm(pq)
dm(pq)
print(pq.data)



if __name__ == "__main__":
    import doctest
    doctest.testmod()