import numpy as np
import matplotlib.pyplot as plt
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

# input: two strings of sequence and one number for threshold
# output: a matrix comparing two sequences
def makeMatrix(seqx, seqy, threshold):

    rows = (len(seqx)//threshold + 1) #defining length of x-axis, rounds down the seq length
    cols = (len(seqy)//threshold + 1) #defining length of y-axis, rounds down the seq length
    print(rows, cols)
    zeros_matrix = np.zeros((rows,cols))

    for i in range(rows):
        for j in range(cols):

            if i == (rows - 1):
                frameX = seqx[threshold * i:]
            else:
                frameX = seqx[threshold * i: threshold * (i + 1)]

            if j == (cols - 1):
                frameY = seqy[threshold * j:]
            else:
                frameY = seqy[threshold*j : threshold*(j + 1)]

            count = 0

            for z in range(min(len(frameX), len(frameY))):
                if frameX[z] == frameY[z]:
                    count += 1

            if count >= (threshold/2):
                # print(j, i)
                zeros_matrix[i,j] = 1

    return zeros_matrix

seqx = parseFastaFile("myt1LT8rawseq.txt", True)
seqy = callSeqFromNCBI("NM_001329849.3")

dotplot = plt.imshow(np.array(makeMatrix(seqx, seqy, 20)))
# currently ticks represent number of frames
# xt = plt.xticks(np.arange(len(list(seqx))) , list(seqx)) > if you want to change x-axis
# yt = plt.yticks(np.arange(len(list(seqx))) , list(seqx)) > if you want to change y-axis
plt.show()

