#!/bin/sh

for exp in "prune" "branch" "var" "cmp"
do
	$(python3 reproduce.py --exp $exp)
done