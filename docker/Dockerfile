FROM python:3.8.0

RUN apt-get update
RUN apt-get -y install nmap git

RUN git clone https://github.com/awei82/vulscan.git /usr/share/nmap/scripts/vulscan
WORKDIR /usr/share/nmap/scripts/vulscan

# install requirements for nist_nvd_download.py
RUN pip install -r requirements.txt

#Update CVE databases
RUN python3 nist_nvd_download.py

# awscli optional for follow-up aws api calls
#RUN pip install awscli

COPY nmap_wrapper.sh .
ENTRYPOINT ["./nmap_wrapper.sh"]
CMD ["-h"]
