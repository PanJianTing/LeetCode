//
//  main.swift
//  1304.Find N Unique Integers Sum up to Zero

//  Given an integer n, return any array containing n unique integers such that they add up to 0.

//  Created by panjianting on 2020/5/8.
//  Copyright © 2020 panjianting. All rights reserved.
//

/*
 * 2020/05/08 PanJianTing
 * 我的解法：從0依序塞N-1個數，第N個數為塞值得和的負數
 * 最快解：先判斷是否為奇數。若為奇數，則先塞0，之後就用n/2的方式依序塞-1,1 -2,2...這樣
 */


import Foundation

func sumZero(_ n: Int) -> [Int] {
    if n <= 1 {
        return [0]
    }
    var result = [Int](repeating: 0, count: n)
    var current = 0
    if n % 2 != 0 {
        result[current] = 0
        current += 1
    }
    
    for i in (1...n/2) {
        result[current] = i
        current += 1
        result[current] = -i
        current += 1
    }
    return result
}


func mysumZero(_ n: Int) -> [Int] {

    guard n != 1 else {
        return [0];
    }
    guard n != 2 else {
        return [1,-1];
    }
    
    var ans:[Int] = [];
    var sum = 0;
    
    for i in 0..<n-1{
        ans.append(i);
        sum+=i;
    }
    ans.append(-1 * sum);
    
    
    return n == 1 ? [0]:ans;
}

print(sumZero(1));
print(sumZero(2));
print(sumZero(3));
print(sumZero(4));
print(sumZero(5));
