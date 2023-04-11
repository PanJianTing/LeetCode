class Solution:
	def anagramMappings(A: list[int], B: list[int]) -> list[int]:

		mapdict = {}

		for i in range(0,len(B)):
			mapdict[B[i]] = i

		print(mapdict)

		ansArray = []
		for i in range(0,len(A)):
			ansArray.append(mapdict[A[i]])

		return ansArray 


	def anagramMappings_my(A: list[int], B: list[int]) -> list[int]:

		ansArray = []
		for i in range(0,len(A)):
			for j in range(0,len(B)):
				if A[i] == B[j]:
					ansArray[i] = j

		return ansArray
	

class Solution:
    def anagramMappings(self, nums1: list[int], nums2: list[int]) -> list[int]:
        mapping = {}
        for i, count in enumerate(nums2):
            mapping[count] = i
        
        ans = []
        for count in nums1:
            ans.append(mapping[count])

        return ans