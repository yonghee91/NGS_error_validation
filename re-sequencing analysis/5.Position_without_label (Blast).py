import os

if not os.path.exists(r"5.Position_without_label"):
    os.mkdir("5.Position_without_label")

##############################################################################################################
#################################### Calling variant from 454 results ########################################
##############################################################################################################

position = ["75", "50", "31", "58", "68", "38"]
date = [170331, 170410, 171027, 171102]
ind = 0

c = "A"
j = 1

if False:
    for ind in range(0, 4):
        compare = open(r"5.Position_without_label\1.Position_without_label_%d.txt" % date[ind], "w")
        compare.write("Barcode\tPos\tRef\tVar(454)\n")

        for i in range(1, 7):
            while ord(c) <= ord("H"):
                while j < 13:
                    if not os.path.exists(
                            r"1.Variant_from_454_ill_Results\454\1.%d_%s%d_var_%d.txt" % (i, c, j, date[ind])):
                        j += 1
                        continue

                    # print "Node 1"

                    f = open(r"1.Variant_from_454_ill_Results\454\1.%d_%s%d_var_%d.txt" % (i, c, j, date[ind]), "r")

                    flines = f.readlines()
                    flines = flines[1:]

                    tmp = str("%d_%s%d" % (i, c, j))

                    for fline in flines:
                        if fline.split()[0] in position:
                            compare.write(
                                tmp + "\t" + fline.split()[0] + "\t" + fline.split()[1] + "\t" + fline.split()[
                                    -1] + "\n")
                            break

                    j += 1
                    f.close()

                c = chr(ord(c) + 1)
                j = 1

            c = "A"
            j = 1

        compare.close()

        label = open(r"0.Barcode_LabelPosition\2.Barcode_Pos_%d.txt" % date[ind], "r")
        old_val = open(r"5.Position_without_label\1.Position_without_label_%d.txt" % date[ind], "r")
        new_val = open(r"5.Position_without_label\2.Position_without_label_final_%d.txt" % date[ind], "w")

        old_vallines = old_val.readlines()
        labellines = label.readlines()

        for old_valline in old_vallines:
            decision = True
            for labelline in labellines:
                if labelline.split()[0] == old_valline.split()[0] and labelline.split()[1] == old_valline.split()[1]:
                    decision = False
                    break

            if decision == True:
                new_val.write(old_valline)

        label.close()
        old_val.close()
        new_val.close()

if True:
    for ind in range(0, 4):
        allPos = open(r"5.Position_without_label\Observed(position)_%d.csv" % date[ind], "w")
        allPos.write("Barcode,Pos,Ref,Var(454)\n")

        for i in range(1, 7):
            while ord(c) <= ord("H"):
                while j < 13:
                    if not os.path.exists(
                            r"1.Variant_from_454_ill_Results\454\1.%d_%s%d_var_%d.txt" % (i, c, j, date[ind])):
                        j += 1
                        continue

                    # print "Node 1"

                    f = open(r"1.Variant_from_454_ill_Results\454\1.%d_%s%d_var_%d.txt" % (i, c, j, date[ind]), "r")

                    flines = f.readlines()
                    flines = flines[1:]

                    tmp = str("%d_%s%d" % (i, c, j))

                    for fline in flines:
                        if fline.split()[0] in position:
                            allPos.write(
                                tmp + "," + fline.split()[0] + "," + fline.split()[1] + "," + fline.split()[-1] + "\n")
                            break

                    j += 1
                    f.close()

                c = chr(ord(c) + 1)
                j = 1

            c = "A"
            j = 1

        allPos.close()

print "Extraction completed"
