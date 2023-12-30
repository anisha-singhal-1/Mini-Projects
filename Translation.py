from ParseFile import parseFastaFile, callSeqFromNCBI

# converting DNA sequence into mRNA sequence in codons (triplets)
# input: string of DNA sequence
# output: list of codons
def DNAtomRNA(seq):
    mRNASwitchKey = {'A': 'A', 'G': 'G', 'C': 'C', 'T': 'U'}
    codons = ""  # separated sequence into codons (triplets) and created a list of it
    codon = ""  # each triplet

    for i in range(len(seq)):
        base = seq[i]
        codon += mRNASwitchKey[base]
        if i % 3 == 2:
            codons += codon
            codon = ''

    return codons

# converting mRNA codons into proteins
# input: a string of sequence as mRNA
# output: list of protein characters
def mRNAtoProteins(codons):

    if len(codons) % 3 != 0:
        length = len(codons)
        new_length = length - (length % 3)
        codons = codons[:new_length]
        

    AAcode = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
              "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
              "UAU": "Y", "UAC": "Y", "UAA": "—", "UAG": "—",
              "UGU": "C", "UGC": "C", "UGA": "—", "UGG": "W",
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
              "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

    proteins = ''
    for i in range(0, len(codons), 3):
        codon = codons[i:i+3]
        proteins += AAcode[codon]

    return proteins


if __name__  == '__main__':
    fastaSeq = callSeqFromNCBI("NM_001303052.2")
    mRNAfastaSeq = DNAtomRNA(fastaSeq)
    protSeq = mRNAtoProteins(mRNAfastaSeq)

    print(protSeq)