class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    def get_next_node(self):
        return self.next_node
    def set_next_node(self, value):
        self.next_node = value

class Stack:
    def __init__(self, limit=None):
        self.top = None
        self.limit = limit
        self.size = 0
    def get_size(self):
        return self.size
    
    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
    def has_space(self):
        if self.size > self.limit:
            return False
        else:
            return self.size < self.limit
    def peek(self):
        if not self.is_empty():
            return self.top.get_value()
        else:
            print("Empty stack")
    def push(self, value):
        if self.has_space():
            new_top = Node(value)
            new_top.set_next_node(self.top)
            self.top = new_top
            self.size += 1
            print("Adding a new ring into the stack")
        else:
            print("The stack is full!")

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top
            self.top = item_to_remove.get_next_node()
            self.size -= 1
            print("Removing {} from the stack".format(item_to_remove.get_value()))
            return item_to_remove.get_value()
        else:
            print("No items to remove")

    def print_nodes(self):
        current_top = self.top
        string = ''
        while current_top:
            if current_top.get_value():
                string += str(current_top.get_value()) + "\n"
            current_top = current_top.get_next_node()
        return string
    
stk = Stack(5)
stk.push(10)
stk.push(20)
stk.push(30)
stk.pop()
print(stk.print_nodes())