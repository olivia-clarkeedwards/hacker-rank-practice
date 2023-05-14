import sys 

def main():
    count = 0
    englishRoll = set()
    frenchRoll = set()

    while count < 4:
        for line in sys.stdin:
            if count == 1:
                [englishRoll.add(int(s)) for s in line.split()]
            elif count == 3:
                [frenchRoll.add(int(s)) for s in line.split()]
            count += 1
            break
        
    print(len(englishRoll.symmetric_difference(frenchRoll)), file=sys.stdout)
            




main()