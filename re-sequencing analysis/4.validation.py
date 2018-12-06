import os


os.system("mkdir 4.Validation")

val = open(r"4.Validation\4.validation.txt", "w")
com = open(r"3.Compare\3-1.compare.txt", "r")

comlines = com.readlines()
category = comlines[0]

i = 1
j = 1

val.write(category)

while i < len(comlines):
    if j < len(comlines) - 1:
        if comlines[i].split()[0] == comlines[j + 1].split()[0] and comlines[i].split()[1] == comlines[j + 1].split()[1]:
            val.write(comlines[j])
            print "node 1"
            j += 1
        elif i != j and comlines[i].split()[0] == comlines[j].split()[0] and comlines[i].split()[1] == comlines[j].split()[1]:
            val.write(comlines[j])
            print "node 2"
            j += 1
        elif comlines[i].split()[0] == comlines[j + 1].split()[0] and comlines[i].split()[1] != comlines[j + 1].split()[1]:
            j += 1
            print "node 3"
        elif i != j and comlines[i].split()[0] == comlines[j].split()[0] and comlines[i].split()[1] != comlines[j].split()[1]:
            j += 1
            print "node 4"
        else:
            i = j
            print "node 5"
    else:
        break

    
print "Validation success!"
