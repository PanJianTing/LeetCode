//
//  main.swift
//  1534_CountGoodTriplets
//
//  Created by panjianting on 2020/12/29.
//

import Foundation

func countGoodTriplets(_ arr: [Int], _ a: Int, _ b: Int, _ c:Int) -> Int {
    var count = 0
    for i in 0..<arr.count {
        for j in i+1..<arr.count where abs(arr[i] - arr[j]) <= a {
            for k in j+1..<arr.count where abs(arr[j] - arr[k]) <= b {
                if abs(arr[i] - arr[k]) <= c {
                    count += 1
                }
            }
        }
    }
    return count;
}

func countGoodTriplets_my(_ arr: [Int], _ a: Int, _ b: Int, _ c:Int) -> Int {
    
    var count = 0
    
    for i in 0..<arr.count {
        for j in i+1..<arr.count {
            for k in j+1..<arr.count {
                if abs(arr[i] - arr[j]) <= a && abs(arr[j] - arr[k]) <= b && abs(arr[i] - arr[k]) <= c {
                    count += 1
                }
            }
        }
    }
    
    
    return count;
}

print(countGoodTriplets([3,0,1,1,9,7], 7, 2, 3))
print("Hello, World!")

