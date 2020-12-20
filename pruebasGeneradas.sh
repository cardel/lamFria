#!/usr/bin/sh
for d in input/generated/*.txt ; do
    filename="${d##*/}"
    basename=${filename%.*}
    python3 lamfria.py --file $d -t Edge -o $basename & 
done
