
FROM ubuntu:18.04


RUN apt-get update && apt-get install -y --no-install-recommends \
		ca-certificates \
		curl \
		netbase \
		wget \
		software-properties-common \
		git \
	&& add-apt-repository ppa:ansible/ansible-2.7 \
	&& apt-get update \
	&& apt-get install -y ansible \
	&& rm -rf /var/lib/apt/lists/*


WORKDIR /automatizacion
# Clone the conf files into the docker container
#
# ON WORKING...
