class  Solution:
	def minOperations(self, logs: list[str]) -> int:

		main = 0

		for log in logs:
			if log == '../':
				if main == 0:
					main = 0
				else:
					main -= 1
			elif log == './':
				pass
			else:
				main += 1

		return main