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
    >>> insert(7, pq)
    >>> pq.size()
    1
    >>> insert(6, pq)
    >>> pq.size()
    2
    """
   
    storage = 0
    
    if Append:
        print("before adding value ", pq.data)
        pq.data.append(value)
        print("after adding value: ", pq.data)
    
    valueI = pq.data.index(value)
    parent = pq.data[(pq.data.index(value)-1)//2]
    parentI = (pq.data.index(value)-1)//2
    
    print("value: ", value)
    print("parent: ", parent)
    if pq.data.index(value) == 0:
        return pq.data
    
    elif value <= parent:
        
        pq.data[parentI], pq.data[valueI] =  pq.data[valueI], pq.data[parentI]
        
        print("after swap: ", pq.data)
        insert(pq, value, False)
    
    return 'Sorted Heap: ', pq.data

pq = new()
insert(pq, 7, True)
insert(pq, 8, True)
insert(pq, 5, True)
insert(pq, 1, True)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
