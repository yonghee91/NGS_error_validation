
old = open("Extract_with_ID_171103.txt", "r")
new = open("Extract_with_ID_171116.txt", "r")

analysis = open("5.LOD_171027_new_bead.txt", "w")

olines = old.readlines()
nlines = new.readlines()


for nline in nlines:
    decision = False

    for oline in olines:
        if nline == oline:
            decision = True
            break
        else:
            continue

    if decision == False:
        analysis.write(nline)
    
print "Analysis end!"

