#python program to reverse a linked list
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
#creating a linked list
head = node(1)
head.next = node(2)
head.next.next = node(3)
head.next.next.next = node(4)
head.next.next.next.next = node(5)
#reversing linked list
prev =None
curr = head
while curr:
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node
head = prev 
temp = head
while temp:
    print(temp.data, end =" -> " if temp.next else "")
    temp = temp.next