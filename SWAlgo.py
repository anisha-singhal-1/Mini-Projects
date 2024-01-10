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
            i_m = i + 1   # to skip first row and column
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

    currRow = maxRow
    currCol = maxCol
    currSymb = "|"
    move = "D"

    while currRow != 0 and currCol != 0:
        
        if move == "D":
            aligned_seq1.append(seq1[currRow - 1])
            aligned_seq2.append(seq2[currCol - 1])
            symbSeq.append(currSymb)
        if move == "U":
            aligned_seq1.append(seq1[currRow])
            aligned_seq2.append("-")
            symbSeq.append(currSymb)
        if move == "L":
            aligned_seq1.append("-")
            aligned_seq2.append(seq2[currCol])
            symbSeq.append(currSymb)
        
        diag = matrix[currRow - 1, currCol - 1]
        up = matrix[currRow - 1, currCol]
        left = matrix[currRow, currCol - 1]

        if diag >= up and diag >= left:
            move = "D"
            currRow -= 1 
            currCol -= 1
            currSymb = "|"
        elif up > diag and up >= left:
            move = "U"
            currRow -= 1
            currSymb = " "
        elif left > up and left > diag:
            move = "L"
            currCol -= 1
            currSymb = " "

    aligned_seq1 = ''.join(aligned_seq1[::-1])
    symbSeq = ''.join(symbSeq[::-1])
    aligned_seq2 = ''.join(aligned_seq2[::-1])
    
    return f"{aligned_seq1}\n{symbSeq}\n{aligned_seq2}"
    
seq1 = "CCATGGTGA"
seq2 = "GAACATTGGT"

matrix = ScoringMatrix(seq1, seq2)
print(matrix)
print(traceback(matrix, seq1, seq2)) 

