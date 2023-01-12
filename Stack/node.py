class Node:
    def __init__(self, data) -> None:
        self.Data = data
        self.Next = None
    
    def __repr__(self) -> str:
            return f"(Node: (Data:{self.Data})"