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
    seen_prefixes, seen_words = set(), set()

    for word in words:
        if word in seen_words:
            print(f"BAD SET\n{word}")
            return
        else:
            seen_words.add(word)
        for index in range(1, len(word)):
            prefix = word[:index]
            if prefix in seen_prefixes:
                print(f"BAD SET\n{word}")
                return 
            else:
                seen_prefixes.add(prefix)
    print(f"GOOD SET") 

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