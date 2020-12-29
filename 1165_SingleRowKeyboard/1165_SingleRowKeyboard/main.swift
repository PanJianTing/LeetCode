//
//  main.swift
//  1165_SingleRowKeyboard
//
//  Created by panjianting on 2020/12/17.
//

import Foundation

func calculateTime(_ keyboard:String, _ word:String) -> Int {
    
    var time = 0;
    var now = 0;
    var keyboardDic = [Character:Int]()
    
    var i = 0
    for c in keyboard {
        keyboardDic[c] = i
        i += 1
    }
    
    for wc in word {
        let keyCount = keyboardDic[wc] ?? 0;
        time += abs(keyCount-now)
        now = keyCount;
    }
    return time
}

func calculateTime_my(_ keyboard:String, _ word:String) -> Int {
    
    var time = 0;
    var now = 0;
    let keyboard = Array(keyboard);
    
    for wc in word {
        for i in 0..<keyboard.count {
            let c = keyboard[i]
            
            if wc == c {
                time += abs((i-now))
                now = i
            }
            
        }
    }
    return time
}

print(calculateTime("abcdefghijklmnopqrstuvwxyz", "cba"))
print(calculateTime("pqrstuvwxyzabcdefghijklmno", "leetcode"))

print("Hello, World!")

