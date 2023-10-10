
def invertBinaryTree(root):
    if root:
        left = invertBinaryTree(root.right)
        right = invertBinaryTree(root.left)
        return root


if __name__ == '__main__':
    root =  [4,2,7,1,3,6,9]
    invertBinaryTree(root)







