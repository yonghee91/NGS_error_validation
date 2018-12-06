#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      heeran
# Revised :    Yonghee
#
# Created:     19-02-2016
# Copyright:   (c) heeran 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------


from Bio import SeqIO
from Bio.Seq import Seq

i_list = list(range(1,41))

f = open(r"C:\Users\yonghee91\Desktop\temp\1.TCA.454Reads_KAPA1&Q5.fna", "r")
barcode = open(r"C:\Users\yonghee91\Desktop\temp\well_barcode.txt", "r")

f_lines = f.readlines()
barcode_lines = barcode.readlines()

for i in i_list:
   
    seqRESULT_XY = open(r"C:\Users\yonghee91\Desktop\temp\454Analysis\1\1.only454XY_Q5_" + str(i) + ".txt", "r")
    ID_list = open(r"C:\Users\yonghee91\Desktop\temp\454Analysis\2\2.ID_XY_barcode_Q5_" + str(i) + ".txt", "w")

    
    seqRESULT_XY_lines = seqRESULT_XY.readlines()
    
    ind = 0
    for seqRESULT_XY_line in seqRESULT_XY_lines:
        if seqRESULT_XY_line.split()[0] == "no":
            print "%d : no mapping!!" %i
            # ID_list.write('no mapping!!\n')

        else:
            X = 'x=' + seqRESULT_XY_line.split()[0] + '.0'
            Y = 'y=' + seqRESULT_XY_line.split()[1] + '.0'
            '''
            for f_line in f_lines:
                if ">" in f_line:
                    #print f_line.split()[2]
                    if (f_line.split()[2] == X) and (f_line.split()[3] == Y):
                        ID = f_line.split()[0]
                        ID_list.write(seqRESULT_XY_line.split()[0]+'\t'+seqRESULT_XY_line.split()[1]+'\t'+ID+'\n')
            '''
            for f_line in f_lines:
                if ">" in f_line and (f_line.split()[2] == X) and (f_line.split()[3] == Y):
                    ID = f_line.split()[0]
                    ID_list.write(ID + '\t' + seqRESULT_XY_line[:-1] + "\t" + str(i) + "_" + barcode_lines[ind])
                    break
        ind += 1

            
    seqRESULT_XY.close()
    ID_list.close()

f.close()
barcode.close()

print "end"

