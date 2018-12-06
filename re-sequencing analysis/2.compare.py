import os


os.system("mkdir 2.Compare")

###################################################################################################################
#################################### Calling variant from illumina results ########################################
###################################################################################################################

date = [170331, 170410, 171027, 171102]
ind = 0

c = "A"
j = 1

for ind in range(0, 4):
    compare = open(r"2.Compare\2.Compare_%d.txt" %date[ind], "w")
    compare.write("Barcode\tPos\tRef\tVar(454)\tVar(ill)\tVarFreq(ill)\n")

    for i in range(1, 7):
        while ord(c) <= ord("H"):
            while j < 13:
                if not os.path.exists(r"1.Variant_from_454_ill_Results\454\1.%d_%s%d_var_%d.txt" %(i, c, j, date[ind])) or not os.path.exists(r"1.Variant_from_454_ill_Results\ill\1.%d_%s%d_var_ill.txt" %(i, c, j)):
                    j += 1
                    continue

                #print "Node 1"
                
                f = open(r"1.Variant_from_454_ill_Results\454\1.%d_%s%d_var_%d.txt" %(i, c, j, date[ind]), "r")
                g = open(r"1.Variant_from_454_ill_Results\ill\1.%d_%s%d_var_ill.txt" %(i, c, j), "r")

                flines = f.readlines()
                flines = flines[1:]
                glines = g.readlines()
                glines = glines[1:]
                
                tmp = str("%d_%s%d" %(i, c, j))
                
                for gline in glines:
                    decision = True
                    for fline in flines:
                        if fline.split()[0] == gline.split()[0] and (int(gline.split()[3]) + int(gline.split()[4])) >= 5:
                            compare.write(tmp + "\t" + fline.split()[0] + "\t" + fline.split()[1] + "\t" + fline.split()[-1] + "\t" + gline.split()[-1] + "\t" + gline.split()[-2] + "\n")
                            decision = False
                            break
                    if decision == True:
                        if float(gline.split()[-2][:-1]) >= 90.0 and (int(gline.split()[3]) + int(gline.split()[4])) >= 5:
                            compare.write(tmp + "\t" + gline.split()[0] + "\t" + gline.split()[1] + "\t" + gline.split()[1] + "\t" + gline.split()[-1] + "\t" + gline.split()[-2] + "\n")

                j += 1
                f.close()
                g.close()

            c = chr(ord(c) + 1)
            j = 1
            
        c = "A"
        j = 1   

    compare.close()


print "Compare completed"
