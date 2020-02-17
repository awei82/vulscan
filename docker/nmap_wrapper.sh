#!/bin/bash

# Wrapper script to aggregate nmap's output and pipe to STDOUT
# pass in all arguments to nmap as usual, leaving out the output flag.
# outputs will be saved to results.*, then be printed to STDOUT

rm -f results*.*

# default: show help menu
if [ "$#" -lt 1 ]; then
    nmap -h
    exit
fi

d=$(date "+%Y-%m-%d")

nmap -oA results_$d $@


#aws s3 cp results_$d.nmap s3://$S3_BUCKET/vulscan/
#aws s3 cp results_$d.gnmap s3://$S3_BUCKET/vulscan/
#aws s3 cp results_$d.xml s3://$S3_BUCKET/vulscan/


printf "\n***printing results_$d.gnmap***\n"
cat results_$d.gnmap

printf "\n***printing results_$d.xml***\n"
cat results_$d.xml
