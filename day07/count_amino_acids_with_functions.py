from collections import defaultdict
import sys

CODON_TABLE = {
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
    'STOP': ['TAA', 'TAG', 'TGA']
}

def build_codon_map(table):
    return {codon: aa for aa, codons in table.items() for codon in codons}

def read_fasta(file_path):
    with open(file_path, 'r') as f:
        return ''.join(line.strip() for line in f if not line.startswith('>')).upper()

def translate_sequence(seq, codon_map):
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        if codon in codon_map:
            yield codon_map[codon]

def count_amino_acids(amino_seq):
    counts = defaultdict(int)
    for aa in amino_seq:
        if aa != 'STOP':
            counts[aa] += 1
    return counts

def print_counts(counts):
    for aa in sorted(counts):
        print(f"{aa.ljust(5)} {counts[aa]}")

def main(input_file):
    codon_map = build_codon_map(CODON_TABLE)
    sequence = read_fasta(input_file)
    amino_acids = translate_sequence(sequence, codon_map)
    counts = count_amino_acids(amino_acids)
    print_counts(counts)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_amino_acids_with_functions.py <fasta_file>")
        sys.exit(1)
    main(sys.argv[1])
