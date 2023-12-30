'''
1. Call BLASTn to find similar sequence
2. Use parameters to find the match sequence
3. Match the lengths of sequences
4. Compare inputed sequence with the match
    or see if the sequence is detected in the best BLAST sequence
5. Find the largest piece of sequence without "N" base
6. Detect mutations between the two sequences

1. find difference between two sequence lengths
2. create a list = difference, which stores the number of matches
3. return the frame of values that has the most matches

'''
from ParseFile import parseFastaFile, callSeqFromNCBI

# input: two strings of sequence
# output: number of matches, a string of sequence showing the base matches between input seqeunces
def SeqMatch(seq1, seq2):
    bestMatch = 0
    bestSeqList = []

    if len(seq1) > len(seq2):
        longSeq = seq1
        shortSeq = seq2
    else:
        shortSeq = seq1
        longSeq = seq2

    for i in range(len(longSeq)-len(shortSeq) + 1):
        currSeq = ""
        currMatch = 0
        for j in range(len(shortSeq)):
            lBase = longSeq[i+j]
            sBase = shortSeq[j]
            if sBase == lBase:
                currMatch += 1
                currSeq += lBase
            else:
                currSeq += '*'

        if currMatch > bestMatch:
            bestMatch = currMatch
            bestSeqList = []
            bestSeqList.append(currSeq)
        elif currMatch == bestMatch:
            bestSeqList.append(currSeq)

    return (bestMatch, bestSeqList)

seq1 = callSeqFromNCBI("NM_001329849.3")
seq2 = parseFastaFile("Data/myt1LT8rawseq.txt", False)
x = SeqMatch(seq1, seq2)
print(x)

