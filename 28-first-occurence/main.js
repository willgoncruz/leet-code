/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    
    if (!needle.length) {
        return 0;
    }
    
    for (let i = 0; i < haystack.length; i++) {
        if (haystack[i] !== needle[0]) {
            continue;
        }
        
        let found = true;
        for (let j = 1; j < needle.length; j++) {
            if (i + j >= haystack.length) {
                found = false;
                break;
            }
            
            if (haystack[i + j] !== needle[j]) {
                found = false;
                break;
            }
        }
        
        if (found) {
            return i;
        }
    }
    
    
    return -1;
};
