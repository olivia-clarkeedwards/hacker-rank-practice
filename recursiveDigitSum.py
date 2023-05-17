# get super digit of the string n concatenated k times 
# super digit is the sum of digits until the result is length 1
# https://en.wikipedia.org/wiki/Digital_root

def getSuper(n, memo = {}):
    sum = n % 9
    if sum == 0:
        return 9
    if sum < 10:
        return sum
    return getSuper(sum)
        
def superDigit(n, k):
    superN = getSuper(int(n))
    return getSuper(superN * k)


print(superDigit('14', 3))