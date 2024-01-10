'''
Smith-Waterman Algorithm steps:
1. Define a scoring matrix
2. Initialize the matrix with '0' score
3. Define scoring parameters
4. Calculate the scores and fill matrix
5. Traceback: start with highest score and follow the arrows back
6. Return the traceback sequence
'''
import numpy as np
import matplotlib.pyplot as plt

# input = two strings of sequence
# output = a matrix initialized with scores of the two strings 
def ScoringMatrix(seq1, seq2):

    m = len(seq1)
    n = len(seq2)
    matrix = np.zeros((m + 1, n + 1))

    match = 1
    mismatch = -1
    gap = -2

    for i in range(0, m):
        for j in range(0, n):
            i_m = i + 1
            j_m = j + 1
            max_values = [0, 0, 0]

            max_values[0] = matrix[i_m, j_m-1] + gap # this is the left neighbor
            max_values[1] = matrix[i_m-1, j_m] + gap # this is the up neighbor
            
            if seq1[i] == seq2[j]:
                max_values[2] = matrix[i_m-1, j_m-1] + match # this is the diagonal neighbor
                max_values = [max(x, 0) for x in max_values]
                matrix[i_m,j_m] = max(max_values)

            else:
                max_values[2] = matrix[i_m-1, j_m-1] + mismatch # this is the diagonal neighbor
                max_values = [max(x, 0) for x in max_values]
                matrix[i_m,j_m] = max(max_values)

    return matrix

''' 
WHAT EACH MOVE REPRESENTS
    diagonal: match/mismatch
    left:     gap in sequence 1 (i)
    up:       gap in sequence 2 (j)
'''
# input = a matrix with scores and the two string of sequences it uses
# output = three strings (two sequences aligned and comparison notation string)

def traceback(matrix, seq1, seq2):
    aligned_seq1 = []
    aligned_seq2 = []
    symbSeq = []
    matrix_size = np.array(matrix).shape
    maxRow = 0
    maxCol = 0
    maxScore = 0

    # to find max score in matrix
    for i in range(0, matrix_size[0]):
        for j in range(0, matrix_size[1]):
            currScore = matrix[i, j]

            if currScore >= maxScore:
                maxScore = currScore 
                maxRow = i
                maxCol = j

    end = maxCol == 0 and maxRow == 0
    move = next_move(matrix, maxRow, maxCol)

    while move != end:
        #print(move)
        if move == 1:                             # diagonal move
            maxRow -= 1
            maxCol -= 1
            #print(maxRow, maxCol)
            aligned_seq1.append(seq1[maxRow])
            aligned_seq2.append(seq2[maxCol])
            symbSeq.append("|")

        if move == 2:                             # up move
            maxRow -= 1
           # print(maxRow, maxCol)
            aligned_seq1.append(seq1[maxRow])
            aligned_seq2.append("-")
            symbSeq.append(" ")

        if move == 3:                             # left move 
            maxCol -= 1
           # print(maxRow, maxCol)
            aligned_seq1.append("-")
            aligned_seq2.append(seq2[maxCol])
            symbSeq.append(" ")

        if move == 0:  
            print(move)                          # mismatch and move to next highest number
            aligned_seq1.append(seq1[maxRow])
            aligned_seq2.append(seq2[maxCol])
            symbSeq.append(":")
            end = True

        print(move, matrix[maxRow, maxCol])
        move = next_move(matrix, maxRow, maxCol)
        
    aligned_seq1 = ''.join(aligned_seq1[::-1])
    symbSeq = ''.join(symbSeq[::-1])
    aligned_seq2 = ''.join(aligned_seq2[::-1])
    
    return f"{aligned_seq1}\n{symbSeq}\n{aligned_seq2}"

# input = matrix of two string sequences with rows(i) and columns(j) parameters in integer form
# output = one integer (if no errors)
def next_move(matrix, i, j):
    diag = matrix[i - 1, j - 1]
    up = matrix[i - 1, j]
    left = matrix[i, j - 1]

    if diag >= up and diag >= left:
        return 1 if diag != 0 else 0
    elif up > diag and up >= left:
        return 2 if up != 0 else 0
    elif left > up and left > diag:
        return 3 if left != 0 else 0
    else:
        return "error"
    
seq1 = "ATGGTGA"
seq2 = "ATTGGT"

matrix = ScoringMatrix(seq1, seq2)
print(matrix)
print(traceback(matrix, seq1, seq2)) 

