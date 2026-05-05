# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return ""
        q=[root]
        res=[]
        while q:
            node=q.pop(0)
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")
        return ",".join(res)
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        

    def deserialize(self, data):
        if not data:
            return None
        nodes=data.split(',')
        root=TreeNode(int(nodes[0]))
        q=[root]
        i=1
        while q:
            node=q.pop(0)
            if nodes[i]!="null":
                node.left=TreeNode(int(nodes[i]))
                q.append(node.left)
            i+=1
            if nodes[i]!="null":
                node.right=TreeNode(int(nodes[i]))
                q.append(node.right)
            i+=1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))