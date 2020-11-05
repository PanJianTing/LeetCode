//
//  main.swift
//  NovW1_3
//
//  Created by panjianting on 2020/11/4.
//

import Foundation


func maxPower(_ s: String) -> Int {
    var now = "";
    var ans = 0;
    var count = 0;
    
    for char in s {
        let charStr = String(char)
        if now != charStr {
            now = charStr;
            count = 1;
        }else{
            count += 1;
        }
        
        if count > ans {
            ans = count;
        }
    }
    return ans
}

print(maxPower("leetcode"))
print(maxPower("abbcccddddeeeeedcba"))
print(maxPower("triplepillooooow"))
print(maxPower("hooraaaaaaaaaaay"))
print(maxPower("tourist"))

print("Hello, World!")

