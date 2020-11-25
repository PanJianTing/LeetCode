//
//  main.swift
//  118_Pascal's_Triangle
//
//  Created by panjianting on 2020/11/12.
//

import Foundation

func generate(_ numRows: Int) -> [[Int]] {
    
    var ans:[[Int]] = Array(repeating: Array(), count: numRows)
    
    for i in 0..<numRows {
        ans[i] = Array(repeating: 1, count: i+1)
        for j in 0...i {
            
            if i - 1 >= j {
                if j - 1 >= 0 {
                    ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
                }else{
                    ans[i][j] = 0 + ans[i-1][j]
                }
            }else{
                ans[i][j] = 1
            }
            
        }
    }
    
    return ans;
    
}
print("1：\(generate(1))");
print("2：\(generate(2))");
print("3：\(generate(3))");
print("4：\(generate(4))");
print("5：\(generate(5))");
print("6：\(generate(6))");
print("Hello, World!")

