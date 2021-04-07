
def anagramMappings(A:List[int], B:List[int]) -> List[int]:

	mapdict = {}

	for i in range(0,len(B)):
		mapdict[B[i]] = i

	print(mapdict)

	ansArray = []
	for i in range(0,len(A)):
		ansArray.append(mapdict[A[i]])

	return ansArray 


def anagramMappings_my(A:List[int], B:List[int]) -> List[int]:

	ansArray = []
	for i in xrange(0,len(A)):
		for j in xrange(0,len(B)):
			if A[i] == B[j]:
				ansArray[i] = j

	return ansArray