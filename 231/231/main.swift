//
//  main.swift
//  231
//
//  Created by panjianting on 2020/11/9.
//

import Foundation

func isPowerOfTwo(_ n: Int) -> Bool {
    
    guard n >= 0 else {
        return false
    }
    
    guard n != 1 else {
        return true;
    }
    
    var val = 1;
    
    while val < n  {
        val *= 2;
        if val == n {
            return true
        }
    }
    
    
    return false
    
}

print(isPowerOfTwo(1))
print(isPowerOfTwo(2))
print(isPowerOfTwo(3))

print("Hello, World!")

