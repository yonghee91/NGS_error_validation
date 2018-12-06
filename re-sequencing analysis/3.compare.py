import os


os.system("mkdir 3.Compare")

c = "A"
j = 1

compare = open(r"3.Compare\3-1.compare.txt", "w")

compare.write("Barcode\tPos\tRef\tVar\tReads1\tReads2\tVarFreq\tRemarks\n")

for i in range(1, 6):

    f = open(r"1.454_with_barcodeID\1.plate_%d.txt" %i, "r")
    flines = f.readlines()
    size = len(flines)
    
    while ord(c) <= ord("H"):
        while j < 13:
            if not os.path.exists(r"2.Variant_from_illumina_Results\2.%d_%s%d.txt" %(i, c, j)):
                j += 1
                continue
            
            g = open(r"2.Variant_from_illumina_Results\2.%d_%s%d.txt" %(i, c, j), "r")

            glines = g.readlines()
            glines = glines[1:]

            tmp = str("%d_%s%d" %(i, c, j))
            #print tmp
            
            for k in range(1, size):  
                if not tmp == flines[k].split()[0] or len(flines[k].split()) == 1:
                    continue
                
                for gline in glines:
                    if float(gline.split()[5][:-1]) >= 90.0 or (flines[k].split()[1] == gline.split()[0] and float(gline.split()[5][:-1]) >= 90.0):
                        compare.write(tmp + "\t" + flines[k].split()[1] + "\t" + flines[k].split()[3] + "\t" + flines[k].split()[2] + "\t0\t1\t100%\t454\n")
                        compare.write(tmp + "\t" + "\t".join(gline.split()[0:2]) + "\t" + gline.split()[-1] + "\t" + "\t".join(gline.split()[3:6]) + "\tillumina\n")
                        break

            j += 1
            g.close()

        c = chr(ord(c) + 1)
        j = 1
        
    c = "A"
    j = 1

    f.close()
    

compare.close()


f = open(r"3.Compare\3-1.compare.txt", "r")
flines = f.readlines()
category = flines[0]

size = len(flines)

c = "A"
index = 1

date = [171027, 171027, 171102, 170331, [170410, 171027, 171102]]

for i in range(1, 6):
    if not i == 5:
        g = open(r"3.Compare\3-2.compare_%d_%d.txt" %(i, date[i - 1]), "w")

        g.write(category)
        for k in range(index, size):  
            if not flines[k][0] == str(i):
                index = k
                break
            g.write(flines[k])
        g.close()
        

    else:
        g = open(r"3.Compare\3-2.compare_%d_%d.txt" %(i, date[i - 1][0]), "w")
        g.write(category)        
        for k in range(index, size):
            if not ord(flines[k][2]) <= ord("D"):
                index = k
                break
            g.write(flines[k])
        g.close()

        g = open(r"3.Compare\3-2.compare_%d_%d.txt" %(i, date[i - 1][1]), "w")
        g.write(category)
        for k in range(index, size):
            if not flines[k][2] == "E":
                index = k
                break
            g.write(flines[k])
        g.close()

        g = open(r"3.Compare\3-2.compare_%d_%d.txt" %(i, date[i - 1][2]), "w")    
        g.write(category)
        for k in range(index, size):
            if not ord(flines[k][2]) <= ord("H"):
                index = k
                break
            g.write(flines[k])
        g.close()
        


print "Comparison success!"
