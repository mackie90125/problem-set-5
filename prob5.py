# MOLB-7621 problem set 5

from collections import Counter
import ipdb

# problem 1

filename = '/home/ryan/MOLB-7621/data-sets/bed/lamina.bed'

big_chrom = ''
big_start = 0

bigend_start = 0
bigend_end = 0

for line in open(filename):
    if line.startswith('#'): continue
    parts = line.strip().split('\t')
    chrom = parts[0]
    start = int(parts[1])
    end = int(parts[2])
    if start > big_start:
        big_chrom = chrom
        big_start = start

    if chrom == 'chrY':
        if end > bigend_end:
            bigend_start = start
            bigend_end = end


print 'answer-1: {}'.format(big_chrom)
print 'answer-2: chrY:{}-{}'.format(bigend_start,bigend_end)

# problem 2

fastqfilename = '/home/ryan/MOLB-7621/data-sets/fastq/SP1.fq'

line_num = 0
big_C = 0
big_seq = ''
seq_num = 0
big_qual = 0
rev_comp_list = []

def reverse_complement(sequence):
    comp = []
    for char in sequence:
        if char == 'A':
            comp.append('T')
        elif char == 'T':
            comp.append('A')
        elif char == 'C':
            comp.append('G')
        elif char == 'G':
            comp.append('C')
        elif char == 'U':
            comp.append('A')
    return ''.join(reversed(comp))

for line in open(fastqfilename):
    line_type = line_num % 4
    if line_type == 0:
        name = line.strip()
    elif line_type == 1:
        seq = line.strip()
        seq_num += 1
    elif line_type == 3:
        qual = line.strip()

        counts = Counter(seq)
        if counts['C'] > big_C and seq_num <= 10:
            big_C = counts['C']
            big_seq = name

        sum_qual = sum([ord(i) for i in qual])
        if sum_qual > big_qual:
            big_qual = sum_qual

        if seq_num <= 10:
            rev_comp_list.append(reverse_complement(seq))

    line_num += 1


print 'answer-3: {}'.format(big_seq)
print 'answer-4: {}'.format(big_qual)
print 'answer-5: {}'.format(rev_comp_list)
