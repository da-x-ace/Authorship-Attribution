#!/usr/bin/env bash
#
# Runs the English PCFG parser on one or more files, printing trees only

FILES=/home/theusurper/NLP/authordetection/Data/train/others/*

for f in $FILES
do
  echo "Processing $f file..."
  scriptdir=`dirname $0`

  java -mx4g -cp "$scriptdir/*:" edu.stanford.nlp.parser.lexparser.LexicalizedParser -outputFormat "penn" edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz $f > $f.out
done

