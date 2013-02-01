#!/usr/bin/env bash
#
# Runs the English PCFG parser on one or more files, printing trees only

for f in $(find ./* -type d)
do
	echo $f
	cd $f
	for k in $(ls *.out); do
		echo "Processing $k file..."
		python ../extract.py $k $k.f
	done
	cd ..
	pwd
done

