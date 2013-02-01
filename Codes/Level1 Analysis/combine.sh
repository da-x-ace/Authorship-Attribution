#!/usr/bin/env bash
#
# Runs the English PCFG parser on one or more files, printing trees only

python ./combine.py $(ls pg/*.f)
