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

'''
seq = open(r"C:\Users\yonghee91\Desktop\temp\454Analysis\3\Q5_extractedBEAD_seq_170522.fasta", "w")

for i in range(1,41):

    ID_barcode = open(r"C:\Users\yonghee91\Desktop\temp\454Analysis\2\2.ID_XY_barcode_Q5_"+str(i)+".txt", "r")
    ID_barcode_lines = ID_barcode.readlines()

    for ID_barcode_line in ID_barcode_lines:   
        for key in SeqIO.parse(r"C:\Users\yonghee91\Desktop\temp\1.TCA.454Reads_KAPA1&Q5.fna", 'fasta'):

            if str(">" + key.id) == ID_barcode_line.split()[0]:
                ID = str(ID_barcode_line)
                SEQ = str(key.seq)
                seq.write(ID + SEQ + '\n')
                break
                #i = i+1
                #print i
                #print key.seq

    ID_barcode.close()


seq.close()
 
print "end!"
'''

f = open(r"C:\Users\yonghee91\Desktop\temp\1.TCA.454Reads_KAPA1&Q5.fna", "r")
seq = open(r"C:\Users\yonghee91\Desktop\temp\454Analysis\3\Q5_extractedBEAD_seq_170522.fasta", "w")

f_lines = f.readlines()
ind = len(f_lines)

for i in range(1,45):

    ID_barcode = open(r"C:\Users\yonghee91\Desktop\temp\454Analysis\2\2.ID_XY_barcode_Q5_"+str(i)+".txt", "r")
    ID_barcode_lines = ID_barcode.readlines()

    for ID_barcode_line in ID_barcode_lines:   
        for j in range(0, ind):
            if f_lines[j].split()[0] == ID_barcode_line.split()[0]:
                ID = ID_barcode_line
                SEQ = ''
                while True:
                    j += 1
                    if j == ind or f_lines[j][0] == ">":
                        break
                    SEQ += f_lines[j][:-1]
                seq.write(ID + SEQ + '\n')
                break
                
    ID_barcode.close()


seq.close()
 
print "end!"

