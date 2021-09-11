import time  # import time functions


# -----------------------------------------
# function used to test if queen can be placed at location
def placable(col):
    # Check if other queen in same column
    # if another queen, return false
    for prevCol in sol:
        if col == prevCol:
            return False

    # Check for other queen in diagonals
    # if there is queen, return false
    for prevRow, prevCol in enumerate(sol):
        if abs(len(sol) - prevRow) == abs(col - prevCol):
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


# -----------------------------------------
# recursive function to solve
def solve(col):
    # while there is space in row, ie columns have not reached size
    while col < n:

        # Check if queen can be placed
        if placable(col):

            # if queen can be placed, place queen restart columns at 0
            sol.append(col)
            col = 0

            # num of items in solution list represent rows
            # if there are n rows
            if len(sol) == n:
                global count
                # check if it is first solution, output
                if count == 0:
                    global firstTime
                    firstTime = "Time to First = " + str(1000*(time.time() - startTime))+ " ms"

                count+=1
                # print the solution found
                if (show or writeFile):
                    printBoard()

            # recursively call solve function, increase depth
            solve(col)

            # after inner depth has completed
            # set column to next index after last placed queen
            # continue searching for solutions
            col = sol[- 1] + 1
            sol.pop()
        else:
            col += 1  # if queen cannot be placed, increment columns

    # if no solution on row, return function moving to outer depths
    return


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

# set a counter to 0
count = 0

# create stack to store solutions
sol = []

# record time before running program
startTime = time.time()

# call function
solve(0)

# print number of solutions
print("Number of Solutions = " + str(count))

print(firstTime)
# print time required to complete
print("Time to Complete = ", 1000*(time.time() - startTime), "ms")
