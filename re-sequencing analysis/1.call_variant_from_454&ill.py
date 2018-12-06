import os


os.system("mkdir 1.Variant_from_454_ill_Results")

c = "A"
j = 1


###################################################################################################################
#################################### Calling variant from 454seq results ##########################################
###################################################################################################################

os.system(r"mkdir 1.Variant_from_454_ill_Results\454")

date = [170331, 170410, 171027, 171102]
ind = 0

for ind in range(0, 4):
    for i in range(1, 7):
        while ord(c) <= ord("H"):
            while j < 13:
                if not os.path.exists(r"cns_%d/%d_%s%d_cnsnew.txt" %(date[ind], i, c, j)):
                    j += 1
                    continue
                
                f = open(r"cns_%d/%d_%s%d_cnsnew.txt" %(date[ind], i, c, j), "r")
                g = open(r"1.Variant_from_454_ill_Results/454/1.%d_%s%d_var_%d.txt" %(i, c, j, date[ind]), "w")

                flines = f.readlines()

                size = len(flines)

                g.write("Pos\tRef\tCons\tReads1\tReads2\tVarFreq\tVarAllele\n")

                for k in range(1, size):
                    if flines[k].split()[2] == flines[k].split()[3]:
                        continue
                    g.write("\t".join(flines[k].split()[1:7]) + "\t" + flines[k].split()[-1] + "\n")

                j += 1
                f.close()
                g.close()

            c = chr(ord(c) + 1)
            j = 1
            
        c = "A"
        j = 1
        


print "Variant calling from 454 success!"





###################################################################################################################
#################################### Calling variant from illumina results ########################################
###################################################################################################################

os.system(r"mkdir 1.Variant_from_454_ill_Results\ill")

for i in range(1, 7):
    while ord(c) <= ord("H"):
        while j < 13:
            if not os.path.exists(r"cns_ill/1_%d_%s%d_cns.txt" %(i, c, j)):
                j += 1
                continue
                
            f = open(r"cns_ill/1_%d_%s%d_cns.txt" %(i, c, j), "r")
            g = open(r"1.Variant_from_454_ill_Results/ill/1.%d_%s%d_var_ill.txt" %(i, c, j), "w")

            flines = f.readlines()

            size = len(flines)

            g.write("Pos\tRef\tCons\tReads1\tReads2\tVarFreq\tVarAllele\n")

            for k in range(1, size):
                if flines[k].split()[2] == flines[k].split()[3]:
                    continue
                g.write("\t".join(flines[k].split()[1:7]) + "\t" + flines[k].split()[-1] + "\n")

            j += 1
            f.close()
            g.close()

        c = chr(ord(c) + 1)
        j = 1
            
    c = "A"
    j = 1


print "Variant calling from illumina success!"


    
