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

def insert(val, pq):
    
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
    pq.data.append(val)



def printElements(pq):
    '''
    
    >>> pq = new()
    >>> insert(7, pq)
    
    >>> pq.size()
    
    '''
    print(pq.data)

pq = new()
insert(7, pq)
printElements(pq)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
