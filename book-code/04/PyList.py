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

    def __getitem__(self, index):
        if index >= 0 and index < self.numItems:
            return self.items[index]
        else:
            raise IndexError('Index out of range')

    def __setitem__(self, index, val):
        if index >= 0 and index < self.numItems:
            self.items[index] = val
            return
        else:
            raise IndexError('Index out of range')

    def __add__(self, other):
        result = PyList(size = self.numItems + other.numItems)

        for i in range(self.numItems):
            result.append(self.items[i])

        for j in range(other.numItems):
            result.append(other.items[j])

        return result

    def __makeroom(self):
        newlen = (self.size // 4 )+ self.size + 1
        newlst = [ None ] * newlen

        for i in range(self.numItems):
            newlst[i] = self.items[i]

        self.items = newlst
        self.numItems = newlen

    def append(self, item):
        if self.numItems == self.size:
            self.__makeroom()

        self.items[self.numItems + 1] = item 
        self.numItems += 1

        