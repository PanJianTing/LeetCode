//
//  main.swift
//  762. Prime Number of Set Bits in Binary Representation
//
//  Created by panjianting on 2020/4/21.
//  Copyright © 2020 panjianting. All rights reserved.
//

/*
題目：Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.(Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)
 
解法：
 1. 先找出轉二進制後，1的數量(getBitCount)
 2. 檢查是否為質數 (checkPrime) <- 好的解法為 R <= 10^6 < 2^20 所以最多就20個1，故可以寫固定的數值回傳。
*/



import Foundation

func getBitCount(_ integer : Int) -> Int {
    
    var ans : Int = 0;
    var index = integer
    
    while index != 0 {
        if index == 1{
            ans += 1
            index = 0;
        }else{
            if index % 2 == 1{
                ans += 1
            }
            index = index / 2;
        }
    }
    return ans;
}

func checkPrime(_ integet :Int) -> Bool{
    
    guard integet != 1 else {
        return false
    }
    
    if integet == 2 {
        return true
    }
    
    for index in 2..<integet {
        if integet % index == 0{
            return false
        }
    }
    
    return true;
}

func countPrimeSetBits(_ L: Int, _ R: Int) -> Int {
    
    var ans = 0;
    for index in L...R{
        
        if checkPrime(getBitCount(index)){
            ans += 1;
        }
        
        
    }
    return ans;
}

print(countPrimeSetBits(6, 10));
print(countPrimeSetBits(10, 15));

