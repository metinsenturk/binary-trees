class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_node(self):
        print(self.data)

    def print_in_order(self):
        if self.left:
            self.left.print_in_order()
        print(self.data)
        if self.right:
            self.right.print_in_order()

    def print_pre_order(self):
        print(self.data)
        if self.left:
            self.left.print_pre_order()
        if self.right:
            self.right.print_pre_order()

    def print_post_order(self):
        if self.left:
            self.left.print_post_order()
        if self.right:
            self.right.print_post_order()
        print(self.data)

    def insert(self, data):
        # when there is no binary tree initiated, this will create the root node
        if self.data is None:
            self = data
        # when there is data
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def contains(self, data):
        if self.data == data:
            return print("Found")
        if data < self.data:
            if self.left is None:
                return print("Not Found")
            else:
                self.left.contains(data)
        elif data > self.data:
            if self.right is None:
                return print("Not Found")
            else:
                self.right.contains(data)


print("Root 1")
root = Node(20)
root.left = Node(8)
root.left.left = Node(5)
root.left.right = Node(6)
root.right = Node(28)
root.right.left = Node(24)
root.right.right = Node(32)
root.print_node()
root.print_in_order()

root2 = Node(43)
root2.insert(23)
root2.insert(53)
root2.insert(24)
root2.insert(12)
root2.insert(34)
print("Root 2 in order")
root2.print_in_order()
print("Root 2 pre order")
root2.print_pre_order()
print("Root 2 post order")
root2.print_post_order()

root2.contains(34)
root2.contains(24)
root2.contains(14)


