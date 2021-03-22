import copy

class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1, s2 = list(s1), list(s2)
        if s1 == s2:
            return True

        for i in range(len(s2)):
            for j in range(i, len(s2)):
                s = copy.deepcopy(s2)
                s[i], s[j] = s[j], s[i]
                if s == s1:
                    return True
        
        return False
        

class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        for num in range(1, len(edges)+2):
            print(num)
            count = 0
            for edge in edges:
                if num in edge:
                    count += 1
                else:
                    continue
            if count == len(edges)-1:
                return num

class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        for num in edges[0]:
            if num in edges[1]:
                return num

#import numpy as np
class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        while extraStudents:
            cur = [c[1] for c in classes]
            min_idx = np.argmin(cur)
            if classes[min_idx][0] == classes[min_idx][1]:
                classes[min_idx][0] += 1000
                classes[min_idx][1] += 1000
                continue
            else:
                classes[min_idx][0] += 1
                classes[min_idx][1] += 1
                extraStudents -= 1

        return np.mean([c[0]/c[1] for c in classes])


#import numpy as np
class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        while extraStudents:
            cur_pass = np.array([c[0] for c in classes])
            cur_all = np.array([c[1] for c in classes])
            cur_ratio = np.divide(cur_pass, cur_all)
            new_ratio = np.divide(cur_pass+1, cur_all+1)
            idx = np.argmax(new_ratio - cur_ratio)
            classes[idx][0] += 1
            classes[idx][1] += 1
            extraStudents -= 1
        
        return np.divide(np.array([c[0] for c in classes]), np.array([c[1] for c in classes]))

import heapq
class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        target = []
        for c in classes:
            c_pass, c_all = c
            prior = (c_pass+1)/(c_all+1) - c_pass / c_all
            heapq.heappush(target, (prior, c_pass, c_all))

        while extraStudents:
            _, c_pass, c_all = heapq.heappop(target)
            c_pass += 1
            c_all += 1
            prior = (c_pass+1)/(c_all+1) - c_pass / c_all
            heapq.heappush(target, (prior, c_pass, c_all))
            extraStudents -= 1

        return sum([c[0]/c[1] for c in target])/len(target)


import heapq

class Solution:
    def getNumberOfBacklogOrders(self, orders):
        sells, buys = [], []
        ret = 0
        # sells prior is descend
        for element in orders:
            print(element)
            if element[2] == 1:  # sell
                while element[1]:
                    if buys:
                        buy = heapq.heappop(buys)
                        ret -= buy[1]
                        if element[0] <= -buy[0]:  # match
                            if element[1] < buy[1]:
                                buy[1] -= element[1]
                                element[1] = 0
                                heapq.heappush(buys, buy)
                                ret += buy[1]
                            elif element[1] == buy[1]:
                                element[1] = 0
                            else:
                                element[1] -= buy[1]
                                heapq.heappush(sells, element)
                                ret += element[1]
                        else:
                            break
                    else:
                        heapq.heappush(sells, element)
                        ret += element[1]
                        break
            else:  # buy
                while element[1]:
                    if sells:
                        sell = heapq.heappop(sells)
                        ret -= sell[1]
                        if element[0] >= sell[0]:  # match
                            if element[1] < sell[1]:
                                sell[1] -= element[1]
                                element[1] = 0
                                heapq.heappush(sells, sell)
                                ret += sell[1]
                            elif element[1] == sell[1]:
                                element[1] = 0
                            else:
                                element[1] -= sell[1]
                                element[0] = -1 * element[0]
                                heapq.heappush(buys, element)
                                ret += element[1]
                        else:
                            break
                    else:
                        element[0] = -1 * element[0]
                        heapq.heappush(buys, element)
                        ret += element[1]
                        break
        return ret % (10 ** 9 + 7)


if __name__ == '__main__':
    print(Solution().getNumberOfBacklogOrders([[10,5,0],[15,2,1],[25,1,1],[30,4,0]]))