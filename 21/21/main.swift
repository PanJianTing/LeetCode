//
//  main.swift
//  21
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

// 先創一個temp的node，然後去循環l1,l2的val，比較兩個大小，接上比較小的node。最後再找沒有到nil的list。然後再接上去。
func mergeTwoLists(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
    
    var temp:ListNode = ListNode(-1);
    let ans = temp
    var node1 = l1;
    var node2 = l2;
    
    while true {
        
        if let n1 = node1, let n2 = node2 {
            if n1.val > n2.val{
                temp.next = node2
                node2 = n2.next
            }else{
                temp.next = node1
                node1 = n1.next
            }
            
            if temp.next != nil {
                temp = temp.next!
            }
        }else{
            break;
        }
    }
    
    if let n1 = node1{
        temp.next = n1;
    }
    
    if let n2 = node2{
        temp.next = n2
    }
    
    return ans.next;
}


print("Hello, World!")

