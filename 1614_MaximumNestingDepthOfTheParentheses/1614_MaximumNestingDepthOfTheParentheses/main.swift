//
//  main.swift
//  1614_MaximumNestingDepthOfTheParentheses
//
//  Created by panjianting on 2020/11/25.
//

import Foundation

func maxDepth(_ s: String) -> Int {
    
    var count = 0
    var ans = 0;
    
    for char in s {
        if char == "(" {
            count += 1
            ans = max(ans, count)
        }else if char == ")"{
            count -= 1
        }
    }
    
    return ans
    
}


print(maxDepth("(1+(2*3)+((8)/4))+1"))
print(maxDepth("(1)+((2))+(((3)))"))
print(maxDepth("1+(2*3)/(2-1)"))
print(maxDepth("1"))
print("Hello, World!")

