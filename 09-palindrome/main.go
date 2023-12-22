package leet

func isPalindrome(x int) bool {
    digits := []int{};
    
    n := x;
    if n < 0 {
        return false;
    }
    
    for n > 0 {
        d := n % 10
        digits = append(digits, d)
        n = n / 10
    }
    
    for i := 0; i < len(digits)/2; i++ {
        if digits[i] != digits[len(digits) - i - 1] {
            return false
        }
    }
    
    return true
}
