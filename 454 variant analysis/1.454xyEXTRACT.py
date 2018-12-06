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

i_list = list(range(5,45))

f = open(r"C:\Users\yonghee91\Desktop\temp\THMappingResultOriginal_KAPA2.txt", "r")
f_lines = f.readlines()

for i in i_list:
    
    plate_XY = open(r"C:\Users\yonghee91\Desktop\temp\KAPA2\2.Extraction_Mismatch_KAPA_"+str(i)+".txt", "r")
    newXY= open(r"C:\Users\yonghee91\Desktop\temp\454Analysis\1\1.only454XY_KAPA2_"+str(i)+".txt", "w")

    plate_XY_lines = plate_XY.readlines()


    for plate_XY_line in plate_XY_lines:
        '''
        if ("No" in plate_XY_line) and ("Mapping!!" in plate_XY_line):
                print "no mapping!!"
                newXY.write("no mapping!!\n")
        '''
        cnt = 0
        for f_line in f_lines:               
            if (plate_XY_line.split()[0] == f_line.split()[2]) and (plate_XY_line.split()[1] == f_line.split()[3]):
                X = f_line.split()[0]
                Y = f_line.split()[1]
                newXY.write(X + '\t' + Y + '\n')
                cnt = 1
                break
                
                '''
                if (plate_XY_line.split()[0] == f_line.split()[2]) and (plate_XY_line.split()[1] == f_line.split()[3]):
                    count += 1
                    #print plate_XY_line.split()[0]+"\t"+plate_XY_line.split()[1]
                    X = f_line.split()[0]
                    Y = f_line.split()[1]
                    newXY.write(X + '\t' + Y + '\n')
                    
                    if count > 1:
                        print count
                        print f_line.split()[1]
                        break
                    else:

                        #print plate_XY_line.split()[0]
                        #print f_line.split()[2]
                        #print plate_XY_line.split()[1]
                        #print f_line.split()[3]
                        #print i
                        X = f_line.split()[0]
                        Y = f_line.split()[1]
                        #newXY.write(X + '\t' + Y + '\t' + f_line.split()[2] + '\t' + f_line.split()[3] + '\n')
                        newXY.write(X + '\t' + Y + '\n')
                '''
                        
            elif ((plate_XY_line.split()[0] + ".0" == f_line.split()[2]) and (plate_XY_line.split()[1] == f_line.split()[3])) :                    
                X = f_line.split()[0]
                Y = f_line.split()[1]
                #newXY.write(X + '\t' + Y + '\t' + f_line.split()[2] + '\t'+f_line.split()[3] + '\n')
                newXY.write(X + '\t' + Y + '\n')
                cnt = 1
                break
            elif ((plate_XY_line.split()[0] == f_line.split()[2]) and (plate_XY_line.split()[1]+".0" == f_line.split()[3])):
                X = f_line.split()[0]
                Y = f_line.split()[1]
                #newXY.write(X + '\t' + Y + '\t' + f_line.split()[2] + '\t' + f_line.split()[3] + '\n')
                newXY.write(X + '\t' + Y + '\n')
                cnt = 1
                break
            elif ((plate_XY_line.split()[0] + ".0" == f_line.split()[2]) and (plate_XY_line.split()[1] + ".0" == f_line.split()[3])):
                X = f_line.split()[0]
                Y = f_line.split()[1]
                #newXY.write(X + '\t' + Y + '\t' + f_line.split()[2] + '\t' + f_line.split()[3] + '\n')
                newXY.write(X + '\t' + Y + '\n')
                cnt = 1
                break
            
            # else:
                # print "No mapping : " + plate_XY_line


        if cnt != 1:
            print "%d : no mapping!!" %i
            newXY.write("no mapping!!\n")
      
    plate_XY.close()
    newXY.close()

f.close()

print "end"
