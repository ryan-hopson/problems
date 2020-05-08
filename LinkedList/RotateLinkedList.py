from LinkedList import LinkedList
"""
Problem - Left rotate a linked list by n nodes
"""

def rotate(list, n):
    print("Rotating list by", n)
    head = list.get_head_node()
    k = head
    #Get the kth node as it will be the new tail of the list
    for i in range(n-1):
        k = k.get_next()
        if k is None: #Handle cases where n>size
            k = head
    #If k is already of the tail, nothing needs to be done so return
    if k.get_next() is None:
        #List remains the same
        return
    #The element after k will be the new head
    k_next = k.get_next()
    prev = k
    curr = k_next
    #Find the tail as it needs to be attached to the old head
    while curr is not None:
        prev = curr
        curr = curr.get_next()
    prev.set_next(head)
    list.set_head(k_next)
    k.set_next(None)



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

print(l1)
rotate(l1, 3)
print(l1)

print(l2)
rotate(l2, 11)
print(l2)
