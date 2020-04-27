//
//  main.swift
//  24. Swap Nodes in Pairs
//
//  Created by panjianting on 2020/4/23.
//  Copyright © 2020 panjianting. All rights reserved.
//

import Foundation

public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init(_ val: Int) {
        self.val = val
        self.next = nil
    }
}

func swapPairs(_ head: ListNode?) -> ListNode? {
    
    guard let h = head else {
        return head;
    }
    
    var current : ListNode? = h;
    
    
    while current != nil {
        
        if let nextVal = current?.next?.val, let val = current?.val {
            current?.val = nextVal
            current?.next?.val = val
        }
        
        current = current?.next?.next;
    }
    return h;
}

func printLinkList(_ head: ListNode?) {
    
    var current = head;
    
    while current != nil {
        print(current?.val as Any);
        current = current?.next;
    }
}

var l1 = ListNode(1);
var l2 = ListNode(2);
var l3 = ListNode(3);
var l4 = ListNode(4);

l1.next = l2;
l2.next = l3;
l3.next = l4;

l1 = swapPairs(l1)!;

printLinkList(l1);


print("Hello, World!")

