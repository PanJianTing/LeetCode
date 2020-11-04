//
//  main.swift
//  58
//
//  Created by panjianting on 2020/11/3.
//

import Foundation

func lengthOfLastWord(_ s: String) -> Int {
    
    let array = s.split(separator: " ")
    
//    array.last?.count
    
    if let string = array.last {
        return string.count
    }
    return 0;
}


print(lengthOfLastWord("Hello World"));
print(lengthOfLastWord(""))

print("Hello, World!")

