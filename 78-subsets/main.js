/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    let output = [[]]
    
    nums.forEach((num) => {
        const generated = output.map((curr) => [num, ...curr])
        output = output.concat(generated)
    });
    
    return output
};
