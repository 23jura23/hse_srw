#!/usr/bin/env python3
import vcf
import sys

if len(sys.argv) != 2:
    print("Usage: 1.py filename")
    exit(0)

reader = vcf.Reader(open(sys.argv[1], 'r'))

ploidy = -1

record = next(reader)
if len(record.samples) == 0:
    print("No individuals presented")
    exit(-1)

sample = record.samples[0]
GT = sample['GT']
ploidy = GT.count('/') + GT.count('|') + 1
print(ploidy)
