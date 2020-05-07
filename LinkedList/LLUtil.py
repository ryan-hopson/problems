from LinkedList import LinkedList
import random

#Generate a random linked list of size n
def generate_list(n, min=0, max=100):
    l = LinkedList()
    for i in range(n):
        l.insert(random.randint(min, max))
    return l
