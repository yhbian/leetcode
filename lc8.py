class Automation:
    def __init__(self):
        self.state = 'start'
        self.num = 0
        self.sign = 1
        self.transition = {
                           'start':  ['start', 'signed', 'in_num', 'end'],
                           'signed': ['end', 'end', 'in_num', 'end'],
                           'in_num': ['end', 'end', 'in_num', 'end'],
                           'end':    ['end', 'end', 'end', 'end']
                           }

    def update(self, this_state, c):
        self.state = self.transition[self.state][this_state]
        if self.state == 'in_num':
            self.num = self.num * 10 + int(c)
        if self.state == 'signed' and c == '-':
            self.sign = -1

    def signal(self, c):
        if c == ' ':
            this_state = 0
        elif c == '-' or c == '+':
            this_state = 1
        elif c in ['0', '1', '2', '3', '4',
                   '5', '6', '7', '8', '9']:
            this_state = 2
        else:
            this_state = 3
        self.update(this_state, c)


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        automation = Automation()
        for c in s:
            automation.signal(c)
        num = automation.sign * automation.num
        if num < -2 ** 31:
            return -2 ** 31
        if num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return num


if __name__ == '__main__':
    print(Solution().myAtoi(' m87'))

