import os


os.system("mkdir 2.Variant_from_illumina_Results")

c = "A"
j = 1


for i in range(1, 7):
    while ord(c) <= ord("H"):
        while j < 13:
            if not os.path.exists(r"consensus\1_%d_%s%d_cns.txt" %(i, c, j)):
                j += 1
                continue
            
            f = open(r"consensus\1_%d_%s%d_cns.txt" %(i, c, j), "r")
            g = open(r"2.Variant_from_illumina_Results\2.%d_%s%d.txt" %(i, c, j), "w")

            flines = f.readlines()

            size = len(flines)

            g.write("Pos\tRef\tCons\tReads1\tReads2\tVarFreq\tVarAllele\n")

            for k in range(1, size):
                if flines[k].split()[2] == flines[k].split()[3]:
                    continue
                g.write("\t".join(flines[k].split()[1:7]) + "\t" + flines[k].split()[-1] + "\n")

            j += 1

        c = chr(ord(c) + 1)
        j = 1
        
    c = "A"
    j = 1
    


print "Variant calling from illumina success!"
