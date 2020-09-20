#!/usr/bin/env python3
import vcf
import sys
import re

if len(sys.argv) != 3:
    print("Usage: 2.py filename individual_name")
    exit(0)

reader = vcf.Reader(open(sys.argv[1], 'r'))

ind_name = sys.argv[2]

positions = []
histogram_dct = {}

if ind_name not in reader.samples:
    print("Required individual is not presented in file")
    exit(-1)

def heterozygous(call):
    alleles = re.split('/|\|', call['GT'])
    if alleles[0] != alleles[1]:
        return 1
    else:
        return 0

pos = 0

for record in reader:
    call = record.genotype(ind_name)
    if heterozygous(call):
        positions.append(pos)
    pos += 1

for i in range(len(positions)):
    for j in range(i+1,len(positions)):
        pi, pj = positions[i], positions[j]
        length = pj-pi
        if length not in histogram_dct:
            histogram_dct[length] = 1
        else:
            histogram_dct[length] += 1

histogram = [0]*pos # pos = number of records
for (length, cnt) in histogram_dct.items():
    histogram[length] = cnt

print(histogram)
