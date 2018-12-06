#/bin/bash

Var_total=0
ALL_total=0

for BAR in $(cat ../../../Data/ID_barcode_forBWA.txt)
do

	BAR2=$(echo $BAR | tr -d '\r')

FILE=../../../Data/454_Result/Qval_10/copyline/sum_$BAR2.fa
#FILESIZE=$(stat -c%s "$FILE")
FILESIZE=$(wc -c "$FILE" | awk '{print $1}')
echo $FILESIZE
echo $FILE

if [ "$FILESIZE" == "0" ]
then

	echo $FILE

else



	awk '(NR > 1) && ($3 != $4){split($7,VF,"%"); if (VF[1] > 95) printf $2" " $3" "$19" "$7"("$5" "$6") "FILENAME "\n" }' ./2.Mpileup_Varscan/"D_454_"$BAR2.cns > ./3.Difference_count/"D_454_"$BAR2"_diffCount" 

	ALL=$(cat ./2.Mpileup_Varscan/"D_454_"$BAR2.cns | wc -l) #> $BAR2"_seq_errorRate"
	#echo "\n" >> $BAR2"_seq_errorRate"
 
	Var=$(cat ./3.Difference_count/"D_454_"$BAR2"_diffCount" | wc -l) #>> $BAR2"_seq_errorRate"
	echo $ALL
	#Seq_error = int($(Var)) / int($(ALL)) >> $BAR2"_seq_errorRate"
	 

	ALL_total=$(expr $ALL_total + $ALL)
	Var_total=$(expr $Var_total + $Var)

fi

done 

Seq_error=$(echo "scale=4; $Var_total / $ALL_total" | bc) 


echo $ALL_total $Var_total $Seq_error > ./Result_ErrorRate/Error_rate.txt
#echo $Var >> 1.testresult

