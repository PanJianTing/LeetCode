//
//  main.swift
//  3. Longest Substring Without Repeating Characters
//
//  Created by panjianting on 2020/4/27.
//  Copyright © 2020 panjianting. All rights reserved.
//
//  Given a string, find the length of the longest substring without repeating characters.
//

/*
 * 我的解法，用一個array來
 */


import Foundation

func lengthOfLongestSubstring(_ s: String) -> Int {
    
    let strArr = Array(s)
    var cache: [Character : Int] = [:]
    var startIndex = 0
    var maxLen = 0
    
    for j in 0..<strArr.count {
        if let index = cache.updateValue(j, forKey: strArr[j]) {
            startIndex = max(index + 1, startIndex)
        }
        maxLen = max(maxLen, j - startIndex + 1)
    }
    return maxLen
}

func mylengthOfLongestSubstring(_ s: String) -> Int {
    
    var ansStr:[String] = [];
    var ans = 0;
    
    
    for c in s{
        let index = ansStr.firstIndex(of: String(c));
        
        if let i = index{
            ansStr.removeSubrange(0...i);
        }
        ansStr.append(String(c))
        
        if ansStr.count > ans{
            ans = ansStr.count;
        }
    }
    
    
    return ans;
}


print(lengthOfLongestSubstring("abcabcbb"));
print(lengthOfLongestSubstring("bbbbb"));
print(lengthOfLongestSubstring("pwwkew"));
print(lengthOfLongestSubstring("dvdf"));
print(lengthOfLongestSubstring("anviaj"));



