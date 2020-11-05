//
//  main.swift
//  NovW1_2
//
//  Created by panjianting on 2020/11/4.
//

import Foundation


public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init() { self.val = 0; self.next = nil; }
    public init(_ val: Int) { self.val = val; self.next = nil; }
    public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
}


func insertionSortList(_ head: ListNode?) -> ListNode? {
    var head = head;
    var temp:ListNode? = nil;
    let ans = temp;
    
    while head != nil {
        if temp == nil {
            temp = head;
        }else{
            if var temp = temp {
                if temp.val > head!.val {
                    
                }
            }
        }
        
        head = head?.next;
    }
    return ans;
}
 

print("Hello, World!")

