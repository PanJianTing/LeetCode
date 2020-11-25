//
//  main.swift
//  268
//
//  Created by panjianting on 2020/11/10.
//

import Foundation

// 整個完整的陣列跟index XOR起來必須是0。
func missingNumber(_ nums: [Int]) -> Int {
    var result: Int = nums.count
    for i in 0..<nums.count {
        result = result ^ i ^ nums[i]
        print(result)
    }
    return result
}

func missingNumber_my(_ nums: [Int]) -> Int {
    
    var sum = (nums.count + 1) * nums.count / 2
    
    for num in nums {
        sum -= num;
    }
    
    return sum
}
print("Start")
print(missingNumber([3,0,1]))
print("End")
print("Start")
print(missingNumber([0,1]))
print("End")
print("Start")
print(missingNumber([9,6,4,2,3,5,7,0,1]))
print("End")
print("Start")
print(missingNumber([0]))
print("End")


print("Hello, World!")

