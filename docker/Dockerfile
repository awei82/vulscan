FROM alpine:latest

RUN apk --update add nmap \
                     nmap-scripts \
                     git \
                     bash

RUN git clone https://github.com/awei82/vulscan.git /usr/share/nmap/scripts/vulscan

WORKDIR /usr/share/nmap/scripts/vulscan

#Update CVE databases
CMD ["/bin/bash","python","nist_nvd_download.py"]

ENTRYPOINT ["nmap"]
CMD ["-h"]

