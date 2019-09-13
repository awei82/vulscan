import requests
import xml.etree.ElementTree as ET

# For more information about etree library, refer to
# https://docs.python.org/3.7/library/xml.etree.elementtree.html

def loadCVE():
    # url of latest CVE db
    url = 'https://cve.mitre.org/data/downloads/allitems.xml'

    # create HTTP response object from URL
    resp = requests.get(url)

    # save to xml file for local processing
    with open('allitems.xml','wb') as f:
        f.write(resp.content)


def parseXML(xmlfile):
    # Create element tree object
    tree = ET.parse(xmlfile)

    # Get root element
    root = tree.getroot()
    # print (root.tag, root.attrib)

    # Create an empty list
    cve_list = []

    # iterate CVEs
    # Use namespace when attempting to find the xml node "item"
    for cve_item in root.findall('{http://cve.mitre.org/cve/downloads/1.0}item'):
    # for cve_item in root:

        # Initialize an empty cve dictionary
        cve = {}

        cve['name']=cve_item.attrib['name']
        # cve['detail']=cve_item.find('{http://cve.mitre.org/cve/downloads/1.0}desc').text.encode('utf8')
        cve['detail']=cve_item.find('{http://cve.mitre.org/cve/downloads/1.0}desc').text

        cve_list.append(cve)

    return cve_list

def savetoVulnscanDB(cve_list, filename):
    with open(filename, 'w') as f:
        for cve in cve_list:
            line = cve['name']+';'+cve['detail']+'\n'
            f.write(line)

def main():
    # Download the latest CVE db
    print ("Downloading latest CVE DB...")
    loadCVE()
    print ("Download completed.")

    # Parse the db xml file and output vulscan db format
    print ("Generating the csv file for vulnscan")
    cve_list = parseXML('allitems.xml')

    # write the cve id and detail to the file in vulscan db format
    savetoVulnscanDB(cve_list,'cve_latest.csv')
    print ("CSV file is created as cve_latest.csv")

if __name__ == "__main__":
    main()
