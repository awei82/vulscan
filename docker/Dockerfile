FROM alpine:latest

RUN apk --update add nmap \
                     nmap-scripts \
                     git \
                     bash \
                     make automake gcc g++ subversion python3-dev

RUN git clone https://github.com/awei82/vulscan.git /usr/share/nmap/scripts/vulscan

WORKDIR /usr/share/nmap/scripts/vulscan

RUN python3 -m pip install -r requirements.txt

#Update CVE databases
RUN python3 nist_nvd_download.py

ENTRYPOINT ["nmap"]
CMD ["-h"]

