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

import requests

# input: a string of the accession number of the sequence from NCBI (in quotes)
# output: a string of sequence
def callSeqFromNCBI(accessionNumber):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id={accessionNumber}&retmode=text&rettype=fasta"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch URL. Status code: {response.status_code}")

    sequences = response.text.split("\n")
    seq = ''.join(sequences[1:])

    return (seq)

# input: string for file name (in quotes with .txt), boolean
# output: string of sequence without extra lines and text
def parseFastaFile(fileName, removeFirstLine):
    file = open(fileName, "r")
    seq = file.read()
    file.close()
    if removeFirstLine:
        sequences = seq.split("\n")
        seq = ''.join(sequences[1:])
    else:
        sequences = seq.split("\n")
        seq = ''.join(sequences)
    return seq

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
seq2 = parseFastaFile("myt1LT8rawseq.txt", False)
x = SeqMatch(seq1, seq2)
print(x)







