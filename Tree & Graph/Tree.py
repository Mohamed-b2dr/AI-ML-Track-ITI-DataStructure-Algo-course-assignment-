from algorthmis import *
from nodes import Node

nd1 = Node(1)
nd2 = Node(2)
nd3 = Node(3)
nd1.right = nd3
nd1.left = nd2

nd4 = Node(4)
nd5 = Node(5)
nd2.right = nd5
nd2.left = nd4

nd6 = Node(6)
nd3.right = nd6

nd7 = Node(7)
nd4.left = nd7

nd8 = Node(8)
nd5.left = nd8

nd9 = Node(9)
nd10 = Node(10)
nd6.left = nd9
nd6.right = nd10

nd11 = Node(11)
nd9.left = nd11

nd12 = Node(12)
nd10.left = nd12

print('preOrderTersal', preOrderTersal(nd1))
print('PostorderravTersal', PostorderravTersal(nd1))
print('inorderTraversal', inorderTraversal(nd1))
