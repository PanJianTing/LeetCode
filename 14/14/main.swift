//
//  main.swift
//  14
//
//  Created by panjianting on 2020/11/2.
//

import Foundation

// 找最小的，一個一個比，如果沒有prefix就一個一個字元減少。
func longestCommonPrefix(_ strs: [String]) -> String {
        var s: String?
        var len = Int.max
        
        for str in strs {
            if str.count < len {
                len = str.count
                s = str
            }
        }
        
        if var s = s {
            var endIndex = s.endIndex
            for str in strs {
                while !s.isEmpty && !str.hasPrefix(s) {
                    endIndex = s.index(before: endIndex)
                    s = String(s[..<endIndex]) // substring to endIndex
                }
            }
            return s
        } else {
            return ""
        }
    }

// 先以長度排序，最短跟最長的比，找相同的就好。
//func longestCommonPrefix(_ strs: [String]) -> String {
//    guard strs.count > 0 else {
//        return "";
//    }
//
//    guard strs.count > 1 else {
//        return strs[0];
//    }
//
//
//    let sorted = strs.sorted();
//    let str1 = sorted.first!;
//    let str2 = sorted.last!;
//
//    var prefix = ""
//
//    for i in 1...min(str1.count, str2.count) {
//
//        if str1.prefix(i) == str2.prefix(i) {
//            prefix = String(str1.prefix(i))
//        }else{
//            break;
//        }
//
//    }
//    return prefix;
//
//}


// 以第一個為主，一個一個去比
func longestCommonPrefix_my(_ strs: [String]) -> String {
    guard strs.count > 0 else {
        return ""
    }
    
    var ans = strs[0];
    
    for i in 1..<strs.count {
        
        let string = strs[i];
        
        let miniCount = min(ans.count, string.count)
        
        var temp = "";
        
        for idx in 0...miniCount {
            
            if ans.prefix(idx) == string.prefix(idx) {
                temp = String(ans.prefix(idx));
            }
        }
        
        ans = temp;
        if ans == "" {
            return "";
        }
        
    }
    
    return ans;
}

print(longestCommonPrefix(["flower","flow","fl"]));
print(longestCommonPrefix(["dog","racecar","car"]));
print(longestCommonPrefix([]));



print("Hello, World!")

