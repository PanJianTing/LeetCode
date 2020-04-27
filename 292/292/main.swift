//
//  main.swift
//  292
//
//  Created by panjianting on 2020/4/27.
//  Copyright © 2020 panjianting. All rights reserved.
//

import Foundation

func canWinNim(_ n: Int) -> Bool {
    
    if n <= 3{
        return true
    }
    
    let times = n/3;
    let last = n-times*3;
    
    if times%2 == 1{
        if last > 1{
            return true;
        }
        return false;
    }else{
        return true;
    }
}

print(canWinNim(4));
print(canWinNim(5));


