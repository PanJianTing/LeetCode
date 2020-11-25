//
//  main.swift
//  1295_FindNumbersWithEvenNumberOfDigits
//
//  Created by panjianting on 2020/11/17.
//

import Foundation


func findNumbers(_ nums: [Int]) -> Int {
    var ans = 0;
    var string = ""
    nums.forEach { (count) in
        string = String(count)
        if string.count % 2 == 0 {
            ans += 1
        }
    }
    return ans
}

print(findNumbers([12,345,2,6,7896]))
print(findNumbers([555,901,482,1771]))
print("Hello, World!")

