package leet

func digit(i int) string {
    TEN_CASES := []string{"I", "X", "C", "M"}
    return TEN_CASES[i]
}

func fiveEx(i int) string {
    FIVE_NINE_EXC := []string{"V", "L", "D", ""}
    return FIVE_NINE_EXC[i]
}

func one(i int) string {
    return digit(i)
}

func two(i int) string {
    return digit(i) + digit(i)
}

func three(i int) string {
    s := digit(i)
    return s + s + s
}

func four(i int) string {
    return digit(i) + fiveEx(i)
}

func five(i int) string {
    return fiveEx(i)
}

func six(i int) string {
    return fiveEx(i) + digit(i)
}

func seven(i int) string {
    return fiveEx(i) + digit(i) + digit(i)
}

func eight(i int) string {
    return fiveEx(i) + digit(i) + digit(i) + digit(i)
}

func nine(i int) string {
    return digit(i) + digit(i+1)
}

type fn func (int) string

func choose(n, i int) string {
    switch(n) {
        case 1:
        return one(i)
        case 2:
        return two(i)
        case 3:
        return three(i)
        case 4:
        return four(i)
        case 5:
        return five(i)
        case 6:
        return six(i)
        case 7:
        return seven(i)
        case 8:
        return eight(i)
        case 9:
        return nine(i)
        default:
        return ""
    }
}

func intToRoman(num int) string {

    i := -1
    n := 0
    roman := ""
    for num > 0 {
        i += 1
        n = num % 10
        num = num / 10
        
        if n == 0 {
            continue
        }
        
        partial := choose(n, i)
        
        roman = partial + roman
    }
    
    return roman
}
