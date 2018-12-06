#!/bin/bash

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
	bwa mem ../../../Data/DesignSequence/"Expected_Sequence_genename_phusion_161117".fa ../../../Data/454_Result/Qval_10/copyline/sum_$BAR2.fa > ./1.BWA_samfiles/D_454_$BAR2.sam 
	samtools view -bt ../../../Data/DesignSequence/"Expected_Sequence_genename_phusion_161117".fa -o ./1.BWA_samfiles/"D_454_"$BAR2.bam ./1.BWA_samfiles/"D_454_"$BAR2.sam 
	samtools sort ./1.BWA_samfiles/"D_454_"$BAR2.bam  ./1.BWA_samfiles/"D_454_"$BAR2"_sorted".bam 
	samtools mpileup -f ../../../Data/DesignSequence/"Expected_Sequence_genename_phusion_161117".fa ./1.BWA_samfiles/"D_454_"$BAR2"_sorted.bam".bam > ./2.Mpileup_Varscan/"D_454_"$BAR2.mpileup 
	java -jar VarScan.v2.3.9.jar pileup2cns ./2.Mpileup_Varscan/"D_454_"$BAR2.mpileup --min-coverage 1 --min-reads2 1 > ./2.Mpileup_Varscan/"D_454_"$BAR2.cns

	echo "oo"

fi

done
