//
//  main.swift
//  973. K Closest Points to Origin
//
//  Created by panjianting on 2020/4/21.
//  Copyright © 2020 panjianting. All rights reserved.
//

/*
 我的解法：
    先算距離，存成Map [distance:[[Int]]]
    在用distance做排序
    然後根據K回傳
 最佳解：
    直接做陣列來排序，由小到大。再回傳前幾個。
 */



import Foundation

func kClosest(_ points: [[Int]], _ K: Int) -> [[Int]] {
    let sortedPoint = points.sorted {
        ($0[0] * $0[0] + $0[1] * $0[1]) < ($1[0] * $1[0] + $1[1] * $1[1])
    }
    
    return Array(sortedPoint.prefix(K))
}


func mykClosest(_ points: [[Int]], _ K: Int) -> [[Int]] {
    
    var disPointsDic:[Int : [[Int]]] = [:]
    var ans:[[Int]] = [];
    
    for point in points{
        let dis = point[0] * point[0] + point[1] * point[1];
        
        if var disPoints = disPointsDic[dis] {
            disPoints.append(point);
            disPointsDic[dis] = disPoints;
        }else{
            let array = [point];
            disPointsDic[dis] = array;
        }
    }
    
    print(disPointsDic);
    
    let sortDisPointsDic = disPointsDic.sorted { (dictionary1, dictionary2) -> Bool in
        
        return dictionary1.0 < dictionary2.0
    }
    
    for disPointsDic in sortDisPointsDic{
        for point in disPointsDic.1{
            ans.append(point)
        }
        if ans.count >= K{
            break;
        }
    }
    
    return ans;
}

print(kClosest([[1,3],[-2,2]], 1));
print(kClosest([[3,3],[5,-1],[-2,4]], 2));
print(kClosest([[-2,10],[-4,-8],[10,7],[-4,-7]], 3));
