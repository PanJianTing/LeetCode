//
//  main.swift
//  NovW1_1
//
//  Created by panjianting on 2020/11/3.
//

import Foundation


public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init() { self.val = 0; self.next = nil; }
    public init(_ val: Int) { self.val = val; self.next = nil; }
    public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
}

func getDecimalValue(_ head: ListNode?) -> Int {
    var ans : Int = 0;
    var node = head;
    
    while node != nil {
        ans <<= 2;
        if let node = node {
            if node.val == 1 {
                ans += 1;
            }
        }
        
        node = node?.next
    }
    
    return ans;
}

func printBin(_ val : Int) {
    
    var mask = 2 // 10000000
    
    for _ in 0..<10 {
//        print((val & mask) == 0 ? 0:1, terminator:"");
        print(mask);
        mask <<= 2;
        
    }
    
    print("")
}

printBin(0);
//printBin(1);
//printBin(2);
//printBin(3);
//printBin(4);
//printBin(5);
//printBin(6);
//printBin(7);

print("Hello, World!")

