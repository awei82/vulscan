#!/bin/bash

# Wrapper script to aggregate nmap's output and pipe to STDOUT
# pass in all arguments to nmap as usual, leaving out the output flag.
# outputs will be saved to results.*, then be printed to STDOUT

rm -f results.gnmap
rm -f results.xml

# default to showing help menu
if [ "$#" -lt 1 ]; then
    nmap -h
    exit
fi

nmap -oA results $@

#printf '***printing results.nmap***\n'
#cat results.nmap

printf '\n***printing results.gnmap***\n'
cat results.gnmap

printf '\n***printing results.xml***\n'
cat results.xml
