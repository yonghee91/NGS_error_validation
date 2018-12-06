#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Taehoon Ryu
#
# Created:     24-10-2013
# Copyright:   (c) Taehoon Ryu 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

'''
import glob
import string
import xlrd
import xlwt
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Blast import NCBIWWW, NCBIXML
from Bio.Blast.Applications import NcbiblastnCommandline
from Bio.Blast import NCBIStandalone
'''

mapfile = open('04.THMappingResultOriginal.txt','r')

mapList = []

for i in xrange(151):
    mapList.append([])
    for j in xrange(411):
        mapList[i].append([])

for line in mapfile.readlines():
    temp = line.split()
    mapList[int(temp[0])/10][int(temp[1])/10].append((int(temp[0]),int(temp[1]),float(temp[2]),float(temp[3])))

mapfile.close()

f = open('Mismatch_total_LOD v3_with position_yes_filtering_171103.txt','r')

extraction_list_file = open('4.Extract_Mismatch_total_171103.txt','w')
ID_file = open('Extract_with_ID_171103.txt', 'w')

number = 0

for line in f.readlines() :
    mappable = False
    posX = int(float(line.split()[0]))
    posY = int(float(line.split()[1]))
    for postuple in mapList[posX/10][posY/10]:
        if postuple[0] == posX and postuple[1] == posY :
            extraction_list_file.write(str(postuple[2]) + "\t" + str(postuple[3]) + "\n")
            ID_file.write(line)
            mappable = True
            break

    #if mappable == False :
        #extraction_list_file.write("8723.0" + "\t" + "21748.0" + "\n")
   
    number += 1


print "end!"

f.close()
extraction_list_file.close()
ID_file.close()

