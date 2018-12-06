#######################################################################################
#
#
# Code by Yonghee(17.05.25)
#
#   ** This code is very naive, not optimized
#   ** Rather than python code, shell code would be better!
#
#
#######################################################################################

import os

ind = 1

tp = raw_input("Enter a type of samples(KAPA1~2, Q5) : ")

analysis = open(r"D:\DNA synthesis\170530_illumina_unmatched\%s_analysis.txt" %tp, "w")
analysis.write("Pos" + "\t" + "Ref" + "\t" + "ill" + "\t" + "Var" + "\t" + "Freq" + "\t" + "(variant/normal)" + "\n")

ill = open(r"D:\DNA synthesis\170530_illumina_unmatched\%s.unmatched_cns.txt" %tp, "r")
ill_lines = ill.readlines()

while True:
    if ill_lines[ind].split()[0] != "4":
        print "Not interested!"
        break
    
    if ill_lines[ind].split()[6] == "0%":
        analysis.write(ill_lines[ind].split()[1] + "\t" + ill_lines[ind].split()[2] + "\t" + ill_lines[ind].split()[3] + "\t" + "N" + "\t" + ill_lines[ind].split()[6] + "\t(" + ill_lines[ind].split()[5] + "/" + ill_lines[ind].split()[4] + ")\n")
    else:
        analysis.write(ill_lines[ind].split()[1] + "\t" + ill_lines[ind].split()[2] + "\t" + ill_lines[ind].split()[3] + "\t" + ill_lines[ind].split()[-1] + "\t" + ill_lines[ind].split()[6] + "\t(" + ill_lines[ind].split()[5] + "/" + ill_lines[ind].split()[4] + ")\n")

    if ind + 1 == len(ill_lines) or ill_lines[ind + 1].split()[0] == "Chrom":
        break
    ind += 1


analysis.close()


print "End!!"
