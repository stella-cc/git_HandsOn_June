#!/usr/bin/env python

#import modules
import sys, re
from argparse import ArgumentParser

#arguments
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

#convert input to uppercase
args.seq = args.seq.upper()              
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq):
        print ('The sequence is DNA') # if cointains T is DNA
    elif re.search('U', args.seq): # if contains U is RNA
        print ('The sequence is RNA')
    else: # if only contains A or G
        print ('The sequence can be DNA or RNA')
else: # if contains any other letter than AGTCU
    print ('The sequence is not DNA nor RNA')
