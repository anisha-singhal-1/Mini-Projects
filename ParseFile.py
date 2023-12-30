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
    result = seq.replace(" ", "")

    return result


# input: string for file name (in quotes with .txt), boolean
# output: string of sequence without extra lines and text
def parseFastaFile(fileName, removeFirstLine):
    file = open(fileName, "r")
    seq = file.read()
    file.close()
    if removeFirstLine:
        sequences = seq.split("\n")
        seq = ''.join(sequences[1:])
        result = seq.replace(" ", "")
    else:
        sequences = seq.split("\n")
        seq = ''.join(sequences)
        result = seq.replace(" ", "")
    return result

