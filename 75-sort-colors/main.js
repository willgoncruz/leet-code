/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    let count = {
        0: 0,
        1: 0,
        2: 0
    };
    
    nums.forEach((item) => {
        count[item] = count[item] + 1 
    });
    
    let pos = 0;
    while (count[pos] === 0) {
        pos += 1
    }
    
    for (let i = 0; i < nums.length; i++) {
        nums[i] = pos;
        count[pos] = count[pos] - 1;
        while (count[pos] === 0) {
            pos += 1
        }
    }
};
