/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    const count = {};
    
    let k = nums.length;
    let maxValue = 0; 
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === val) {
            k -= 1;
        } else {
            count[nums[i]] = (count[nums[i]] || 0) + 1;
        }
        
        maxValue = Math.max(maxValue, nums[i])
    }
    
    let j = 0;
    let l = 0;
    for (let i = 0; i <= maxValue; i++) {
        if (count[i] && count[i] > 0) {
            for (l = 0; l < count[i]; l++) {
                nums[j] = i;
                j += 1
            }
        }
    }
    
    return k;
};
