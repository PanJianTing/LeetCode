//
//  main.swift
//  242_ValidAnagram
//
//  Created by panjianting on 2020/11/12.
//

import Foundation

// 生一個26個字母的陣列，轉asciiCode。
// 遍歷s，把相同的字母數量加一。
// 遍歷t，把相同的字母數量減一。
// 遍歷字母陣列，遇到!=0的話，就是false。
func isAnagram(_ s: String, _ t: String) -> Bool {
    if s.count != t.count {
        return false
    }
    var stat = Array(repeating: 0, count: 26)
    let firstIndex = Int(Character("a").asciiValue ?? 0)
    for code in s.unicodeScalars {
        stat[Int(code.value) - firstIndex] += 1
    }
    for code in t.unicodeScalars {
        stat[Int(code.value) - firstIndex] -= 1
    }
    for n in stat {
        if n != 0 {
            return false
        }
    }
    
    return true
}

func isAnagram_MY(_ s: String, _ t: String) -> Bool {
    
    var sDic:[Character:Int] = [:]
    var tDic:[Character:Int] = [:]
    
    for sChar in s {
        if let sCount = sDic[sChar]{
            sDic[sChar] = sCount + 1
        }else{
            sDic[sChar] = 1
        }
    }
    
    for tChar in t {
        if let tCount = tDic[tChar]{
            tDic[tChar] = tCount + 1
        }else{
            tDic[tChar] = 1
        }
    }
    
    if sDic.keys.count == tDic.keys.count {
        for key in sDic.keys {
            if let sCount = sDic[key], let tCount = tDic[key] {
                if sCount != tCount {
                    return false
                }
            }else{
                return false
            }
        }
    } else {
        return false
    }
    
    return true
}

print(isAnagram("anagram","nagaram"));
print(isAnagram("rat","car"));

print("Hello, World!")

