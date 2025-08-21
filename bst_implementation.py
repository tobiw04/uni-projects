numbers = [-12, 4, 12, -3, 154, 13, 14]


class Node:
    
    def __init__(self, value):
        self.content = value
        self.left = None
        self.right = None

    def insert(self, value):
        new_node = Node(value)
        if value < self.content and self.left == None:
            self.left = new_node
        elif value >= self.content and self.right == None:
            self.right = new_node
        else:
            if value < self.content:
                self.left.insert(value)
            else:
                self.right.insert(value)

    def get_max(self):
        if self.right == None:
            return self.content
        else:
            return self.right.get_max()
    
    def remove_max(self):
        if self.right is None:
            return self.left
        else:
            parent = self
            cur = self.right
            while cur.right:
                parent = cur
                cur = cur.right
            parent.right = cur.left
            return self
        
    def remove(self, key):
        if self is None:
            return self
        elif self.content > key:
            self.left = self.left.remove(key)
            return self
        elif self.content < key:
            self.right = self.right.remove(key)
            return self
        elif self.left is None:
            return self.right
        else:
            self.content = self.left.get_max()
            self.left = self.left.remove_max()
            return self

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.content)
        if self.right:
            self.right.inorder()
    
    def inorder_list(self):
        new_list = []
        if self.left:
            new_list.extend(self.left.inorder_list())
        new_list.append(self.content) 
        if self.right:
            new_list.extend(self.right.inorder_list())
        return new_list
    
    def check(self): # Checks if BST criteria is valid
        if self.left is None and self.right is None:
            return True
        if self.left:
            if self.left.content > self.content:
                return False
            else:
                self.left.check()
        if self.right:
            if self.right.content < self.content:
                return False
            else:
                self.right.check()

                

root = Node(numbers[0])

for x in numbers[1:]:
    root.insert(x)

#root.insert(-5)
#root.remove_max()
#root.remove(154)
print(root.inorder_list())

print(root.check())

#print(bin(hash((45,55))))