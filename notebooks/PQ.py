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
    """
    return PQ()

def insert(pq, value, Append = True):
    
    """
    >>> pq = new()
    >>> pq.size()
    0
    >>> insert(pq, 7)
    [7]
    >>> insert(pq, 6)
    [6, 7]
    """
   
    storage = 0
    
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
    '''
    >>> pq = new()
    >>> insert(pq, 3)
    [3]
    >>> insert(pq, 7)
    [3, 7]
    >>> insert(pq, 1)
    [1, 7, 3]
    >>> dm(pq)
    [3, 7]
    '''
    if value == -1:
        value = pq.data[len(pq.data)-1]
    
    if Assign:
        pq.data[0] = value
        pq.data.pop()

    leftParent = (pq.data.index(value)*2)+1
    rightParent = (pq.data.index(value)*2)+2
    

    if (leftParent) < len(pq.data):
        p1 = pq.data[(pq.data.index(value)*2)+1]
        p1Index = (pq.data.index(value)*2)+1
    if (rightParent) < len(pq.data):
        p2 = pq.data[(pq.data.index(value)*2)+2]
        p2Index = (pq.data.index(value)*2)+2
    else:
        return pq.data
    
    left = p1<p2

    if value <= p1 and left:
        return pq.data
    elif left and (p1Index) < len(pq.data) :
            pq.data[p1Index], pq.data[pq.data.index(value)] = pq.data[pq.data.index(value)], pq.data[p1Index]
            dm(pq, value, False)
    elif not left and (p2Index) < len(pq.data):
        pq.data[p2Index], pq.data[pq.data.index(value)] = pq.data[pq.data.index(value)], pq.data[p2Index]
        dm(pq, value, False)
    else:
        return pq.data

def fm(pq):
    '''
    >>> pq = new()
    >>> insert(pq, 3)
    [3]
    >>> insert(pq, 7)
    [3, 7]
    >>> insert(pq, 1)
    [1, 7, 3]
    >>> fm(pq)
    1
    '''
    return pq.data[0]

pq = new()

insert(pq, 7)
insert(pq, 1)
insert(pq, 4)
insert(pq, 8)
insert(pq, 9)
insert(pq, 2)
insert(pq, 3)
insert(pq, 6)
insert(pq, 5,)
print(pq.data)
dm(pq)
print(pq.data)


if __name__ == "__main__":
    import doctest
    doctest.testmod()