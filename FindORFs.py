'''
1. extract DNA sequence from NCBI using accession number
2. convert DNA sequence into mRNA
3. convert mRNA sequence into protein
4. parse fasta file
5. detect open reading frames

NEW TASK: 12/27
Three reading frames
1. Offset the start of the sequence by 0, 1 and 2
2. Return longest ORF and which frame it is in

Complement DNA sequences
1. Reverse the sequence (5'3 -> 3'5)
2. Find complementary strand sequence
3. Reverse and complement 
'''
from ParseFile import parseFastaFile, callSeqFromNCBI
from Translation import DNAtomRNA, mRNAtoProteins

# input: a string of protein sequence
# output: list of ORF strings
def ORFfinder(protSeq):
    ORFs = []
    ORF = ""
    inORF = False
    
    for protein in protSeq:

        if protein == "M":
            inORF = True

        if protein == "—" and inORF:
            inORF = False
            ORFs.append(ORF)
            ORF = ''

        if inORF:
            ORF += protein
    
    return ORFs

def reverseSeq(seq):
    return seq[::-1]

def complementStrand(seq):
    compBase = {"A":"T", "T":"A", "C":"G", "G":"C"}
    
    compStrand = ""
    for base in seq:
        compStrand += compBase[base]

    return compStrand

def reverseComplementSeq(seq):
    comp = complementStrand(seq)
    revCompStrand = comp[::-1]

    return revCompStrand
    
# input: a string of sequence in mRNA format
# output: a string of sequence which is the longest ORF from all three frames

def ReadingFrames(mRNAseq):

    FrameSeq1 = mRNAtoProteins(mRNAseq)
    FrameSeq2 = mRNAtoProteins(mRNAseq[1:])
    FrameSeq3 = mRNAtoProteins(mRNAseq[2:])

    frames = [FrameSeq1, FrameSeq2, FrameSeq3]
    bestFrame = None
    longestORF = ""

    for frame in frames:
        ORFList = ORFfinder(frame)

        for i in ORFList:
            if len(i) > len(longestORF):
                longestORF = i
                bestFrame = frames.index(frame) + 1
               
    return bestFrame, "longest ORF: " + longestORF


fastaSeq = parseFastaFile("Data/DNAfasta.txt", False)
mRNAsequence = DNAtomRNA(fastaSeq)
ORF = ReadingFrames(mRNAsequence)
print(ORF)


