class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for i in intervals[1:]:
            if res[-1][1]>=i[0]:
                res[-1][1] = max(i[1],res[-1][1])
            else:
                res.append(i)
        
        return res





intervals = [[1,4],[2,3]]
s=Solution()
s.merge(intervals)