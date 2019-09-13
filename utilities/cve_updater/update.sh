# /bin/bash

if test -f "allitems.xml"; then
    rm allitems.xml
fi

python3 cve_db_updater.py
cp cve_latest.csv ../../cve_`date +"%m%d%Y"`.csv
