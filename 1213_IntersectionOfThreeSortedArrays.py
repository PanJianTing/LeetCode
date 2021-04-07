def arraysIntersection(arr1: List[int], arr2: List[int], arr3:List[int]) -> List[int]:
	set1 = set(arr1)
	set2 = set(arr2)
	set3 = set(arr3)

	return sorted(List(set1.intersetction(set2).intersetction(set3)))



def arraysIntersection_my(arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
	a1UnionA2 = []
	for a1 in arr1:
		for a2 in arr2:
			if a1 == a2:
				a1UnionA2.append(a1)


	ansArr = []
	for a1 in ansArr:
		for a3 in arr3:
			if a1 == a3:
				ansArr.append(a3)

	return ansArr