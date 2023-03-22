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




if __name__ == "__main__":
    import doctest
    doctest.testmod()
