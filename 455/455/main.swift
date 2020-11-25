//
//  main.swift
//  455
//
//  Created by panjianting on 2020/11/9.
//

import Foundation

func findContentChildren(_ g: [Int], _ s: [Int]) -> Int {
    
    var child = 0
    var s = s.sorted()
    let g = g.sorted()

    for greedFactor in g {
        for indexCookie in 0..<s.count {
            if greedFactor <= s[indexCookie] {
                child += 1
                s.removeSubrange(0...indexCookie)
                break;
            }
        }
    }
    return child
}

print(findContentChildren([1,2,3], [1,1]))
print(findContentChildren([1,2], [1,2,3]))


print("Hello, World!")

