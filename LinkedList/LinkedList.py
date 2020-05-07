class ListNode:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    #Get data associated with the given node
    def get_data(self):
        return self.data

    #Get the next node in the list
    def get_next(self):
        return self.next

    #Reassign the next node in the list
    def set_next(self, next):
        self.next = next

class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        curr = self.head
        if curr is None:
            return "Empty"
        s = "LinkedList: " + str(curr.get_data())
        while curr:
            curr = curr.get_next()
            if curr is not None:
                s = s + "->" + str(curr.get_data())
        return s

    def __str__(self):
        return self.__repr__()

    #Insert node to the start of the list - O(1) complexity
    def insert(self, data):
        #Create a new node for inserted data and set it's link to the current head
        list_node = ListNode(data, self.head)
        #Reassign head node to inserted node
        self.head = list_node

    #TODO: Allow nodes to be added to end or inside the LinkedList

    #Searches the list to find node to delete and sets the node before it to point to the node after it - O(n) complexity worse case
    def delete(self, data):
        curr = self.head
        prev = None
        #Loop until end of the list, comparing each node to needed node
        while curr:
            if curr.get_data() == data:
                break #Node has been found, stop looping
            else:
                prev = curr
                curr = curr.get_next()
        #If node cannot be found, raise error
        if curr is None:
            raise Error("Cannot find", data, " in the list!")

        if prev is None:
            self.head = curr.get_next()
        else:
            prev.set_next(curr.get_next())

    #Returns the size of the list - O(n) complexity
    def get_size(self):
        curr = self.head
        counter = 0
        #Loop unti curr is None. This indicates end of the list
        while curr:
            counter += 1
            curr = curr.get_next()
        return counter

    #Seach the list until a node containing required data is found - O(n) complexity worse case
    def search(self, data):
        curr = self.head
        #Loop until end of the list, comparing each node to needed node
        while curr:
            if curr.get_data() == data:
                break #Node has been found, stop looping
            else:
                curr = curr.get_next()
        #If node cannot be found, raise error
        if curr is None:
            raise Error("Cannot find", data, " in the list!")
        return curr
