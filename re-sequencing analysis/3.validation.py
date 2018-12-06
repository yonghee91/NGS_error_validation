import os


os.system("mkdir 3.Validation")

#####################################################################################################
#################################### Validating real variant ########################################
#####################################################################################################

position = ["75", "50", "31", "58", "68", "38"]
date = [170331, 170410, 171027, 171102]
ind = 0

for ind in range(0, 4):
    val = open(r"3.Validation\1.Validation_%d.txt" %date[ind], "w")
    com = open(r"2.Compare\2.Compare_%d.txt" %date[ind], "r")

    comlines = com.readlines()
    
    val.write(comlines[0])

    for i in range(1, len(comlines)):
        if float(comlines[i].split()[-1][:-1]) >= 90.0 and comlines[i].split()[1] in position:
            val.write(comlines[i])

    com.close()
    val.close()


    label = open(r"0.Barcode_LabelPosition\2.Barcode_Pos_%d.txt" %date[ind], "r")
    old_val = open(r"3.Validation\1.Validation_%d.txt" %date[ind], "r")
    new_val = open(r"3.Validation\2.Validation_final_%d.txt" %date[ind], "w")

    new_val.write("Barcode\tPos\tRef\tVar(454)\tVar(ill)\tVarFreq(ill)\n")

    old_vallines = old_val.readlines()
    labellines = label.readlines()

    for old_valline in old_vallines:
        decision = True
        for labelline in labellines:
            if (labelline.split()[0] == old_valline.split()[0] and labelline.split()[1] == old_valline.split()[1]) or old_valline.split()[-3] != old_valline.split()[-2]:
                decision = False
                break

        if decision == True:
            new_val.write(old_valline)

    label.close()
    old_val.close()
    new_val.close()
    
    
    
print "Validation success!"
