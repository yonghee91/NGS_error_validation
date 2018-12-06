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

i = 1
c = 'a'
j = 1

ind = 1

tp = raw_input("Enter a type of samples(KAPA1~2, Q5) : ")

analysis = open(r"D:\DNA synthesis\NGS validation\170523_454&illumina 분석\%s\%s_analysis.txt" %(tp, tp), "w")
low_reads = open(r"D:\DNA synthesis\NGS validation\170523_454&illumina 분석\%s\%s_low_reads.txt" %(tp, tp), "w")
                
analysis.write("Well" + "\t" + "Pos" + "\t" + "Ref" + "\t" + "454" + "\t" + "ill" + "\t" + "Freq" + "\t" + "(variant/normal)" + "\n")

while i < 45:
    while ord(c) <= ord('h'):
        while j <= 12:
            if not (os.path.exists(r"D:\DNA synthesis\NGS validation\170523_454&illumina 분석\%s\cns_454\%s_extractedBEAD_%d_%s%d.txt" %(tp, tp, i, c, j)) and os.path.exists(r"D:\DNA synthesis\NGS validation\170523_454&illumina 분석\%s\cns_illumina\%s_%d_%s%d.txt" %(tp, tp, i, c, j))):
                j += 1
                continue

            pyro = open(r"D:\DNA synthesis\NGS validation\170523_454&illumina 분석\%s\cns_454\%s_extractedBEAD_%d_%s%d.txt" %(tp, tp, i, c, j), "r")
            pyro_lines = pyro.readlines()

            ill = open(r"D:\DNA synthesis\NGS validation\170523_454&illumina 분석\%s\cns_illumina\%s_%d_%s%d.txt" %(tp, tp, i, c, j), "r")
            ill_lines = ill.readlines()

            if len(ill_lines) <= 1:
                pyro.close()
                ill.close()
                j += 1
                continue
            
            read_count = int(ill_lines[1].split()[4]) + int(pyro_lines[1].split()[5])
            #print read_count

            if pyro_lines[1][0] != '4' or ill_lines[1][0] != '4':
                j += 1
                continue
            
            if read_count <= 10:
                low_reads.write("%d_%s%d\n" %(i, c, j))
                j += 1
                continue

            align_position = int(ill_lines[1].split()[1]) - int(pyro_lines[1].split()[1])
            increment = abs(align_position)
            
            ind = 1

            if align_position >= 0:
                while True:
                    if pyro_lines[ind + increment].split()[2] != pyro_lines[ind + increment].split()[3]:
                        if ill_lines[ind].split()[2] == ill_lines[ind].split()[3]:
                            if pyro_lines[ind + increment].split()[6] != "0%":
                                analysis.write("%d_%s%d" %(i, c, j) + "\t" + pyro_lines[ind + increment].split()[1] + "\t" + pyro_lines[ind + increment].split()[2] + "\t" + pyro_lines[ind + increment].split()[-1] + "\t" + ill_lines[ind].split()[3] + "\t" + ill_lines[ind].split()[6] + "\t(" + ill_lines[ind].split()[5] + "/" + ill_lines[ind].split()[4] + ")\n")
                            else:
                                analysis.write("%d_%s%d" %(i, c, j) + "\t" + pyro_lines[ind + increment].split()[1] + "\t" + pyro_lines[ind + increment].split()[2] + "\t" + pyro_lines[ind + increment].split()[3] + "\t" + ill_lines[ind].split()[3] + "\t" + ill_lines[ind].split()[6] + "\t(" + ill_lines[ind].split()[5] + "/" + ill_lines[ind].split()[4] + ")\n")
                        else:
                            if pyro_lines[ind + increment].split()[6] != "0%" and ill_lines[ind].split()[6] != "0%":
                                analysis.write("%d_%s%d" %(i, c, j) + "\t" + pyro_lines[ind + increment].split()[1] + "\t" + pyro_lines[ind + increment].split()[2] + "\t" + pyro_lines[ind + increment].split()[-1] + "\t" + ill_lines[ind].split()[-1] + "\t" + ill_lines[ind].split()[6] + "\t(" + ill_lines[ind].split()[5] + "/" + ill_lines[ind].split()[4] + ")\n")
                            elif pyro_lines[ind + increment].split()[6] != "0%" and ill_lines[ind].split()[6] == "0%":
                                analysis.write("%d_%s%d" %(i, c, j) + "\t" + pyro_lines[ind + increment].split()[1] + "\t" + pyro_lines[ind + increment].split()[2] + "\t" + pyro_lines[ind + increment].split()[-1] + "\t" + ill_lines[ind].split()[3] + "\t" + ill_lines[ind].split()[6] + "\t(" + ill_lines[ind].split()[5] + "/" + ill_lines[ind].split()[4] + ")\n")
                            elif pyro_lines[ind + increment].split()[6] == "0%" and ill_lines[ind].split()[6] != "0%":
                                analysis.write("%d_%s%d" %(i, c, j) + "\t" + pyro_lines[ind + increment].split()[1] + "\t" + pyro_lines[ind + increment].split()[2] + "\t" + pyro_lines[ind + increment].split()[3] + "\t" + ill_lines[ind].split()[-1] + "\t" + ill_lines[ind].split()[6] + "\t(" + ill_lines[ind].split()[5] + "/" + ill_lines[ind].split()[4] + ")\n")
                            else:
                                analysis.write("%d_%s%d" %(i, c, j) + "\t" + pyro_lines[ind + increment].split()[1] + "\t" + pyro_lines[ind + increment].split()[2] + "\t" + pyro_lines[ind + increment].split()[3] + "\t" + ill_lines[ind].split()[3] + "\t" + ill_lines[ind].split()[6] + "\t(" + ill_lines[ind].split()[5] + "/" + ill_lines[ind].split()[4] + ")\n")

                    elif ill_lines[ind].split()[2] != ill_lines[ind].split()[3]:
                        if ill_lines[ind].split()[6] != "0%":
                            analysis.write("%d_%s%d" %(i, c, j) + "\t" + pyro_lines[ind + increment].split()[1] + "\t" + pyro_lines[ind + increment].split()[2] + "\t" + pyro_lines[ind + increment].split()[3] + "\t" + ill_lines[ind].split()[-1] + "\t" + ill_lines[ind].split()[6] + "\t(" + ill_lines[ind].split()[5] + "/" + ill_lines[ind].split()[4] + ")\n")
                        else:
                            analysis.write("%d_%s%d" %(i, c, j) + "\t" + pyro_lines[ind + increment].split()[1] + "\t" + pyro_lines[ind + increment].split()[2] + "\t" + pyro_lines[ind + increment].split()[3] + "\t" + ill_lines[ind].split()[3] + "\t" + ill_lines[ind].split()[6] + "\t(" + ill_lines[ind].split()[5] + "/" + ill_lines[ind].split()[4] + ")\n")
                       
                        
                    if ind + increment + 1 == len(pyro_lines) or ind + 1 == len(ill_lines) or ill_lines[ind + 1].split()[0] == "Chrom":
                        break
                    ind += 1

            else:
                while True:
                    if pyro_lines[ind].split()[2] != pyro_lines[ind].split()[3]:
                        if ill_lines[ind + increment].split()[2] == ill_lines[ind + increment].split()[3]:
                            if pyro_lines[ind].split()[6] != "0%":
                                analysis.write("%d_%s%d" %(i, c, j) + "\t" + pyro_lines[ind].split()[1] + "\t" + pyro_lines[ind].split()[2] + "\t" + pyro_lines[ind].split()[-1] + "\t" + ill_lines[ind + increment].split()[3] + "\t" + ill_lines[ind + increment].split()[6] + "\t(" + ill_lines[ind + increment].split()[5] + "/" + ill_lines[ind + increment].split()[4] + ")\n")
                            else:
                                analysis.write("%d_%s%d" %(i, c, j) + "\t" + pyro_lines[ind].split()[1] + "\t" + pyro_lines[ind].split()[2] + "\t" + pyro_lines[ind].split()[3] + "\t" + ill_lines[ind + increment].split()[3] + "\t" + ill_lines[ind + increment].split()[6] + "\t(" + ill_lines[ind + increment].split()[5] + "/" + ill_lines[ind + increment].split()[4] + ")\n")
                        else:
                            if pyro_lines[ind].split()[6] != "0%" and ill_lines[ind + increment].split()[6] != "0%":
                                analysis.write("%d_%s%d" %(i, c, j) + "\t" + pyro_lines[ind].split()[1] + "\t" + pyro_lines[ind].split()[2] + "\t" + pyro_lines[ind].split()[-1] + "\t" + ill_lines[ind + increment].split()[-1] + "\t" + ill_lines[ind + increment].split()[6] + "\t(" + ill_lines[ind + increment].split()[5] + "/" + ill_lines[ind + increment].split()[4] + ")\n")
                            elif pyro_lines[ind].split()[6] != "0%" and ill_lines[ind].split()[6] == "0%":
                                analysis.write("%d_%s%d" %(i, c, j) + "\t" + pyro_lines[indt].split()[1] + "\t" + pyro_lines[ind].split()[2] + "\t" + pyro_lines[ind].split()[-1] + "\t" + ill_lines[ind + increment].split()[3] + "\t" + ill_lines[ind + increment].split()[6] + "\t(" + ill_lines[ind + increment].split()[5] + "/" + ill_lines[ind + increment].split()[4] + ")\n")
                            elif pyro_lines[ind].split()[6] == "0%" and ill_lines[ind].split()[6] != "0%":
                                analysis.write("%d_%s%d" %(i, c, j) + "\t" + pyro_lines[ind].split()[1] + "\t" + pyro_lines[ind].split()[2] + "\t" + pyro_lines[ind].split()[3] + "\t" + ill_lines[ind + increment].split()[-1] + "\t" + ill_lines[ind + increment].split()[6] + "\t(" + ill_lines[ind + increment].split()[5] + "/" + ill_lines[ind + increment].split()[4] + ")\n")
                            else:
                                analysis.write("%d_%s%d" %(i, c, j) + "\t" + pyro_lines[ind].split()[1] + "\t" + pyro_lines[ind].split()[2] + "\t" + pyro_lines[ind].split()[3] + "\t" + ill_lines[ind + increment].split()[3] + "\t" + ill_lines[ind + increment].split()[6] + "\t(" + ill_lines[ind + increment].split()[5] + "/" + ill_lines[ind + increment].split()[4] + ")\n")

                    elif ill_lines[ind + increment].split()[2] != ill_lines[ind + increment].split()[3]:
                        if ill_lines[ind].split()[6] != "0%":
                            analysis.write("%d_%s%d" %(i, c, j) + "\t" + pyro_lines[ind].split()[1] + "\t" + pyro_lines[ind].split()[2] + "\t" + pyro_lines[ind].split()[3] + "\t" + ill_lines[ind + increment].split()[-1] + "\t" + ill_lines[ind + increment].split()[6] + "\t(" + ill_lines[ind + increment].split()[5] + "/" + ill_lines[ind + increment].split()[4] + ")\n")
                        else:
                            analysis.write("%d_%s%d" %(i, c, j) + "\t" + pyro_lines[ind].split()[1] + "\t" + pyro_lines[ind].split()[2] + "\t" + pyro_lines[ind].split()[3] + "\t" + ill_lines[ind + increment].split()[3] + "\t" + ill_lines[ind + increment].split()[6] + "\t(" + ill_lines[ind + increment].split()[5] + "/" + ill_lines[ind + increment].split()[4] + ")\n")
                       
                    if ind + 1 == len(pyro_lines) or ind + increment + 1 == len(ill_lines) or ill_lines[ind + increment + 1].split()[0] == "Chrom":
                        break
                    ind += 1


            print "%d_%s%d" %(i, c, j)

            
            j += 1
            ill.close()
            pyro.close()


            
        j = 1
        c = chr(ord(c) + 1)
    c = 'a'
    i += 1

    if not os.path.exists(r"D:\DNA synthesis\NGS validation\170523_454&illumina 분석\%s\cns_454\%s_extractedBEAD_%d_%s%d.txt" %(tp, tp, i, c, j)):
        if os.path.exists(r"D:\DNA synthesis\NGS validation\170523_454&illumina 분석\%s\cns_454\%s_extractedBEAD_%d_%s%d.txt" %(tp, tp, i, c, j + 1)) or os.path.exists(r"D:\DNA synthesis\NGS validation\170523_454&illumina 분석\%s\cns_454\%s_extractedBEAD_%d_%s%d.txt" %(tp, tp, i, c, j + 2)):
            continue
        else:
            break

analysis.close()
low_reads.close()

print "End!!"
