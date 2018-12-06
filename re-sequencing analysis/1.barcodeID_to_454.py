import os


os.system("mkdir 1.454_with_barcodeID")


# Assign plate&well barcode to first plate
f = open(r"Bead_extraction\plate_1.txt", "r")
g = open("well_number_1.txt", "r")
h = open(r"1.454_with_barcodeID\1.plate_1.txt", "w")

flines = f.readlines()
glines = g.readlines()


size = len(flines)

h.write("Barcode\tPos\tReads\tRef\t454_ID\n")
for i in range(0, size):
    h.write("1_" + glines[i].split()[1] + "\t" + "\t".join(flines[i].split()[6:]) + "\n")


f.close()
g.close()
h.close()



# Assign plate&well barcode to second~fifth plate
g = open("well_number_2~5.txt", "r")
glines = g.readlines()

for i in range(2, 6):
    f = open(r"Bead_extraction\plate_%d.txt" %i, "r")
    h = open(r"1.454_with_barcodeID\1.plate_%d.txt" %i, "w")

    flines = f.readlines()
    size = len(flines)

    h.write("Barcode\tPos\tReads\tRef\t454_ID\n")
    
    for j in range(0, size):
        h.write(str(i) + "_" + glines[j].split()[1] + "\t" + "\t".join(flines[j].split()[6:]) + "\n")

    f.close()
    h.close()



print "ID assignment success!"
