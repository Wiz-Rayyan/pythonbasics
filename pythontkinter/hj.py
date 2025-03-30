class Node:
 def __init__(self, val, next=None):
  self.val = val
  self.next = next

  def __str__(self):
    return str(self.val)

h = Node(1)

a = Node(2)
h.next = a
b = Node(3)
a.next = b

cur = h
while cur:
  print(cur)
  cur = cur.next
