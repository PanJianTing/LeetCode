//
//  main.swift
//  1436_DestinationCity
//
//  Created by panjianting on 2020/11/27.
//

import Foundation

func destCity(_ paths:[[String]]) -> String {
    
    var pathDic:[String:String] = Dictionary(minimumCapacity: paths.count)
    
    for path in paths {
        
        pathDic[path[0]] = path[1]
    }
    
    return pathDic.values.first(where: {
        pathDic[$0] == nil
    })!
    
}

print(destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
print(destCity([["B","C"],["D","B"],["C","A"]]))
print(destCity([["A","Z"]]))

print("Hello, World!")

