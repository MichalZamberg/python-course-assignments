import sys
from collections import defaultdict

codon_table = {
    'Phe' : ['TTT', 'TTC'],
    'Leu' : ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'Ile' : ['ATT', 'ATC', 'ATA'],
    'Met' : ['ATG'],
    'Val' : ['GTT', 'GTC', 'GTA', 'GTG'],
    'Ser' : ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Pro' : ['CCT', 'CCC', 'CCA', 'CCG'],
    'Thr' : ['ACT', 'ACC', 'ACA', 'ACG'],
    'Ala' : ['GCT', 'GCC', 'GCA', 'GCG'],
    'Tyr' : ['TAT', 'TAC'],
    'His' : ['CAT', 'CAC'],
    'Gln' : ['CAA', 'CAG'],
    'Asn' : ['AAT', 'AAC'],
    'Lys' : ['AAA', 'AAG'],
    'Asp' : ['GAT', 'GAC'],
    'Glu' : ['GAA', 'GAG'],
    'Cys' : ['TGT', 'TGC'],
    'Trp' : ['TGG'],
    'Arg' : ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Gly' : ['GGT', 'GGC', 'GGA', 'GGG'],
    'STOP' : ['TAA', 'TAG', 'TGA']
}
codon_to_amino = {}
for aa, codons in codon_table.items():
    for codon in codons:
        codon_to_amino[codon] = aa

def read_fasta_sequence(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))
    return sequence.upper()

def count_amino_acids(dna_sequence):
    counts = defaultdict(int)
    for i in range(0, len(dna_sequence) - 2, 3):
        codon = dna_sequence[i:i+3]
        if codon in codon_to_amino:
            amino = codon_to_amino[codon]
            if amino != 'STOP':
                counts[amino] += 1
    return counts

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_amino_acids.py <fasta_file>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    dna_seq = read_fasta_sequence(fasta_file)
    aa_counts = count_amino_acids(dna_seq)

    for aa in sorted(aa_counts):
        print(f"{aa.ljust(5)} {aa_counts[aa]}")
