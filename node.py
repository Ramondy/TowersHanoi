class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.name = "Disk " + str(self.value)
        self.next_node = next_node

    def __str__(self):
        return self.name

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value
