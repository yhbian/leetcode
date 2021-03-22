import heapq

class Solution:
    def getNumberOfBacklogOrders(self, orders):
        sells, buys = [], []
        ret = 0
        # sells prior is descend
        for element in orders:
            print(ret)
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
                            ret += buy[1] + element[1]
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
                            ret += sell[1] + element[1]
                            break
                    else:
                        element[0] = -1 * element[0]
                        heapq.heappush(buys, element)
                        ret += element[1]
                        break
                        
        return ret % (10 ** 9 + 7)

if __name__ == '__main__':
    print(Solution().getNumberOfBacklogOrders([[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]))