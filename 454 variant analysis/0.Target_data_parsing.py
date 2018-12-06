#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      huiran Yeom
#
# Created:     24-10-2013
# Copyright:   (c) Taehoon Ryu 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import time
from multiprocessing import Process, Queue
import string
from Bio.Seq import Seq
from Bio.Blast import NCBIStandalone

import fileinput
import glob


OutFile = r'Blast\out\02.blast_result_total.txt'

f = open(OutFile,'r')

Mismatch_total_file = open('Mismatch_total_LOD v3_171103.txt','w')

blast_parser = NCBIStandalone.BlastParser()
print blast_parser
iterator = NCBIStandalone.Iterator(f,blast_parser)


for record in iterator :
    for alignment in record.alignments :
        for hsp in alignment.hsps :
            mismatch_Number = (hsp.identities[1]-( hsp.identities[0] + hsp.gaps[0] ))
            Gaps_Number = hsp.gaps[0]
            if ( mismatch_Number != 0) :                
                Mismatch_total_file.write('%s\t%s\t%s\t%s\n'%(record.query,alignment.title,mismatch_Number,Gaps_Number))

f.close()
Mismatch_total_file.close()

print 'end'

