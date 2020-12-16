//
//  main.swift
//  1221_SplitAStringInBlancedStrings
//
//  Created by panjianting on 2020/11/26.
//

import Foundation

func balancedStringSplit(_ s: String) -> Int {
    
    var balance = 0
    var ans = 0

    for char in s {
        if char == "R" {
            balance += 1
        }else{
            balance -= 1
        }
        
        if balance == 0 {
            ans += 1
        }
    }
    
    
    return ans;
}

print(balancedStringSplit("RLRRLLRLRL"))
print(balancedStringSplit("RLLLLRRRLR"))
print(balancedStringSplit("LLLLRRRR"))
print(balancedStringSplit("RLRRRLLRLL"))
print("Hello, World!")

