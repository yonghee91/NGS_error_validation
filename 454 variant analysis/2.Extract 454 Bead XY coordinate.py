#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Huiran Yeom
# revised:     Yonghee Lee
#
# Created:     12-07-2014
# Copyright:   (c) Taehoon Ryu 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os.path
import Bio.SeqIO
import subprocess


for i in range(1, 7):
    f = open(r'bc_split\bc_labelF%d.fasta' %i,'r')
    g = open('2.XY_coordinate_labelF%d.txt' %i,'w')

    for line in f.readlines():
        if '>' == line[0] :
            temp = line.split()
            Xpos = float(temp[2][2:])
            Ypos = float(temp[3][2:])
            g.write('%.1f\t%.1f\n'%(Xpos, Ypos))

    f.close()
    g.close()

print "2.Extract 454 Bead XY coordinate.py good!"
