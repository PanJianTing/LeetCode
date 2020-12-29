//
//  main.swift
//  1266_MinimumTimeVistingAllPoints
//
//  Created by panjianting on 2020/12/21.
//

import Foundation
func minTimeToVisitAllPoints(_ points:[[Int]]) -> Int {
    var dis = 0
    
    
    for i in 0..<points.count-1 {
        let p1 = points[i]
        let p2 = points[i+1]
        
        let px = abs(p1[0] - p2[0])
        let py = abs(p1[1] - p2[1])
        dis += max(px, py)
    }
    
    return dis
}


print(minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
print(minTimeToVisitAllPoints([[3,2],[-2,2]]))
print("Hello, World!")

