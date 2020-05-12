class LinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None
    def add_to_end(self,value):
        new_node = Node(value)

        if not self.head and not self.tail:
            self.head = new_node
            self.head = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node


    def remove_from_head(self):
        if not self.head:
            return None
        else:
            value = self.head.get_value()
