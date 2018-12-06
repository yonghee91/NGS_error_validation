#!/bin/bash

awk '{ split($6,BAR,"D_454_"); split(BAR[2],BAR2,"."); print $1,$2,$3,$4"+"$5,BAR2[1]}' 0.merge_diffCount > 1.COMPARISON_merge_diffCount.txt
