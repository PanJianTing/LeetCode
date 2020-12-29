//
//  main.swift
//  1688_CountOfMatchesInTournament
//
//  Created by panjianting on 2020/12/21.
//

import Foundation

func numberOfMatches(_ n:Int) -> Int {
    
    var n = n
    var matches = 0
    
    while n > 1 {
        if n % 2 == 0 {
            matches += n/2
            n = n - n/2
        }else{
            matches += ( n - 1 ) / 2 + 1
            n = n - ((n-1)/2+1)
        }
    }
    return matches
}

print(numberOfMatches(7))
print(numberOfMatches(14))
print("Hello, World!")

