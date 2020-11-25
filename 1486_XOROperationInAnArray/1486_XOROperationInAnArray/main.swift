//
//  main.swift
//  1486_XOROperationInAnArray
//
//  Created by panjianting on 2020/11/25.
//

import Foundation

func xorOperation(_ n: Int, _ start: Int) -> Int {
    
    var ans = 0;
    
    for i in 0..<n {
        ans ^= start + 2 * i
    }
    
    return ans
}

print(xorOperation(5, 0))
print(xorOperation(4, 3))
print(xorOperation(1, 7))
print(xorOperation(10, 5))
print("Hello, World!")

