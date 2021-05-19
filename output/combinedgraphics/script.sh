#!/bin/bash
args=" "
for filename in ../files/Scale*; do
 	echo $filename
 	args+="$filename "
done
args+="scalefree"

python3 generateGraphicsScaleFree.py $args

args=" "
for filename in ../files/Small*; do
 	echo $filename
 	args+="$filename "
done
args+="smallworld"
python3 generateGraphicsSmallWorld.py $args

args=" "
for filename in ../files/Random*; do
	echo $filename
	args+="$filename "
done
args+="random"
echo "ok"
echo $args
python3 generateGraphicsRandom.py $args
