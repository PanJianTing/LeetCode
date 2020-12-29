//
//  main.swift
//  1704_DetermineIfStringHalvesAreAlike
//
//  Created by panjianting on 2020/12/29.
//

import Foundation


func halvesAreAlike(_ s: String) -> Bool {
    
    let chars = Array(s);
    
    let half = chars.count/2;
    
//    let vowels:Array<Character> = ["a","e","u","i","o","A","E","U","I","O"];
    
    let vowels:Set<Character> = ["a","e","u","i","o","A","E","U","I","O"];
    
    
    var count = 0;
    
    for i in 0..<half {
        if vowels.contains(chars[i]) {
            count += 1;
        }
    }
    
    for i in half..<chars.count {
        if vowels.contains(chars[i]) {
            count -= 1;
        }
    }
    
    return count == 0 ? true:false;
}


print(halvesAreAlike("Book"))
print(halvesAreAlike("MerryChristmas"))
print(halvesAreAlike("AbCdEfGh"))
print("Hello, World!")

