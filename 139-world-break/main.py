class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        memory = {}
        
        def helper(phrase):
            
            if phrase in memory:
                return memory[phrase]
            
            if not phrase:
                memory[phrase] = True
                return True
            
            can_build = False
            
            for w in wordDict:
                if w == phrase[:len(w)] and helper(phrase[len(w):]):
                    can_build = True
            
            memory[phrase] = can_build
            return can_build
        
        return helper(s)
