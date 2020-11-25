//
//  main.swift
//  263
//
//  Created by panjianting on 2020/11/10.
//

import Foundation


func isUgly(_ num: Int) -> Bool {
    
    guard num > 0 else {
        return false
    }
    
    var num = num
    
    while num > 1 {
        if num%2 == 0 {
            num /= 2
        }
        else if num%3 == 0 {
            num /= 3
        }
        else if num%5 == 0 {
            num /= 5
        } else {
            
            return false
        }
    }
    
    return true
}

print(isUgly(55))
//print(isUgly(8))
//print(isUgly(14))
print("Hello, World!")

