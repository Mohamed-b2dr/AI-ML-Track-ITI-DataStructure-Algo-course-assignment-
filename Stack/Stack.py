
from node import Node
from LinkedList import LinkedList




class Stack:
    def __init__(self):
        self.Ls = LinkedList()

    def push(self, node):
        if self.Ls.Head == None:
            self.Ls.Head = node
        else:
            nd = node
            nd.Next = self.Ls.Head
            self.Ls.Head = nd

    def pop(self):
        if self.Ls.Head == None:
            return None
        else:
            nd = self.Ls.Head
            self.Ls.Head = self.Ls.Head.Next
            nd.Next = None
            return nd.Data

    def _repr_(self):
        return f"List({self.Ls})"

    def displayAll(self):
        self.Ls.displayAll()



if __name__ == '__main__':
    S = Stack()
    while True:
        print("""
                1- push
                2-pop
                3-displayAll
                4-Exist
        
                """)
        choose = int(input('Enter CAHOOSE\n'))
        if choose == 1:
            inp = int(input('Enter element\n'))
            S.push(Node(inp))

        elif  choose == 2:
              print('Pop\n')
              S.pop()
        elif choose == 3:
            S.displayAll()
        elif choose == 4:
            break
