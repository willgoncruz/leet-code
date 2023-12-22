class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        stack = []
        directories = path.split("/")
        
        for i in range(len(directories)):
            current = directories[i]
            
            if not current:
                continue
                
            if current == '.':
                continue
            elif current == '..':
                if len(stack) > 0:
                    del stack[len(stack) - 1]
            else:
                stack.append(current)
                
        
        new_path = '/' + '/'.join(stack)
        return new_path
