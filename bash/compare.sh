#!/bin/bash

read num 
read nnum

if (("$num" > "$nnum"))
then
	echo "X is greater than Y"
fi
if (("$num" < "$nnum"))
then
	echo "X is less than Y"
fi
if [ "$num" -eq "$nnum" ]
then
	echo "X is equal to Y"
fi