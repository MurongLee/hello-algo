/*
 * File: binary_tree.cpp
 * Created Time: 2022-11-25
 * Author: Krahets (krahets@163.com)
 */

#include "../include/include.hpp"


/* Driver Code */
int main() {
    /* 初始化二叉树 */
    // 初始化结点
    TreeNode* n1 = new TreeNode(1);
    TreeNode* n2 = new TreeNode(2);
    TreeNode* n3 = new TreeNode(3);
    TreeNode* n4 = new TreeNode(4);
    TreeNode* n5 = new TreeNode(5);
    // 构建引用指向（即指针）
    n1->left = n2;
    n1->right = n3;
    n2->left = n4;
    n2->right = n5;
    cout << endl << "初始化二叉树\n" << endl;
    PrintUtil::printTree(n1);

    /* 插入与删除结点 */
    TreeNode* P = new TreeNode(0);
    // 在 n1 -> n2 中间插入结点 P
    n1->left = P;
    P->left = n2;
    cout << endl << "插入结点 P 后\n" << endl;
    PrintUtil::printTree(n1);
    // 删除结点 P
    n1->left = n2;
    delete P;  // 释放内存
    cout << endl << "删除结点 P 后\n" << endl;
    PrintUtil::printTree(n1);

    return 0;
}
