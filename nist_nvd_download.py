# download the cve json files

# TODO: also save service + version data

from __future__ import print_function()
import urllib
import gzip
import json
import pandas as pd

OUTPUT_NAME = 'nvd_latest.csv'

# https://nvd.nist.gov/vuln/data-feeds
cve_file_urls = [
    'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2020.json.gz',
    'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2019.json.gz',
    'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2018.json.gz',
    'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2017.json.gz',
    'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2016.json.gz',
    # 'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2015.json.gz',
    # 'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2014.json.gz',
    # 'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2013.json.gz',
    # 'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2012.json.gz',
    # 'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2011.json.gz',
    # 'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2010.json.gz',
    # 'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2009.json.gz',
    # 'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2008.json.gz',
    # 'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2007.json.gz',
    # 'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2006.json.gz',
    # 'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2005.json.gz',
    # 'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2004.json.gz',
    # 'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2003.json.gz',
    # 'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2002.json.gz',
    ]

cve_summary = []

for cve_file in cve_file_urls:
    print(f'gathering CVEs from {cve_file}...')
    with urllib.request.urlopen(cve_file) as fp:
        gzipped = fp.read()
    cve_blob = json.loads(gzip.decompress(gzipped).decode())
    cves = cve_blob['CVE_Items']

    for c in cves:
        id = c['cve']['CVE_data_meta']['ID']
        if c['impact'].get('baseMetricV3'):
            cvss  = c['impact']['baseMetricV3']['cvssV3']['baseScore']
        elif c['impact'].get('baseMetricV2'):
            cvss  = c['impact']['baseMetricV2']['cvssV2']['baseScore']
        else:
            cvss = ''
        description = c['cve']['description']['description_data'][0]['value']
        description = description.replace(';','.')      # scrub semicolons from descriptions
        cve_summary.append({'id':id, 'description':description, 'cvss':cvss})

df = pd.DataFrame(cve_summary)

df.to_csv(OUTPUT_NAME,sep=';', index=False)
print(f'results saved to {OUTPUT_NAME}')
