//
//  main.swift
//  1480_RunningSumOf1DArray
//
//  Created by panjianting on 2020/11/17.
//

import Foundation

func runningSum(_ nums: [Int]) -> [Int] {
    var nums = nums
    for i in 0..<nums.count {
        if i == 0 {
            continue;
        }
        nums[i] = nums[i] + nums[i-1];
    }
    return nums;
}

print(runningSum([1,2,3,4]))
print(runningSum([1,1,1,1,1]))
print(runningSum([3,1,2,10,1]))


print("Hello, World!")

