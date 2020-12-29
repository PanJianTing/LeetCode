//
//  main.swift
//  1469_FindAllTheLonelyNodes
//
//  Created by panjianting on 2020/12/29.
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



func getLonelyNodes(_ root: TreeNode?) -> [Int] {
    
    
    return [10,10]
}


print(getLonelyNodes(<#T##root: TreeNode?##TreeNode?#>))
print("Hello, World!")

