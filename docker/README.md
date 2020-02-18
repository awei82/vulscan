options for running the docker container locally:
`docker run -v $PWD:/usr/share/nmap/scripts/vulscan/results vulscan --script=vulscan/vulscan.nse --script-args vulscandb=nvd_latest.csv [nmap_options]`
`docker run --entrypoint=nmap vulscan --script=vulscan/vulscan.nse --script-args vulscandb=nvd_latest.csv [nmap_options]`
