//
//  main.swift
//  13
//
//  Created by panjianting on 2020/11/2.
//

import Foundation

func numericValue(_ r : Character) -> Int {
    switch r {
    case "I": return 1
    case "V": return 5
    case "X": return 10
    case "L": return 50
    case "C": return 100
    case "D": return 500
    case "M": return 1000
    default:  return 0
    }
}

// 最佳解：先反向尋找。如果目前val小於上一個的val的話，就扣掉目前的val。
func romanToInt(_ s: String) -> Int {
    
    var ans = 0;
    var pre = 0;
    
    for char in s.reversed() {
        let val = numericValue(char);
        
        ans += (val >= pre ? 1 : -1) * val
        pre = val
        
    }
    
    return ans;
}


func romanToInt_my(_ s: String) -> Int {
    var ans = 0
    var sArray = Array(s);
    sArray.append("0") // 加長一個數，讓他不要out of bounds.
    
    
    
    for i in 0...sArray.count-1 {
        
        let char = sArray[i];
        
        
        switch char {
        
        case "I":
            if sArray[i+1] == "X" || sArray[i+1] == "V"{
                ans -= 1;
            }else{
                ans += 1;
            }
            break;
            
        case "V":
            ans += 5;
            break;
            
        case "X":
            if sArray[i+1] == "L" || sArray[i+1] == "C"{
                ans -= 10;
            }else{
                ans += 10;
            }
            
            break;
            
        case "L":
            ans += 50
            break;
            
        case "C":
            if sArray[i+1] == "D" || sArray[i+1] == "M"{
                ans -= 100;
            }else{
                ans += 100;
            }
            break;
            
        case "D":
            ans += 500;
            break;
            
        case "M":
            ans += 1000;
            break;
            
        default:
            break;
        }
        
        
    }
    
    return ans
}


print(romanToInt("III"))
print(romanToInt("IV"))
print(romanToInt("IX"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))

print("Hello, World!")

