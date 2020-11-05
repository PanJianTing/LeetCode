//
//  main.swift
//  100
//
//  Created by panjianting on 2020/11/5.
//

import Foundation

public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init() { self.val = 0; self.left = nil; self.right = nil; }
    public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
    public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}

// 遞迴解法：判斷當前的結點值是否相同，相同則遞迴左節點與右節點。不同則回傳false。
func isSameTree(_ p: TreeNode?, _ q: TreeNode?) -> Bool {
    
    if let p = p, let q = q {
        if p.val != q.val{
            return false
        }else{
            if isSameTree(p.right, q.right) && isSameTree(p.left, q.left) {
                return true
            }else{
                return false
            }
        }
    }
    return p === q; // 判斷p跟q的記憶體位址是否一樣。(當兩個都指向nil的時候，會是true)
}


var node1 = TreeNode(1);
var node2 = TreeNode(2);
var node3 = TreeNode(3);

node1.left = node2
node1.right = node3


var node11 = TreeNode(1);
var node21 = TreeNode(2);
var node31 = TreeNode(3);

node11.left = node21
node11.right = node31

print(isSameTree(node1, node11))

print("Hello, World!")

