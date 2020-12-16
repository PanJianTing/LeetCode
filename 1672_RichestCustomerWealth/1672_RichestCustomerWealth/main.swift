//
//  main.swift
//  1672_RichestCustomerWealth
//
//  Created by panjianting on 2020/11/30.
//

import Foundation

func maximumWealth(_ accounts: [[Int]]) -> Int {
    
    var maxAmount = 0
    
    for account in accounts {
        var sum = 0
        for money in account {
            sum += money
        }
        if maxAmount < sum {
            maxAmount = sum
        }
    }
    
    return maxAmount
    
}

print("Hello, World!")

