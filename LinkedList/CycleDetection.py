from LinkedList import *

"""Problem - given a linked list, determine if it contains a cycle"""

#Use Floyd's Cycle Detection Algorithm - Two pointers, one traverses the list twice as fast as the other. If they both meet, a cycle exists
def detect_cycle(list):
    head = list.get_head_node()
    slwPtr = head
    fstPtr = head

    while fstPtr is not None:
        fstPtr = fstPtr.get_next()
        if fstPtr is None:
            return True
        fstPtr = fstPtr.get_next() #The faste pointer needs to traverse the list at twice the speed of the slow pointer
        slwPtr = slwPtr.get_next()
        if fstPtr == slwPtr:
            return True
    #LinkedList has ended, therefore does not contain a cycle
    return False


#10->25->4->43->30
l1 = LinkedList()
l1.insert(10)
l1.insert(25,1)
l1.insert(4,2)
l1.insert(43,3)
l1.insert(30,4)
n1 = l1.search(30)
n2 = l1.search(4)
#Create a loop from 30->4
n1.set_next(n2)

#10->30->32->4
l2 = LinkedList()
l2.insert(10)
l2.insert(30,1)
l2.insert(32,2)
l2.insert(4,3)

print("Does l1 contain a cycle?", detect_cycle(l1))
print("Does l2 contain a cycle?", detect_cycle(l2))
