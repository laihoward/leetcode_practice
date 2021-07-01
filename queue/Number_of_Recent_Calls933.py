class RecentCounter(object):

    def __init__(self):
        self.num = []

    def ping(self, t):
        while self.num and self.num[0]<t-3000:
            self.num.pop(0)
        self.num.append(t)
        return len(self.num)

        """
        :type t: int
        :rtype: int
        """
        