//
//  main.swift
//  1656_DesignAnOrderedStream
//
//  Created by panjianting on 2020/11/27.
//

import Foundation

class OrderedStream {

    var index = 0
    var n = 0;
    var array:[String] = []
    
    init(_ n: Int) {
        self.n = n
        self.array = Array(repeating: "", count: n)
        
    }
    
    func insert(_ id: Int, _ value: String) -> [String] {
        var chunkStrs:[String] = [];
        
        self.array[id-1] = value
        
        while self.index < self.n {
            
            if self.array[self.index] != ""{
                chunkStrs.append(self.array[self.index])
                self.index += 1
            }else{
                break
            }
        }
        
        return chunkStrs
    }
}


let orderStream = OrderedStream(5);
print(orderStream.insert(3, "ccccc"))
print(orderStream.insert(1, "aaaaa"))
print(orderStream.insert(2, "bbbbb"))
print(orderStream.insert(5, "eeeee"))
print(orderStream.insert(4, "ddddd"))

print("Hello, World!")

