def preOrderTersal(root, result = []):
    if root:
            result.append(root.data)
            preOrderTersal(root.left, result)
            preOrderTersal(root.right, result)
    return result

def PostorderravTersal(root, result = []):
        if root:
            PostorderravTersal(root.left, result)
            PostorderravTersal(root.right, result)
            result.append(root.data)
        return result

def inorderTraversal( root, result = []):
        if root:
            inorderTraversal(root.left, result)
            result.append(root.data)
            inorderTraversal(root.right, result)
        return result