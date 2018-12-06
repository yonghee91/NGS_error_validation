import os


position = ['75', '50', '31', '58', '68', '38']
 
f = open('Mismatch_total_LOD v3_with position_171116.txt', 'r')

g1 = open('3.Mismatch_total_LOD_with position_no_filtering_171027_new.txt', 'w')
g2 = open('3.Mismatch_total_LOD_with position_yes_filtering_171027_new.txt', 'w')

flines = f.readlines()


'''
tmp = 0
for fline in flines:
        decide = 1
        if fline.split()[5] != '75' and fline.split()[5] != '50' and fline.split()[5] != '31' and fline.split()[5] != '58' and fline.split()[5] != '68':
            tmp += 1
print tmp

'''

# 아래 코드는 매우 naive한 코드로, 파일 크기가 커질수록 running time이 기하급수적으로 증가함. O(n^2)의 쓰레기 성능의 코드임을 감안할 것!

for i in range(1, 7):
    h = open('2.XY_coordinate_labelF%d.txt' %i, 'r')
    hlines = h.readlines()

    for fline in flines:
        decide = 1
        if fline.split()[5] == position[i - 1]:
            g1.write(fline)
            for hline in hlines:
                if fline.split()[0] == hline.split()[0] and fline.split()[1] == hline.split()[1]:
                    #print fline.split()[0], hline.split()[0], fline.split()[1], hline.split()[1]
                    decide = 0
                    break
        if decide == 0:
            continue
        if fline.split()[5] == position[i - 1]:
            g2.write(fline)


    h.close()
    print "labelF%d filtering success!" %i

'''
h = open('2.XY_coordinate_labelF6.txt', 'r')
hlines = h.readlines()

for fline in flines:
    decide = 1
    if fline.split()[5] == '34':
        g1.write(fline)
    for hline in hlines:
        if fline.split()[0] == hline.split()[0] and fline.split()[1] == hline.split()[1]:
            #print fline.split()[0], hline.split()[0], fline.split()[1], hline.split()[1]
            decide = 0
            break
    if decide == 0:
        continue
    if fline.split()[5] == '34':
        g2.write(fline)


h.close()

'''

f.close()
g1.close()
g2.close()

print "End"
