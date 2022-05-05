class PyList(object):
    def __init__(self, size=1):
        self.items = [None] * size
        self.numItems = 0

    def append(self, item):
        if self.numItems == len(self.items):
            newlst = [ None ] * size * 2

            for k in range(len(self.items)):
                newlst[k] = self.items[k]

            self.items[k] = newlst
        
        self.items[self.numItems] = item
        self.numItems += 1
        