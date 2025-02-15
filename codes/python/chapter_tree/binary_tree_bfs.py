"""
File: binary_tree_bfs.py
Created Time: 2022-12-20
Author: a16su (lpluls001@gmail.com)
"""

import sys, os.path as osp
import typing

sys.path.append(osp.dirname(osp.dirname(osp.abspath(__file__))))
from include import *


""" 层序遍历 """
def hier_order(root: TreeNode):
    # 初始化队列，加入根结点
    queue = collections.deque()
    queue.append(root)
    # 初始化一个列表，用于保存遍历序列
    res = []
    while queue:
        node = queue.popleft()       # 队列出队
        res.append(node.val)         # 保存节点值
        if node.left is not None:
            queue.append(node.left)  # 左子结点入队
        if node.right is not None:
            queue.append(node.right) # 右子结点入队
    return res


""" Driver Code """
if __name__ == "__main__":
    # 初始化二叉树
    # 这里借助了一个从数组直接生成二叉树的函数
    root = list_to_tree(arr=[1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, None, None])
    print("\n初始化二叉树\n")
    print_tree(root)

    # 层序遍历
    res = hier_order(root)
    print("\n层序遍历的结点打印序列 = ", res)
    assert res == [1, 2, 3, 4, 5, 6, 7]
