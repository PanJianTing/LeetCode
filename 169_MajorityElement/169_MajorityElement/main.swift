//
//  main.swift
//  169_MajorityElement
//
//  Created by panjianting on 2020/11/11.
//

import Foundation

// 先假定major的是nums[0]，然後從1至nums.count-1循環，如果出現不等於目前major的數，則減一(類似抵銷掉非major的數)。
// 若count變0了，則更改major，並循環到結束。
// major為出現大於一半的數，故想成區分為major與非major的數
func majorityElement(_ nums: [Int]) -> Int {
    var major = nums[0]
    var count = 1
    
    for i in 1..<nums.count {
        if count == 0 {
            count += 1
            major = nums[i]
        } else {
            if nums[i] == major {
                count += 1
            } else {
                count -= 1
            }
        }
    }
    return major
}


func majorityElement_my(_ nums: [Int]) -> Int {
    
    var dic:[Int:Int] = [:]
    
    for num in nums {
        if let count = dic[num]{
            dic[num] = count + 1
        }else{
            dic[num] = 1
        }
    }
    
    for key in dic.keys {
        
        if let count = dic[key]{
            if count > nums.count/2 {
                return key;
            }
        }
        
    }
    
    return 0;
}


print("Hello, World!")

print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,3,2,2]))
