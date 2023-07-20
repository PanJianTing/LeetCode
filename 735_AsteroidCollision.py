class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        
        st = []
        for num in asteroids:
            while st and st[-1] > 0 and num < 0:
                if abs(st[-1]) < abs(num):
                    st.pop()
                    continue
                elif abs(st[-1]) == abs(num):
                    st.pop()
                break
            else:
                st.append(num)
        
        return st
    

print(Solution().asteroidCollision([5,10,-5]))
print(Solution().asteroidCollision([8,-8]))
print(Solution().asteroidCollision([10,2,-5]))
