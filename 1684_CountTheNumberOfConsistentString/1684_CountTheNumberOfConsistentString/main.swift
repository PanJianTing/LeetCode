//
//  main.swift
//  1684_CountTheNumberOfConsistentString
//
//  Created by panjianting on 2020/12/17.
//

import Foundation

func countConsistentStrings(_ allowed:String, _ words:[String] ) -> Int {
    
    var ans = 0;
    let allowedSet = Set(allowed.map({$0}))
    
    for word in words {
        let wordSet = Set(word.map({$0}))
        
        if wordSet.isSubset(of: allowedSet) {
            ans += 1
        }
    }
    return ans;
}


print(countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))
print(countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"]))
print(countConsistentStrings("cad", ["cc","acd","b","ba","bac","bad","ac","d"]))
print("Hello, World!")

