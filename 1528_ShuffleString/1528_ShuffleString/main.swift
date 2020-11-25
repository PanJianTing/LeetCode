//
//  main.swift
//  1528_ShuffleString
//
//  Created by panjianting on 2020/11/24.
//

import Foundation


func restoreString(_ s: String, _ indices: [Int]) -> String {
    
    var ans:[Character] = Array(repeating: Character("a"), count: s.count)
    let charArray = Array(s)
    
    
    for index in 0..<indices.count {
        let position = indices[index]
        ans[position] = charArray[index]
    }
    
    return String(ans)
}

print(restoreString("codeleet", [4,5,6,7,0,2,1,3]))
print(restoreString("abc", [0,1,2]))
print(restoreString("aiohn", [3,1,4,2,0]))
print(restoreString("aaiougrt", [4,0,2,6,7,3,1,5]))
print(restoreString("art", [1,0,2]))

print("Hello, World!")

