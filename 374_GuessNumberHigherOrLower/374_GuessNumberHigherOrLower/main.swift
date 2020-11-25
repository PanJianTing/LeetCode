//
//  main.swift
//  374_GuessNumberHigherOrLower
//
//  Created by panjianting on 2020/11/16.
//

import Foundation

var picker = 1

func guess(_ num: Int) -> Int{
    
    if picker < num {
        return -1
    }
    else if picker > num{
        return 1
    }
    else{
        return 0
    }
}

func guessNumber(_ n: Int) -> Int {
    
    var start = 1
    var end = n
    
    while end >= start {
        let num = (start + end)/2
        if guess(num) > 0 {
            
            start = num + 1
        }
        else if guess(num) < 0{
            end = num - 1
        }
        else {
            return num
        }
    }
    return end == start ? end : n
}


print(guessNumber(3));

print("Hello, World!")

