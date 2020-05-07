from LinkedList import *
from LLUtil import *

"""
Problem - Find the middle node of a linked list
"""

"""
This method requires first finding the size of the linked list 'n' and then
it moves through the first half 'n/2' part of the list
"""

def slow(list):
    size = list.get_size() #O(n) complexity
    middle = int(size/2)
    curr = list.get_head_node()
    for i in range(0, middle):
        curr = curr.get_next()
    return curr.get_data()

def fast(list):
    fstPtr = list.get_head_node()
    slwPtr = list.get_head_node()
    while fstPtr is not None:
        fstPtr = fstPtr.get_next()
        if fstPtr is None:
            break #We reached the end, as fstPtr is moving through twice as fast, the slow pointer should be in the middle of the list
        fstPtr = fstPtr.get_next()
        slwPtr = slwPtr.get_next()
    return slwPtr.get_data()


#10->25->4->43->30
l1 = LinkedList()
l1.insert(10)
l1.insert(25)
l1.insert(4)
l1.insert(43)
l1.insert(30)

#10->30->32->4
l2 = LinkedList()
l2.insert(10)
l2.insert(30)
l2.insert(32)
l2.insert(4)

l3 = generate_list(20)

print(l1, "| size:", l1.get_size())
print(l2, "| size:", l2.get_size())
print(l3, "| size:", l3.get_size())

print("Middle of l1 (slow): ", slow(l1))
print("Middle of l2 (slow): ", slow(l2))
print("Middle of l2 (slow): ", slow(l3))
print("Middle of l1 (fast): ", fast(l1))
print("Middle of l2 (fast): ", fast(l2))
print("Middle of l2 (fast): ", fast(l3))
