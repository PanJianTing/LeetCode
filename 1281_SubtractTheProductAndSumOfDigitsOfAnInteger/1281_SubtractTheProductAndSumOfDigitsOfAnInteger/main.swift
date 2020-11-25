//
//  main.swift
//  1281_SubtractTheProductAndSumOfDigitsOfAnInteger
//
//  Created by panjianting on 2020/11/24.
//

import Foundation

func subtractProductAndSum(_ n: Int) -> Int {
    
    var n = n
    var mutilple = 1;
    var sum = 0
    
    while n > 0 {
        let digit = n%10
        n /= 10
        
        mutilple *= digit
        sum += digit
    }
    
    
    return mutilple - sum
}

print(subtractProductAndSum(234))
print(subtractProductAndSum(4421))

print("Hello, World!")

