//
//  main.swift
//  1389_CreateTargetInTheGivenOrder
//
//  Created by panjianting on 2020/11/25.
//

import Foundation


func createTargetArray(_ nums: [Int], _ index: [Int]) -> [Int] {
    
    var target:[Int] = Array()
    
    for i in 0..<index.count  {
        target.insert(nums[i], at: index[i])
    }
    
    return target
}

print(createTargetArray([0,1,2,3,4], [0,1,2,2,1]))
print(createTargetArray([1,2,3,4,0], [0,1,2,3,0]))
print("Hello, World!")

