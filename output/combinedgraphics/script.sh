#!/bin/sh
args=" "
for filename in ../files/Scale*; do
 	#echo $filename
 	args+="$filename "
done
args+="scaleFree"

python3 generateGraphics.py $args

