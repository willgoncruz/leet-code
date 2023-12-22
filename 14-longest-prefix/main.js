/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    
    let prefix = "";
    let pos = 0;
    
    while (true) {
        if (pos >= strs[0].length) {
            break;
        }
        
        let shouldStop = false;
        const letter = strs[0][pos]
        
        for (let i = 1; i < strs.length; i++) {
            if (pos >= strs[i].length) {
                shouldStop = true;
                break;
            }
            
            if (letter != strs[i][pos]) {
                shouldStop = true;
                break;
            }
        }
        
        if (shouldStop) {
            break;
        }
        
        prefix = prefix + `${letter}`;
        pos += 1;
    }
    
    return prefix;
};
