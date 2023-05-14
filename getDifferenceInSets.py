import sys

def main():
    inputCount = 0
    englishRoll = set()
    frenchRoll = set()

    while inputCount < 4:
        for line in sys.stdin:
            if inputCount == 1:
                students = line.split()
                [englishRoll.add(int(s)) for s in students]
            elif inputCount == 3:
                students = line.split()
                [frenchRoll.add(int(s)) for s in students]
            inputCount += 1
            break
        
    print(len(englishRoll.difference(frenchRoll)), file=sys.stdout)
    # sys.stdout.write(str(len(englishRoll.difference(frenchRoll))))


main()