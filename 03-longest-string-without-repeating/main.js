/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    const substrings = new Map()
    
    const finalizedSubstrings = []
    
    for (let i = 0; i < s.length; i++) {
        const c = s[i]
        
         substrings.forEach((value,key,map) => {
            if (value.includes(c)) {
                finalizedSubstrings.push(value)
                map.delete(key)
                return
            }
            
            value.push(c)
            map.set(i, value)
        })

        substrings.set(i, [c])
    }
    
     substrings.forEach((value,key,map) => {
        finalizedSubstrings.push(value)  
     })
    
    let max = 0
    for (let i = 0; i < finalizedSubstrings.length; i++) {
        const s = finalizedSubstrings[i]
        if (s.length > max) {
            max = s.length
        }
    }
    
    return max
};
