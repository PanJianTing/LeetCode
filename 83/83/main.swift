//
//  main.swift
//  83
//
//  Created by panjianting on 2020/11/5.
//

import Foundation


public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init() { self.val = 0; self.next = nil; }
    public init(_ val: Int) { self.val = val; self.next = nil; }
    public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
}
 

func deleteDuplicates(_ head: ListNode?) -> ListNode? {
    
    var head = head
    var myHead:ListNode? = nil
    var temp:ListNode? = nil
    
    while head != nil {
        if myHead == nil{
            temp = head
            myHead = temp
        }else{
            if head!.val != temp?.val {
                temp?.next = head;
                temp = temp?.next;
            }
        }
        head = head?.next
    }
    temp?.next = nil
    
    return myHead;
}

var node1 = ListNode(1)
var node2 = ListNode(1)
var node3 = ListNode(2)
var node4 = ListNode(3)
var node5 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

var new = deleteDuplicates(node1)

print(new?.val)
print(new?.next?.val)
print(new?.next?.next?.val)
print(new?.next?.next?.next?.val)



print("Hello, World!")

