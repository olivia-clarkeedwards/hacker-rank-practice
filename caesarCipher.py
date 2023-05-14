# shift alpha characters of string by k places 
# wrap around at end of alpha bet 
# retain casing 

def caesarCipher(s, k):
    lowerAlpha = ''.join(letter for letter in [chr(x) for x in range(97, 123)])
    upperAlpha = lowerAlpha.upper()

    result = ''
    
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i] in lowerAlpha:
                result += lowerAlpha[(lowerAlpha.index(s[i]) + k) % 26]
            elif s[i] in upperAlpha:
                result += upperAlpha[(upperAlpha.index(s[i]) + k) % 26]
        else:
            result += s[i]

    return result


print(caesarCipher('There\'s-a-starman-waiting-in-the-sky', 3))