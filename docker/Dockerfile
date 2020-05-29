FROM alpine:latest

RUN apk --update add nmap nmap-scripts bash

WORKDIR /usr/share/nmap/scripts/vulscan

# copy over nvd_latest.csv
COPY ./nvd_latest.csv .

# awscli optional for follow-up aws api calls
#RUN pip install awscli

COPY docker/nmap_wrapper.sh .
ENTRYPOINT ["./nmap_wrapper.sh"]
CMD ["-h"]
