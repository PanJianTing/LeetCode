//
//  main.swift
//  1365_HowManyNumbersAreSmallerThanTheCurrentNumber
//
//  Created by panjianting on 2020/11/23.
//

import Foundation

func smallerNumbersThanCurrent(_ nums: [Int]) -> [Int] {
    let MAX = 101
    var Counter = Array(repeating: 0, count: MAX + 1)
    for Num in nums {
        Counter[Num] += 1
    }
    
    var ElementCount = 0
    var SmallerCount = Array(repeating: 0, count: MAX + 1)
    for I in 1...MAX {
        ElementCount += Counter[I - 1]
        SmallerCount[I] = ElementCount
    }
    
    var Result = Array(repeating: 0, count: nums.count)
    for I in 0..<nums.count {
        Result[I] = SmallerCount[nums[I]]
    }
    
    return Result
}

func smallerNumbersThanCurrent_my(_ nums: [Int]) -> [Int] {
    
    var ans:[Int] = []
    
    for current in nums {
        var count = 0
        for num in nums {
            if num < current {
                count += 1
            }
        }
        ans.append(count)
    }
    return ans
}

print(smallerNumbersThanCurrent([8,1,2,2,3]))
print(smallerNumbersThanCurrent([6,5,4,8]))
print(smallerNumbersThanCurrent([7,7,7,7]))


print("Hello, World!")

