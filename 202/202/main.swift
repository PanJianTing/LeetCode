//
//  main.swift
//  202
//
//  Created by panjianting on 2020/11/4.
//

import Foundation

func isHappy(_ n: Int) -> Bool {
    
    var isHaveArray:[Int] = [];
    var now = n
    
    while true {
        
        var plus = 0;
        while true {
            let digit = now%10;
            plus += digit * digit;
            now /= 10;
            if now == 0 {
                break;
            }
        }
        
        if plus == 1 {
            return true
        }
        
        for count in isHaveArray {
            if plus == count {
                return false
            }
        }
        
        isHaveArray.append(plus);
        now = plus
    }
}

print(isHappy(19))

print("Hello, World!")

