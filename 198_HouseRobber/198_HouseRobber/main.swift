//
//  main.swift
//  198_HouseRobber
//
//  Created by panjianting on 2020/11/17.
//

import Foundation
/*******
 設一個陣列定義為偷盜第N間的最大值，初始全為0，循環nums.count。
 想法：
 若街上只有一間，則我就偷那間
 若街上有兩間，則我都這兩間的最大值。
 若有三間，則我偷nums[0]加偷nums[2]
 若有四間，則偷nums[0~1]的最大值+nums[3]。
 若有五間，則偷nums[0~2]的最大值+nums[4]。
 
 */

func rob(_ nums: [Int]) -> Int {
    guard nums.count != 0 else {
        return 0;
    }
    
    var robMoney:[Int] = Array(repeating: 0, count: nums.count);
    
    for index in 0..<nums.count {
        
        if index == 0 {
            robMoney[0] = nums[0]
        }else if index == 1{
            robMoney[1] = nums[0] > nums[1] ? nums[0] : nums[1]
        }else{
            robMoney[index] = max(robMoney[index-1], nums[index] + robMoney[index-2])
        }
    }
    
    return robMoney.last!;
}

print(rob([1,2,3,1]))

print(rob([2,7,9,3,1]))

print("Hello, World!")

