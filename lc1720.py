class Solution(object):
    @staticmethod
    def mapping(x):
        map_dict = {'11': '0', '10':'1', '00':'0', '01':'1'}
        return map_dict[x]

    def element_decoder(self, num1, num2):
        num1, num2 = bin(num1)[2:], bin(num2)[2:]
        if len(num1) < len(num2):
            while len(num1) < len(num2):
                num1 = '0' + num1
        else:
            while len(num2) < len(num1):
                num2 = '0' + num2
        num = ''
        for i in range(len(num1)):
            num += self.mapping(num1[i]+num2[i])
        return int(num, 2)

    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        lst = [first]
        for i in range(len(encoded)):
            lst.append(self.element_decoder(lst[i], encoded[i]))
        return lst

if __name__ == '__main__':
    # print(Solution().element_decoder(0, 2))
    print(Solution().decode([6, 2, 7, 4], 4))
