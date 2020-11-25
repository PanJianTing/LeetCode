//
//  main.swift
//  171
//
//  Created by panjianting on 2020/11/10.
//

import Foundation

func titleToNumber(_ s: String) -> Int {
    
    var ans = 0;
    var index = 0;
    
    for char in s.reversed() {
        
        if let ascii = char.asciiValue{
            let count = Int(ascii-65+1);
            ans += Int(pow(26.0, Double(index))) * count
        }
        index += 1;
        
    }
    return ans;
}


print(titleToNumber("A"))
print(titleToNumber("AA"))
print(titleToNumber("AB"))
print(titleToNumber("ZY"))
//print(titleToNumber("ANR"))

print("Hello, World!")

