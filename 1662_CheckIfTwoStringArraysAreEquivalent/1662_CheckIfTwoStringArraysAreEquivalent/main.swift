//
//  main.swift
//  1662_CheckIfTwoStringArraysAreEquivalent
//
//  Created by panjianting on 2020/11/27.
//

import Foundation

func arrayStringsAreEqual(_ word1: [String], _ word2: [String]) -> Bool {
    
    return word1.reduce("", +) == word2.reduce("", +)
}

print(arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))
print("Hello, World!")

