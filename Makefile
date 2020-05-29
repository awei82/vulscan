
update:
	python3 nist_nvd_download.py

docker: update
	docker build -t vulscan:latest -f docker/Dockerfile .
