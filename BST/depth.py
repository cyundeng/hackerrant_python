class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        cur_depth = 0
        self.longest = 1
        self.getDepth(root, cur_depth)
        return self.longest - 1

    def getDepth(self, cur_node, cur_depth):
        cur_depth += 1
        if cur_node is None:
            cur_depth -= 1
            return cur_depth
        else:
            cur_depth = self.getDepth(cur_node.left, cur_depth)
            print(cur_node.data, cur_depth)
            if self.longest < cur_depth:
                self.longest = cur_depth
            cur_depth = self.getDepth(cur_node.right, cur_depth)
            return cur_depth - 1

    def getHeight2(self, root):
        if root is None:
            return -1
        leftDepth = self.getHeight2(root.left)
        rightDepth = self.getHeight2(root.right)

        return (leftDepth if leftDepth > rightDepth else rightDepth) + 1


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
height = myTree.getHeight2(root)
print(height)
