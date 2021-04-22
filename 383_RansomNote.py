class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        nMap = collections.Counter(ransomNote)
        
        for letter in nMap:
            if letter not in magazine:
                return False
            elif nMap[letter] > magazine.count(letter):
                return False
        return True
    
    def canConstruct_twoMap(self, ransomNote: str, magazine: str) -> bool:
        
        nMap = collections.Counter(ransomNote)
        mMap = collections.Counter(magazine)
        
        for letter in nMap:
            if letter not in mMap:
                return False
            else:
                if nMap[letter] > mMap[letter]:
                    return False
        return True
    
    def canConstruct_my(self, ransomNote: str, magazine: str) -> bool:
        
        ransomMap = {}
        magazineMap = {}
        
        for c in ransomNote:
            if c in ransomMap:
                ransomMap[c] += 1
            else:
                ransomMap[c] = 1
                
        for c in magazine:
            if c in magazineMap:
                magazineMap[c] += 1
            else:
                magazineMap[c] = 1
        
        for key in ransomMap.keys():
            if key not in magazineMap:
                return False
            
            ransomCount = ransomMap[key]
            magazineCount = magazineMap[key]
            
            if ransomCount > magazineCount:
                return False
        return True


print("Hello World!")