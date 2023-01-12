class LinkedList:
    size = 0
    def __init__(self):
        self.Head = None
        LinkedList.size += 1

    def displayAll(self):
        nd = self.Head
        if self.Head == None:
            return None
        else:
            while nd != None:
                print(nd)
                nd = nd.Next
    def __repr__(self):
        return f"{self.head}"