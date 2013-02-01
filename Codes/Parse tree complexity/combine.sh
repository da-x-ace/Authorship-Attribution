#!/usr/bin/env bash
#
# Runs the English PCFG parser on one or more files, printing trees only
cd ./pg
python ../combine.py $(ls *.f)

cd ../bh
python ../combine.py $(ls *.f)

cd ../jk
python ../combine.py $(ls *.f)

cd ../mw
python ../combine.py $(ls *.f)

cd ../others
python ../combine.py $(ls *.f)

cd ..
