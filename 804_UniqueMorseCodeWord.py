def uniqueMorseRepresentations(words:List[str]) -> int:

	arr = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
	myset = set()

	for word in words:
		string = ""
		for char in word:
			string = string + (arr[ord(char)-97])
		myset.add(string)

	return len(myset);


def uniqueMorseRepresentations_best(words: List[str]) -> int:
    
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    d = {}
    for key, value in zip(letters, codes):
        d[key] = value
    outputs = []
    for w in words:
        output = "".join(d[c] for c in w) 
        if output not in outputs:
            outputs.append(output)
    return(len(outputs))

print(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))