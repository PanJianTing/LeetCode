//
//  main.swift
//  20
//
//  Created by panjianting on 2020/11/3.
//

import Foundation

class Node{
    let val:String
    var next:Node?
    
    init() {
        self.val = ""
        self.next = nil
    }
    
    init(_ val:String) {
        self.val = val
        self.next = nil
    }
}

class Stack {
    var now:Node?
    
    init() {
        self.now = nil
    }
    
    func push(_ node : Node) {
        node.next = self.now;
        self.now = node;
    }
    
    func pop() -> Node? {
        let returnNode = now;
        now = now?.next
        return returnNode;
    }
}

func isValid(_ s: String) -> Bool {
    
    guard s.count > 1 else {
        return false;
    }
    
    let stack = Stack();
    
    for char in s {
        if char == "[" || char == "(" || char == "{" {
            stack.push(Node(String(char)))
        }
        else if char == "]" {
            if let node = stack.pop(){
                if node.val != "[" {
                    return false;
                }
            }else{
                stack.push(Node(String(char)))
            }
        }
        else if char == ")" {
            if let node = stack.pop(){
                if node.val != "(" {
                    return false;
                }
            }else{
                stack.push(Node(String(char)))
            }
        }
        else if char == "}" {
            if let node = stack.pop(){
                if node.val != "{" {
                    return false;
                }
            }else{
                stack.push(Node(String(char)))
            }
        }
    }
    
    return (stack.pop() != nil) ? false : true;
}


//print(isValid("()"))
//print(isValid("()[]{}"))
//print(isValid("(]"))
//print(isValid("([)]"))
//print(isValid("{[]}"))
//print(isValid("{"))
print(isValid("]"))

print("Hello, World!")

