class SimpleTextEditor():
    def __init__(self):
        self.string = ''
        self.last_move = []

    def addString(self, string_to_append):
        self.string += string_to_append
        self.last_move.append([1, len(string_to_append)])

    def delete(self, num_to_delete):
        deleted_section = self.string[len(self.string) - num_to_delete:]
        self.string = self.string[:len(self.string) - num_to_delete]
        self.last_move.append([2, deleted_section])

    def printChar(self, index_to_print):
        print(self.string[index_to_print - 1])

    def undoLastMove(self):
        if len(self.last_move) == 0:
            print('No moves to undo.')
        else:
            move_to_undo = self.last_move.pop()
            if move_to_undo[0] == 1:
                self.string = self.string[:len(self.string) - move_to_undo[1]]
            else:
                self.string += move_to_undo[1]


def processQueries():
    queryCount = int(input())
    s = SimpleTextEditor()

    for _ in range(queryCount):
        query = input().split()
        if query[0] == '1':
            s.addString(query[1])
        elif query[0] == '2':
            s.delete(int(query[1]))
        elif query[0] == '3':
            s.printChar(int(query[1]))
        else:
            s.undoLastMove()

processQueries()