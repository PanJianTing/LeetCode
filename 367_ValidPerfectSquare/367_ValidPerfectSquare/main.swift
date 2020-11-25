//
//  main.swift
//  367_ValidPerfectSquare
//
//  Created by panjianting on 2020/11/12.
//

import Foundation

func isPerfectSquare_f(_ num: Int) -> Bool {
    guard num > 1 else { return true }
    var left = 0
    var right = num / 2
    
    while left <= right {
        let mid = (right - left) / 2 + left
        let s = mid * mid
        
        if s == num {
            return true
        } else if s > num {
            right = mid - 1
        } else {
            left = mid + 1
        }
    }
    
    return false
}


func isPerfectSquare(_ num: Int) -> Bool {
    
    var ans = 1;
    
    while ans*ans <= num {
        if ans*ans == num {
            return true
        }
        ans += 1;
    }
    
    return false
}

print(isPerfectSquare(14))
print(isPerfectSquare(16))
print(isPerfectSquare(Int(INT_MAX)))

print("Hello, World!")

