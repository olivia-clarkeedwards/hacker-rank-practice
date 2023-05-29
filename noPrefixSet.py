#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    words_by_alpha = {}
    
    for word in words:
        target_letter = word[0]

        if target_letter in words_by_alpha:
            
            for target in words_by_alpha[target_letter]:
                if target[:len(word)] == word or word[:len(target)] == target:
                    print('BAD SET')
                    print(word)
                    return
            words_by_alpha[target_letter].append(word)
        else:
            words_by_alpha[target_letter] = [word]
            
    print('GOOD SET')
    return
        
    

def main():
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)

main()

# noPrefix(['aab', 'defgab', 'abcde', 'aabcde', 'bbbbbbbbbb', 'jabjjjad'])
# noPrefix(['ab', 'bc', 'cd'])