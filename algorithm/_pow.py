def power(a, b): 
    ans = 1
    while b:
        if b % 2 == 1:
            ans *= a
        a *= a
        b = b//2
    return ans