from typing import Counter, get_args


class Node:
    def __init__(self,data= None,next = None):
        self.data = data
        self.next = next



class LinkedList:
    def __init__(self):
        self.head = None 


    def insert(self,data):
        
        if(self.head == None):
            self.head = Node(data,None)
            return
        else:
            current = self.head
            while current:
                current = current.next
                current.next = Node(data,None)
                return
            
    def insert_after(self,value,data):
        self.node = Node(data)
        if self.head == None:
            self.head = Node(data, None)
            return
        else:
            current = self.head 
            while current.data != value:
                current = current.next
                self.node = current.next.next
                current.next = self.node
                return

                        



    def insert_at_begining(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def get_length(self):
        counter = 0 
        current = self.head
        while current:
            counter += 1
            current = current.next
        print(counter)

    def print_list(self):
        if self.head is None: 
            print('List is empty')
            return
        
        current = self.head
        list_string = ''

        while current:
            list_string += str(current.data) + '-->'
            current = current.next

        print(list_string)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert(data)
    
    def remove_at(self, index):
        if index <0 or index >= self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0: 
            self.head = self.head.next
            return
        
        count = 0
        current = self.head
        while current: 
            current = current.next



        
if __name__ == '__main__'    :
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(89)
    ll.insert(20)
    #ll.insert_after(5,22)
    ll.print_list()
    ll.get_length()