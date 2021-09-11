import time  # import time functions


# -----------------------------------------
# function used to test if queen can be placed at location
def placable(row, col):
    # Check if other queen in same column
    # if another queen, return false
    for prevCol in sol:
        if col == prevCol:
            return False

    # Check for other queen in diagonals
    # if there is queen, return false
    for prevRow, prevCol in enumerate(sol):
        if abs(row - prevRow) == abs(col - prevCol):
            return False

    # if no issues queen can be placed, return true
    return True


# -----------------------------------------
# print function
def printBoard():

    # create empty string for output
    output = ""

    output += ('Solution: ' + str(count) + '\n')

    # go through each item in solution list, row by row
    for col in sol:

        # represents columns in the row
        for i in range(n):

            # if queen is located at index, output a 'Q'
            if col == i:
                output += "Q "

            else:  # Otherwise output '-'
                output += "- "

        # print output
        output += '\n'

    output += '\n'

    if show:
        print(output)

    if writeFile:
        f.write(output)


def yesNo(ans):
    while True:
        if ans.upper() == 'Y':
            return True
        if ans.upper() == 'N':
            return False
        else:
            ans = input('invalid answer; Enter Y/N: ')



# -----------------------------------------
# Main Program

print("N-Queen Solver")
print("Find number of solutions for placing chess queens on a NxN sized board without threatening each other \n \n")

# Prompt User Input
n = int(input("input size of chess board: "))

show = yesNo(input('Do you want to show results? (Y/N): '))

writeFile = yesNo(input('Write results to file? (Y/N): '))


if writeFile:
    name = str(n) + '_Queens_Results.txt'
    f = open(name,'w')


# create stack to store solutions
sol = []

# create row,column and count, set to 0
row = 0
col = 0
count = 0

# set flag used to check for first result to True
first = True

# record time program started
startTime = time.time()

# loop
while True:

    # Each Q must be placed in unique column
    # Checks if there is remaining space where Q can be placed
    while col < n:

        # Checks if Q can be placed in next row
        if placable(row, col):

            # place queen in column
            # set column to 0, increase row by 1
            sol.append(col)
            col = 0
            row += 1

            # exit loop break
        else:   # otherwise move to next position in row
            col += 1

    # if cant place
    if row == n or col == n:

        # backtrack
        if col == n and row != 0:

            # find column of last queen in stack and add 1
            # used for next iteration
            col = sol[-1] + 1

            # remove last queen placed
            sol.pop()

            # go to previous row
            row -= 1

        # if already backtracked to first row, no solution
        if row == 0 and col == n:

            # exit loop
            break

        # board complete if n - 1 rows have queens filled (index starts at 0)
        # Found Solution
        if row == n - 1:

            # if first solution found, record time in variable
            if first:
                first = False
                firstTime = time.time()

            # increase counter and backtrack
            # count = count + 1
            sol.append(col - 1)
            count+=1

            if (show or writeFile):
                printBoard()

            sol.pop()

#close file
if writeFile:
    f.close()

# output results
print("\n\nNumber of Solutions = " + str(count))
print("Time to First = ", 1000*(firstTime - startTime), "ms")
print("Time to Complete = ", 1000*(time.time() - startTime), "ms")
