from LinkedList import *
from LLUtil import *

"""
Problem - Find the middle node of a linked list
"""

"""
This method utilises two pointers, the first traverses the list 1 node at a time
and the other 2 nodes at a time. Since n is 2*(n/2) and the second pointer moves
twice as fast as the first, once the second pointer reaches n, the first will be
at n/2 which is the middle of the list. Once it has found the middle, it deletes
it from the list
"""
def remove_middle(list):
    fstPtr = list.get_head_node()
    slwPrev = None
    slwPtr = list.get_head_node()
    while fstPtr is not None:
        fstPtr = fstPtr.get_next()
        if fstPtr is None:
            break #We reached the end, as fstPtr is moving through twice as fast, the slow pointer should be in the middle of the list
        fstPtr = fstPtr.get_next()
        slwPrev = slwPtr
        slwPtr = slwPtr.get_next()

    #Middle has been found, so make slwPrev point to slwPtr's next node
    print("Removing", slwPtr.get_data(), "from the list!")
    slwPrev.set_next(slwPtr.get_next())



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

remove_middle(l1)
remove_middle(l2)
remove_middle(l3)

print(l1, "| size:", l1.get_size())
print(l2, "| size:", l2.get_size())
print(l3, "| size:", l3.get_size())
