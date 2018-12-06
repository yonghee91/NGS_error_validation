#######################################################################################
#
#
# Code by Yonghee(17.05.25)
#
#
#
#
#
#######################################################################################

import os

tp = raw_input("Enter a type of samples(KAPA1~2, Q5) : ")

validation = open(r"D:\DNA synthesis\NGS validation\170523_454&illumina 분석\%s\%s_analysis.txt" %(tp, tp), "r")
val_lines = validation.readlines()

real = open(r"D:\DNA synthesis\NGS validation\170523_454&illumina 분석\%s\%s_real_variant.txt" %(tp, tp), "w")
real.write("Well" + "\t" + "Pos" + "\t" + "Ref" + "\t" + "454" + "\t" + "ill" + "\t" + "Freq" + "\t" + "(variant/normal)" + "\n")
real_count = 0

error = open(r"D:\DNA synthesis\NGS validation\170523_454&illumina 분석\%s\%s_sequencing_error.txt" %(tp, tp), "w")
error.write("Well" + "\t" + "Pos" + "\t" + "Ref" + "\t" + "454" + "\t" + "ill" + "\t" + "Freq" + "\t" + "(variant/normal)" + "\n")
error_count = 0

etc = open(r"D:\DNA synthesis\NGS validation\170523_454&illumina 분석\%s\%s_only_illumina.txt" %(tp, tp), "w")
etc.write("Well" + "\t" + "Pos" + "\t" + "Ref" + "\t" + "454" + "\t" + "ill" + "\t" + "Freq" + "\t" + "(variant/normal)" + "\n")
etc_count = 0

a_to_g = 0
a_to_t = 0
a_to_c = 0

g_to_a = 0
g_to_t = 0
g_to_c = 0

t_to_a = 0
t_to_g = 0
t_to_c = 0

c_to_a = 0
c_to_g = 0
c_to_t = 0


for i in range(1, len(val_lines) - 1):
    if val_lines[i].split()[2] != val_lines[i].split()[3] and val_lines[i].split()[3] == val_lines[i].split()[4] and val_lines[i].split()[3] != "N":
        if float(val_lines[i].split()[5][:-1]) >= 95.0:
            real.write(val_lines[i])
            real_count += 1
            if val_lines[i].split()[2] == "A" and val_lines[i].split()[3] == "G":
                a_to_g += 1
            elif val_lines[i].split()[2] == "A" and val_lines[i].split()[3] == "T":
                a_to_t += 1
            elif val_lines[i].split()[2] == "A" and val_lines[i].split()[3] == "C":
                a_to_c += 1
                
            elif val_lines[i].split()[2] == "G" and val_lines[i].split()[3] == "A":
                g_to_a += 1
            elif val_lines[i].split()[2] == "G" and val_lines[i].split()[3] == "T":
                g_to_t += 1
            elif val_lines[i].split()[2] == "G" and val_lines[i].split()[3] == "C":
                g_to_c += 1

            elif val_lines[i].split()[2] == "T" and val_lines[i].split()[3] == "A":
                t_to_a += 1
            elif val_lines[i].split()[2] == "T" and val_lines[i].split()[3] == "G":
                t_to_g += 1
            elif val_lines[i].split()[2] == "T" and val_lines[i].split()[3] == "C":
                t_to_c += 1

            elif val_lines[i].split()[2] == "C" and val_lines[i].split()[3] == "A":
                c_to_a += 1
            elif val_lines[i].split()[2] == "C" and val_lines[i].split()[3] == "G":
                c_to_g += 1
            elif val_lines[i].split()[2] == "C" and val_lines[i].split()[3] == "T":
                c_to_t += 1

                
    elif val_lines[i].split()[2] != val_lines[i].split()[3] and val_lines[i].split()[2] == val_lines[i].split()[4]:
        error.write(val_lines[i])
        if val_lines[i].split()[3] != "N":
            error_count += 1
    elif val_lines[i].split()[2] != val_lines[i].split()[4] and val_lines[i].split()[3] != val_lines[i].split()[4]:
        if float(val_lines[i].split()[5][:-1]) >= 95.0:
            etc.write(val_lines[i])
            etc_count += 1

print """
Real variant\t%d
Seq. error\t%d
Only illumina\t%d

A->G\t%d
A->T\t%d
A->C\t%d
G->A\t%d
G->T\t%d
G->C\t%d
T->A\t%d
T->G\t%d
T->C\t%d
C->A\t%d
C->G\t%d
C->T\t%d
""" %(real_count, error_count, etc_count, a_to_g, a_to_t, a_to_c, g_to_a, g_to_t, g_to_c, t_to_a, t_to_g, t_to_c, c_to_a, c_to_g, c_to_t)

real.write("#_of_real_variant\t%d" %real_count)
real.write("""
\tA->G\t%d
\tA->T\t%d
\tA->C\t%d
\tG->A\t%d
\tG->T\t%d
\tG->C\t%d
\tT->A\t%d
\tT->G\t%d
\tT->C\t%d
\tC->A\t%d
\tC->G\t%d
\tC->T\t%d
""" %(a_to_g, a_to_t, a_to_c, g_to_a, g_to_t, g_to_c, t_to_a, t_to_g, t_to_c, c_to_a, c_to_g, c_to_t))
error.write("#_of_sequencine_error\t%d" %error_count)
etc.write("#_of_only_illumina\t%d" %etc_count)

real.close()
error.close()
etc.close()

"""
real = open(r"D:\DNA synthesis\NGS validation\170523_454&illumina 분석\%s\%s_real_variant.txt" %(tp, tp), "r")
error = open(r"D:\DNA synthesis\NGS validation\170523_454&illumina 분석\%s\%s_sequencing_error.txt" %(tp, tp), "r")
etc = open(r"D:\DNA synthesis\NGS validation\170523_454&illumina 분석\%s\%s_only_illumina.txt" %(tp, tp), "r")

real_lines = real.readlines()
error_lines = error.readlines()
etc_lines = etc.readlines()
print len(real_lines) - 2, len(error_lines) - 2, len(etc_lines) - 2
real.close()
error.close()
etc.close()
"""

print "End"
