#!/bin/bash

cat ../../../D_illumina/3.Difference_count/"1-2.NoRepeat_Result_onlyBAR_illu_lower_than20_Reads.txt" | while read line
do
	#L=$(echo $line | awk '{printf $1'})

	L2=$(echo $line | awk '{split($0,BAR,"."); printf BAR[1]'})

	awk '{if("'${L2}'"==$5)printf $0"\n" >> "2.Result_Extract_low_illuReads_from_454merge.txt" }' 1.COMPARISON_merge_diffCount.txt 
done 

#awk '{print $1}' result.sam 
#awk '{printf "'${ID}'"}'
