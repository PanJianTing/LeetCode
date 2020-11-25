//
//  main.swift
//  204
//
//  Created by panjianting on 2020/11/6.
//

import Foundation

// 從2開始算，倍數也不會是質數。
// 一個數如果不能從2開始到自身的開根號範圍內被整數整除，則他就是質數
func countPrimes(_ n: Int) -> Int {
    
    guard n > 2 else {
        return 0;
    }
    
    var ans = 0;
    var primes = Array(repeating: true, count: n);
    var i = 2;
    while i * i < n {
        if primes[i] {
            var j = i
            while j * i < n {
                primes[j * i] = false
                j += 1
            }
        }
        i += 1
    }
    
    for k in 2..<primes.count {
        if primes[k] == true {
            ans += 1
        }
    }
    
    
    return ans;
}

print("Hello, World!")

