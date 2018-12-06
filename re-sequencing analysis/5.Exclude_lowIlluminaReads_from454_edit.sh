#!/bin/bash

grep -vwf 2.Result_Extract_low_illuReads_from_454merge.txt 1.COMPARISON_merge_diffCount.txt > 3.Result_Exclude_lowIlluminaReads_from_merge_D_454_Diffcount2.txt
