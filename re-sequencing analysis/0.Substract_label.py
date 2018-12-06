import os
import glob


os.system("mkdir 0.Barcode_LabelPosition")


position = ["75", "50", "31", "58", "68", "38"]

date = [170331, 170410, 171027, 171102]
ind = 0


#################################################################################################################################
#################################### 1. Extracting 454ID&position from bc_splitted files ########################################
#################################################################################################################################

for ind in range(0, 4):
    ID = open(r"0.Barcode_LabelPosition/1.454ID_Pos_%d.txt" %date[ind], "w")
    
    for i in range(1, 7):
        bcfile = glob.glob(r"Barcode_split/%d/*labelF%d.fasta" %(date[ind], i))

        f = open(bcfile.pop(), "r")
        flines = f.readlines()

        j = 0
        while j < len(flines):
            ID.write(flines[j].split()[0][1:] + "\t" + position[i - 1] + "\n")
            j += 2
        f.close()
        

    ID.close()

print "Extraction completed"


#################################################################################################################################
#################################### 2. Merging plate/well barcode with label position ##########################################
#################################################################################################################################


for ind in range(0, 4):
    f = open("Barcode_454ID/0.(ill_new)Barcode_454ID_new_%d.txt" %date[ind], "r")
    g = open("0.Barcode_LabelPosition/1.454ID_Pos_%d.txt" %date[ind], "r")

    Bar = open("0.Barcode_LabelPosition/2.Barcode_Pos_%d.txt" %date[ind], "w")

    flines = f.readlines()
    glines = g.readlines()

    for fline in flines:
        for gline in glines:
            if fline.split()[1] == gline.split()[0]:
                Bar.write(fline.split()[0] + "\t" + gline.split()[1] + "\n")

    f.close()
    g.close()
    Bar.close()


print "Merging completed"











