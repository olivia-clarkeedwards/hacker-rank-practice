def processQueries():
    queryCount = int(input())

    for _ in range(queryCount):
        query = input().split()
        if query[0] == '1':
            # append specified string to current string
        elif query[0] == '2':
            # delete last specified number of letters
        elif query[0] == '3':
            # print the nth specified letter
        else:
            # undo the last append or delete operation

processQueries()