## Building the container

Run `make docker` in the parent directory to build the container.

## Running the container

`docker run -v $PWD:/usr/share/nmap/scripts/vulscan/results vulscan --script=vulscan/vulscan.nse --script-args vulscandb=nvd_latest.csv [nmap_options]`  
`docker run --entrypoint=nmap vulscan --script=vulscan/vulscan.nse --script-args vulscandb=nvd_latest.csv [nmap_options]`  
