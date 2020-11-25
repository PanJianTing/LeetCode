//
//  main.swift
//  167
//
//  Created by panjianting on 2020/11/9.
//

import Foundation

// 頭尾相加：如果目前sum>target，則往前找一個。如果目前sum < target，則往後找一個直到兩邊慢慢逼近。
func twoSum(_ numbers: [Int], _ target: Int) -> [Int] {

    var i = 0;
    var j = numbers.count - 1;
    
    while i<j {
        
        let now = numbers[i] + numbers[j]
        if now > target {
            j -= 1;
        }
        else if now < target {
            i += 1
        }else{
            return [i+1, j+1];
        }
    }
    
    return [];
}


func twoSum_my(_ numbers: [Int], _ target: Int) -> [Int] {
    
//    var ans:[Int] = [];
//    var numbers = numbers;
    
    for i in 0..<numbers.count {
        for j in i+1..<numbers.count {
            if numbers[i]+numbers[j] == target {
                return [i+1,j+1]
            }
        }
    }
    
    return [];
}


print(twoSum([2,7,11,15], 9));
print(twoSum([2,3,4], 6));
print(twoSum([-1, 0], -1));

print("Hello, World!")

