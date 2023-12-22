package leet 

func twoSum(nums []int, target int) []int {
    positions := map[int][]int{}
            
    for i, n := range nums {
        list, exists := positions[n]
        if !exists {
            positions[n] = []int{i}
        } else {
            list = append(list, i)
            positions[n] = list
        }
    }
    
    
    for i, n := range nums {
        subs := target - n
        list, exists := positions[subs]
        
        if exists && list[0] != i {
            index := list[0]
            return []int{i, index}
        }
    }
    
    return []int{}
}
