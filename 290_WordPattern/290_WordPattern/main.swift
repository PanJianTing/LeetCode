//
//  main.swift
//  290_WordPattern
//
//  Created by panjianting on 2020/11/11.
//

import Foundation

func wordPattern(_ pattern: String, _ s: String) -> Bool {
    var map_char = [Character: String]()
    var map_word = [String: Character]()
    let words:[String] = s.split(separator: " ").map(String.init)
    
    if words.count != pattern.count { return false }
    
    for i in 0..<words.count {
        let index = pattern.index(pattern.startIndex, offsetBy: i)
        let c = pattern[index]
        let w = words[i]
        
        if !map_char.keys.contains(c) {
            if map_word.keys.contains(w) {
                return false
            } else {
                map_char[c] = w
                map_word[w] = c
            }
        } else {
            let mapped_word = map_char[c]
            if mapped_word != w {
                return false
            }
        }
    }
    return true
}

func wordPattern_P(_ pattern: String, _ s: String) -> Bool {
    
    var charDic = [Character: String]()
    var wordDic = [String: Character]()
    let words:[String] = s.split(separator: " ").map(String.init)
    
    if words.count != pattern.count {
        return false
    }
    
    for i in 0..<words.count {
        
        let char = pattern[i]
        let word = words[i]
        
    }
    
    
    return true;
}

print(wordPattern("abba", "dog cat cat dog"))
//print(wordPattern("abba", "dog cat cat fish"))
//print(wordPattern("aaaa", "dog cat cat dog"))
//print(wordPattern("abba", "dog dog dog dog"))

print("Hello, World!")

