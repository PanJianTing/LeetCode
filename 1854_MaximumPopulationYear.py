class Solution:
	def maximumPopulation(self, logs: list[list[int]]) -> int:
		populationArray = [0] * 101

		for log in logs:
			# 出生年份則加一，死亡年份則減一
			populationArray[log[0] - 1950] += 1
			populationArray[log[1] - 1950] -= 1


		population = 0
		maxPopulation = 0
		result = 0

		for year in range(1950, 2051):
			# 計算今年的人數，加多少或減多少
			temp = population + populationArray[year - 1950]
			if temp > maxPopulation:
				result = year
				maxPopulation = temp
			# 更新最新的人數
			population = temp

		return result


	def maximumPopulation_my(self, logs: list[list[int]]) -> int:
		populationArray = [0] * 101

		for index in range(0, 101):
			year = 1950+index
			for log in logs:
				birth = log[0]
				death = log[1]

				if birth <= year < death:
					populationArray[index] += 1

		maximum = max(populationArray)

		for index in range(0, 101):
			population = populationArray[index]
			if population == maximum:
				return 1950 + index
