//
//  main.swift
//  9
//
//  Created by panjianting on 2020/10/30.
//

import Foundation


func isPalindrome(_ x: Int) -> Bool {
    
    if x < 0 {
        return false;
    }
    
    if x < 10 {
        return true
    }
    
    var countArr:[Int] = [];
    var count = x;
    while count > 0 {
        countArr.append(count%(10))
        count = count / 10;
    }
    
    for i in 0...countArr.count-1 {
        let reverse = countArr.count - 1 - i;
        if countArr[i] != countArr[reverse] {
            return false;
        }
        if reverse <= i {
            break;
        }
    }
    
    print(countArr);
    
    return true;
        
}

print(isPalindrome(-100));

print("Hello, World!")

