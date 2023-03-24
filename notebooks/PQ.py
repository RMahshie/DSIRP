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

def insert(pq, value, Append):
    
    """
    >>> pq = new()
    >>> pq.size()
    0
    >>> insert(pq, 7, True)
    [7]
    >>> insert(pq, 6, True)
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


def dm(pq, value, Assign):
    if Assign:
        print("pq.data: ", pq.data)
        print("value: ", value)
        pq.data[0] = value
        print("pq.data after setting first to value: ", pq.data)
        pq.data.pop()
    leftParent = (pq.data.index(value)*2)+1
    rightParent = (pq.data.index(value)*2)+2
    print("pq.data: ", pq.data)
    print("value index: ",pq.data.index(value))
    if (leftParent) < len(pq.data):
        p1 = pq.data[(pq.data.index(value)*2)+1]
        p1Index = (pq.data.index(value)*2)+1
    if ((pq.data.index(value)*2)+2) < len(pq.data):
        p2 = pq.data[(pq.data.index(value)*2)+2]
        p2Index = (pq.data.index(value)*2)+2
    else:
        return pq.data
    print("left parent", p1)
    print("right parent", p2)
    print("Swap Left?", p1<p2)
    left = p1<p2
    print()
    if value <= p1:
        return pq.data
    elif left and (p1Index) < len(pq.data) :
            pq.data[p1Index], pq.data[pq.data.index(value)] = pq.data[pq.data.index(value)], pq.data[p1Index]
            dm(pq, value, False)
    elif not left and (p2Index) < len(pq.data):
        pq.data[p2Index], pq.data[pq.data.index(value)] = pq.data[pq.data.index(value)], pq.data[p2Index]
        dm(pq, value, False)
    else:
        return pq.data

    

pq = new()
insert(pq, 7, True)
insert(pq, 6, True)
insert(pq, 5, True)
insert(pq, 4, True)
dm(pq, pq.data[len(pq.data)-1], True)
print(pq.data)
if __name__ == "__main__":
    import doctest
    doctest.testmod()
