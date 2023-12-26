'''
1. extract DNA sequence from NCBI using accession number
2. convert DNA sequence into mRNA
3. convert mRNA sequence into protein
4. parse fasta file
5. detect open reading frames

another day...
5. pairwise align multiple sequences
6. identifying the motifs of repeated sequences
7. making gene trees
'''

import requests

# input: string of accession number from NCBI
# output: string of sequence without first line
def callSeqFromNCBI(accessionNumber):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id={accessionNumber}&retmode=text&rettype=fasta"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch URL. Status code: {response.status_code}")

    sequences = response.text.split("\n")
    seq = ''.join(sequences[1:])

    return (seq)


# input sequence fasta file name, returns string of sequence only
def parseFastaFile(fileName):
    file = open(fileName, "r")
    seq = file.read()
    # print(seq)
    file.close()
    sequences = seq.split("\n")
    seq = ''.join(sequences[1:])

    return seq

# converting DNA sequence into mRNA sequence in codons (triplets)
# input: string of DNA sequence
# output: list of codons
def DNAtomRNA(seq):
    mRNASwitchKey = {'A': 'U', 'G': 'C', 'C': 'G', 'T': 'A'}
    codons = []  # separated sequence into codons (triplets) and created a list of it
    codon = ""  # each triplet

    for i in range(len(seq)):
        base = seq[i]
        codon += mRNASwitchKey[base]
        if i % 3 == 2:
            codons.append(codon)
            codon = ''

    return codons

# converting mRNA codons into proteins
# input: list of codon strings
# output: list of protein characters
def mRNAtoProteins(codons):
    AAcode = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
              "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
              "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
              "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
              "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
              "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
              "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
              "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
              "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
              "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
              "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
              "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
              "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
              "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
              "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
              "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", }

    proteins = []
    for codon in codons:
        proteins.append(AAcode[codon])

    return proteins

# input: list of codon strings
# output: list of ORF strings
def ORFreader(mRNAseq):
    protSeq = mRNAtoProteins(mRNAseq)
    ORFs = []
    ORF = ""
    inORF = False
    for protein in protSeq:
        if protein == "M":
            inORF = True

        if protein == "STOP" and inORF:
            inORF = False
            ORFs.append(ORF)
            ORF = ''

        if inORF:
            ORF += protein
    return ORFs



fastaSeq = callSeqFromNCBI("NM_001303052.2")
mRNAfastaSeq = DNAtomRNA(fastaSeq)
ORFs = ORFreader(mRNAfastaSeq)
print(ORFs)

