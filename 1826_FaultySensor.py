class Solution:
    def badSensor(self, sensor1: list[int], sensor2: list[int]) -> int:

        index1 = 0
        index2 = 0

        while index1 < len(sensor1):
            if sensor1[index1] != sensor2[index2]:
                print(sensor1[index1+1:], sensor2[index2:-1])
                if sensor1[index1+1:] == sensor2[index2:-1] and sensor1[index1:-1] == sensor2[index2+1:]:
                    return -1
                elif sensor1[index1+1:] == sensor2[index2:-1]:
                    return 2
                elif sensor1[index1:-1] == sensor2[index2+1:]:
                    return 1
                
            else:
                index1 += 1
                index2 += 1
        return -1



class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        n = len(sensor1)
        for i in range(n):
            if sensor1[i] != sensor2[i]: # find point at which the sensors differ
                break
        j = k = i # init two pointers
        while j < n-1 and sensor1[j] == sensor2[j+1]: # find to what point sensor1 data is shifted
            j += 1
        while k < n-1 and sensor1[k+1] == sensor2[k]: # find to what point sensor2 data is shifted
            k += 1
        # a sensor is faulty if the ptr reaches end of arr
        # if both reach end of arr, it's impossible to tell
        return -1 if k == n-1 and j == n-1 else 1 if j == n-1 else 2
        