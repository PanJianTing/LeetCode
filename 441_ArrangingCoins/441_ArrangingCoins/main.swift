//
//  main.swift
//  441_ArrangingCoins
//
//  Created by panjianting on 2020/11/16.
//

import Foundation

func arrangeCoins_max(_ n: Int) -> Int {
    // for k : k * (k + 1) / 2 coins
    // max k, where k * (k + 1) <= n
    var left = 0
    var right = n
    var k = 0
    var current = 0
    while left <= right {
        k = left + (right - left) / 2
        current = k * (k + 1) / 2
        if current == n {
            return k
        }
        if n < current {
            right = k - 1
        } else {
            left = k + 1
        }
    }
    return right
}

// find x is range x^2-x <= 2n <= x^2+x
func arrangeCoins(_ n: Int) -> Int {

    
    var start = 1;
    var end = n;
    
    while end >= start {
        let x = (end + start)/2
        let left = (x*(x-1)) >> 1
        let right = (x*(x+1)) >> 1
        
        if n >= left && n <= right {
            
            if n == right {
                return x
            }
            
            return x - 1
        }else{
            if n > right {
                start = x + 1;
                
            }
            if n < left {
                end = x - 1;
            }
        }
    }
    
    return end
}

print(arrangeCoins(0))
print(arrangeCoins(1))
print(arrangeCoins(2))
print(arrangeCoins(3))
print(arrangeCoins(4))
print(arrangeCoins(5))
//print(arrangeCoins(8))

print("Hello, World!")

