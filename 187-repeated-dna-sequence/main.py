class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        hits = {}
        results = set()
        for i in range(len(s)):
            seq = s[i:i+10]
            if seq in hits:
                results.add(seq)                
            else:
                hits[seq] = 1
                
        return results
