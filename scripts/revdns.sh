#!/bin/sh

while read ip; do
	host $ip $2
done < $1
