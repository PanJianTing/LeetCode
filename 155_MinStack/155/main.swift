//
//  main.swift
//  155
//
//  Created by panjianting on 2020/11/9.
//

import Foundation


class Node {
    var val:Int
    var next:Node?
    
    init() {
        self.val = 0;
        self.next = nil;
    }
    
    init(_ val:Int) {
        self.val = val;
        self.next = nil;
    }
    
}

class MinStack {

    var minCount:Int
    var topNode:Node? = nil
    
    /** initialize your data structure here. */
    init() {
        self.minCount = 99999999999999
        self.topNode = nil;
    }
    
    func push(_ x: Int) {
        let node = Node(x);
        node.next = topNode
        topNode = node;
        
        self.minCount = min(self.minCount, x);
    }
    
    func pop() {
        topNode = topNode?.next
    }
    
    func top() -> Int {
        if let topNode = topNode {
            return topNode.val
        }
        return 0
        
    }
    
    func getMin() -> Int {
        
//        var temp = self.topNode
//        var minCount = 99999999999999
//
//        while temp != nil {
//            minCount = min(temp!.val, minCount);
//            temp = temp?.next;
//        }
        
        return minCount
    }
}

var stack = MinStack()

print("Hello, World!")

