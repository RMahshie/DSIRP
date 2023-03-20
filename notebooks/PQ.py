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
        
    '''
    >>> pq = new()
    >>> isinstance(pq, PQ)
    True
    '''
    return PQ()






if __name__ == "__main__":
    import doctest
    doctest.testmod()
