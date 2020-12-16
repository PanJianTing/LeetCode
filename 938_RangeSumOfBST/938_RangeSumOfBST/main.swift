//
//  main.swift
//  938_RangeSumOfBST
//
//  Created by panjianting on 2020/11/26.
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


class Solution {
    var ans : Int = 0
    var low : Int = 0
    var high : Int = 0
    
    func dps(_ node : TreeNode?) {
        
        if let val = node?.val{
            if val >= self.low && val <= high{
                ans += val
            }
        }
        
        if node != nil {
            if node?.left != nil{
                dps(node?.left)
            }
            if node?.right != nil{
                dps(node?.right)
            }
        }
    }
    
    func rangeSumBST(_ root: TreeNode?, _ low: Int, _ high: Int) -> Int {
        
        self.ans = 0
        self.low = low
        self.high = high
        dps(root)
        
        return self.ans
    }
}




let node10 = TreeNode(10)
let node5 = TreeNode(5)
let node15 = TreeNode(15)
let node3 = TreeNode(3)
let node7 = TreeNode(7)
let node18 = TreeNode(18)

node10.left = node5
node10.right = node15
node5.left = node3
node5.right = node7
node15.right = node18

let sol = Solution()
print(sol.rangeSumBST(node10, 7, 15))
//rangeSumBST(node10, 7, 15)


print("Hello, World!")

