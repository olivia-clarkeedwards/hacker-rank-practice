def palindromeIndex(word):
    if isPalindrome(word):
        return -1
    
    for index in range(len(word)):
        wordWithoutChar = word[:index] + word[index + 1:]
        if isPalindrome(wordWithoutChar):
            return index 
    
    return -1
    

def isPalindrome(word):
    if len(word) == 1:
        return True
    if len(word) % 2 == 0:
        midIndex = len(word) // 2
        firstHalf = word[:midIndex]
        lastHalf = reverse(word[midIndex:])
        if firstHalf == lastHalf:
            return True 
        else:
            return False
    else:
        midIndex = len(word) // 2
        firstHalf = word[:midIndex]
        lastHalf = reverse(word[midIndex + 1:])
        if firstHalf == lastHalf:
            return True 
        else:
            return False

def reverse(string):
    return string[::-1]


print(isPalindrome('aabc')) # false
print(isPalindrome('aba')) # true
print(isPalindrome('')) # true
print(isPalindrome('starrats')) # true
print(isPalindrome('hfien')) # false


print(palindromeIndex('bcbc')) # 0
print(palindromeIndex('aaab')) # 3
print(palindromeIndex('baa')) # 0
print(palindromeIndex('aaa')) # -1
print(palindromeIndex('a'))

