#!/bin/bash
while IFS=$'\t' read -r f1 f2 f3 f4
do
	samtools faidx "$1" "$f2:$f3-$f4" > "$f2"_"$f3"-"$f4.fa"
done < <(tail -n +2 "$2")
