def compare(first):
    return first[0]

class Solution(object):
    def isIntervalContained(self, first, second):
        firstStart = first[0]
        firstEnd = first[1]
        secondStart = second[0]
        secondEnd = second[1]
        
        return firstEnd >= secondStart
    
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort(key=compare)
        
        i = 0
        while i < len(intervals) - 1:
            firstInterval = intervals[i]
            nextInterval = intervals[i + 1]
            
            if self.isIntervalContained(firstInterval, nextInterval):
                start = min(firstInterval[0], nextInterval[0])
                end = max(firstInterval[1], nextInterval[1])
                intervals[i] = [start, end]
                del intervals[i + 1]
            else:
                i += 1

        return intervals
