import os

tp = raw_input("Enter a type of samples(KAPA1~2, Q5) : ")

unmatched = open("%s.unmatched.fastq" %tp, "r")
aligned = open("%s.unmatched.sam" %tp, "r")

unmatched_lines = unmatched.readlines()
aligned_lines = aligned.readlines()

count1 = 0
count2 = 0

for line1 in unmatched_lines:
    if line1[:7] == "@M02595":
        count1 += 1

for line2 in aligned_lines:
    if line2.split()[0][:6] == "M02595" and line2.split()[2] == "4":
        count2 += 1

print count1, count2
print "End"
