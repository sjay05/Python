
#Euclidean algorithm to find gcd of two numbers.

def gcd(divident, divisor):
    r = divident % divisor
    if r == 0:
        return divisor
    
    ans = gcd(divisor, r)
    return ans
    
    

gcd_ans = gcd(1071, 462)
print gcd_ans

lcm_ans = (1071 * 462) / gcd (1071, 462)
print lcm_ans
