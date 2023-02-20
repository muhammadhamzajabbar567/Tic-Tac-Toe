# TIC TAC TOE
def sum(a, b, c):
    return a + b + c

def printboard(xstate, ystate):

    zero = 'X' if xstate[0] else ('0' if ystate[0] else 0)
    one = 'X' if xstate[1] else ('0' if ystate[1] else 1)
    two = 'X' if xstate[2] else ('0' if ystate[2] else 2)
    three = 'X' if xstate[3] else ('0' if ystate[3] else 3)
    four = 'X' if xstate[4] else ('0' if ystate[4] else 4)
    five = 'X' if xstate[5] else ('0' if ystate[5] else 5)
    six = 'X' if xstate[6] else ('0' if ystate[6] else 6)
    seven = 'X' if xstate[7] else ('0' if ystate[7] else 7)
    eight = 'X' if xstate[8] else ('0' if ystate[8] else 8)

    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")

def checkwin(xstate, ystate):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for win in wins:
        if(sum(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3):
            print("\n \t \t Congratulations! X Won The Match")
            return 1
        if (sum(ystate[win[0]], ystate[win[1]], ystate[win[2]]) == 3):
            print("\n \t \t Congratulations! Y Won The Match")
            return 0
    return -1

if __name__ == "__main__":
    xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ystate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1         # 1 for x and 0 for O
    print("\n Well Come To Tic Tac Toe")
    print("==========================")
    while(True):
        printboard(xstate, ystate)
        if (turn == 1):
            print("X's Chance")
            value = int(input("Please Enter A Value: "))
            xstate[value] = 1
        else:
            print("0's Chance")
            value = int(input("Please Enter A Value: "))
            ystate[value] = 1
        cwin = checkwin(xstate, ystate)
        if(cwin != -1):
            print("\t \t Match Over!")
            print("\t\t  =======================================")
            break

        turn = 1 - turn

