//
//  main.swift
//  1588_SumOfAllOddLengthSubarrays
//
//  Created by panjianting on 2020/12/22.
//

import Foundation

func sumOddLengthSubarrays(_ arr:[Int]) -> Int {
    var sum = 0;
    
    for n in 1...arr.count {
        if n % 2 == 0 {
            continue
        }
        for i in 0...arr.count {
            let last = i+n-1;
            if last >= arr.count {
                break;
            }
            let subarr = arr[i...last];
            
            for count in subarr {
                sum += count;
            }
        }
    }
    return sum;
}

print(sumOddLengthSubarrays([1,4,2,5,3]))
print(sumOddLengthSubarrays([1,2]))
print(sumOddLengthSubarrays([10,11,12]))

print("Hello, World!")
