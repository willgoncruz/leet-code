package leet

import (
  "math"
)

func reverse(x int) int {
    i := 1
    if (x < 0) {
        i = -1
        x = x * i
    }
    
    n := 0
    for x > 0 {
        n = n * 10 + x % 10
        x = x / 10
        
        if n > math.MaxInt32 {
            n = 0
            i = 1
            break
        }
    }
    
    return n * i
}
