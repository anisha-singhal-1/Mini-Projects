

def smith_waterman(seq1, seq2, match=2, mismatch=-1, gap_penalty=-1):
    m = len(seq1)
    n = len(seq2)

    # Initialize scoring matrix
    matrix = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill in the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match_mismatch = matrix[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)
            gap_up = matrix[i-1][j] + gap_penalty
            gap_left = matrix[i][j-1] + gap_penalty

            matrix[i][j] = max(0, match_mismatch, gap_up, gap_left)

    # Traceback to find the local alignment
    max_score = 0
    max_i, max_j = 0, 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if matrix[i][j] > max_score:
                max_score = matrix[i][j]
                max_i, max_j = i, j

    # Output the local alignment
    aligned_seq1 = seq1[max_i-1::-1]
    aligned_seq2 = seq2[max_j-1::-1]

    return aligned_seq1, aligned_seq2

seq1 = "ATTGGTGAATTCCTA"
seq2 = "AGGTGAATTCTA"

print(smith_waterman(seq1, seq2, match=2, mismatch=-1, gap_penalty=-1))