class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date = date.split('-')
        ans = []

        for d in date:
            cnt = int(d)
            temp = []
            
            while cnt > 0:
                temp.append(str(cnt%2))
                cnt >>= 1
            
            ans.append(''.join(temp[::-1]))
        return '-'.join(ans)
