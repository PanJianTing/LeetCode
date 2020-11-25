//
//  main.swift
//  1313_DecompressRun-LengthEncodedList
//
//  Created by panjianting on 2020/11/24.
//

import Foundation

func decompressRLElist(_ nums: [Int]) -> [Int] {
    
    var index = 0
    var ans:[Int] = []
    
    while index < nums.count {
        let freq = nums[index];
        let val = nums[index+1];
        index += 2
        
        for _ in 0..<freq {
            ans.append(val)
        }
        
    }
    
    return ans
}

print(decompressRLElist([1,2,3,4]))
print(decompressRLElist([1,1,2,3]))
print("Hello, World!")

