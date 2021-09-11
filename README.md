# N-Queens Solver

## Overview

The N-Queens Solver program aims to solve the problem of placing N number of
queens on a NxN sized chess board. Often the number of queens being looked at is
8, however it is scalable to larger sizes.

The aim of this project was to analyze and find any benefits that may exist when solving the problem using a recursive algorithm over an iterative algorithm.

## How to Use

This program compares two different approaches both with an iterative algorithm,
and a recursive solution. Both variations allow for input of the size of board
and allow users to print solutions in terminal and choose whether or not to
write to a file.

To execute simply run either `iterative.py` or `recursive.py`

## Algorithm and Analysis

### Algorithm
Described below is the algorithm pseudocode used in the planning of the
implementation of each solution.

#### Iterative

```
Algorithm queensIterative(n):
	Input: The size of chess board / number of queens used in puzzle
	Output: All possible solutions to N-Queens puzzle

	A -> new list of integers
	col -> 0

	While True do:

		While column < n do:
			if canPlace(col) then:
				A.append(col)
				col <- 0
				break
			Else:
				col <- col + 1

		if A.length = n or col = n then:

			if A.length != 0 and col =n then:
				col <- A[-1] + 1
                A.pop()
			if A.length = 0 and col = n then:
				Break
			if A.length = n:
				printBoard(A)
				col <- A[-1] + 1
                A.pop()
```
#### Recursive
```
Algorithm: queensRecursive(n,col, A):
	Input: The size of chess board, current column, empty list
	Output: All possible solutions to N-Queens puzzle

		While col < n do:
            If canPlace(col) then:
		        A.append(col)
				col <- 0

				if A.length = n then:
					printBoard()

				queenRecursive(n,col,A)
			    col <- A[-1] + 1
                A.pop()
			else:
				col <- col + 1
		return
```

### Performance

##### Comparison of running time between algorithms
Time in seconds

| Method    | Finding First solution (N=8) | Finding First solution (N=9) | Finding all Solutions(N=8) | Finding all Solutions(N=9) |
| --------- | ---------------------------- | ---------------------------- | -------------------------- | -------------------------- |
| Iterative | 0.999928                     | 1.000404                     | 39.00862                   | 255.057096                 |
| Recursive | 0.999928                     | 1.000404                     | 38.00869                   | 248.055696                 |

##### Time to find solutions on NxN sized board
For N > 6

| **N** | **Iterative** | **Recursive** | **% Difference** |
| ----- | ------------- | ------------- | ---------------- |
| 6     | 0.999         | 1.000         | 0.166964818      |
| 7     | 16.004        | 14.003        | 13.33418086      |
| 8     | 39.009        | 38.009        | 2.596637042      |
| 9     | 255.057       | 248.056       | 2.783232743      |
| 10    | 638.158       | 634.143       | 0.631172327      |
| 11    | 2838.640      | 2804.138      | 1.222865302      |
| 12    | 17331.448     | 17232.958     | 0.569891244      |
| 13    | 106688.073    | 105764.0202   | 0.869892562      |

### Conclusion
It was found that the N-Queens efficiency does not improve using a recursive solution over an iterative implementation.
