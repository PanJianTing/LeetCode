//
//  main.swift
//  342
//
//  Created by panjianting on 2020/11/10.
//

import Foundation

func isPowerOfFour(_ num: Int) -> Bool {
    
    var count = 4
    if num == 1 {
        return true;
    }
    
    while count <= num {
        
        if count == num {
            return true
        }
        
        count *= 4;
        
    }
    
    return false
}

print(isPowerOfFour(0))
print(isPowerOfFour(1))
print(isPowerOfFour(2))
print(isPowerOfFour(3))
print(isPowerOfFour(4))
print(isPowerOfFour(16))
print(isPowerOfFour(5))

print("Hello, World!")

