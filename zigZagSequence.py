# Sample input 

# 2 - number of test cases 
# 7 - length of test array 
# 1 2 3 5 4 7 6 - test array 
# 9 - length of test array
# 5 4 3 6 1 2 8 7 9 - test array

def findZigZagSequence(a, n):
    a.sort()
    mid = int((n)//2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)



