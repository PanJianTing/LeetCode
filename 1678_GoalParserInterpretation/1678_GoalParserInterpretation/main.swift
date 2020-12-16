//
//  main.swift
//  1678_GoalParserInterpretation
//
//  Created by panjianting on 2020/12/16.
//

import Foundation

//func interpret(_ command : String) -> String {
//
//    let commandAry = Array(command);
//    var str = "";
//    var i = 0;
//
//    while i < commandAry.count {
//        if commandAry[i] == "G" {
//            str.append("G");
//        }else if commandAry[i] == "("{
//            if commandAry[i+1] == "a" {
//                str.append("al");
//                i += 3
//            }else if commandAry[i+1] == ")"{
//                str.append("o");
//                i += 1;
//            }
//        }
//        i += 1
//    }
//
//    return str;
//
//}


func interpret(_ command : String) -> String {
    
    var str = "";
    var isO = false;
    
    for c in command {
        if c == "G" {
            str.append("G");
        }
        else if c == "(" {
            isO = true
        }
        else if c == "a" {
            str.append("al")
            isO = false
        }else if c == ")" {
            if isO {
                str.append("o")
                isO = false
            }
            
        }
    }
    
    return str;
    
}

print(interpret("G()()()()(al)"));
print(interpret("(al)G(al)()()G"));
print("Hello, World!")

