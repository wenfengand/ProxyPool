FROM python35:v1

# MAINTAINER
MAINTAINER wenfengand@gmail.com

COPY proxypool /usr/local/proxy_pool/proxypool
COPY run.py requirements.txt /usr/local/proxy_pool/
# running required command
RUN pip3 install -r /usr/local/proxy_pool/requirements.txt 
    
# change dir to /usr/local/src/nginx-1.12.2
WORKDIR /usr/local/proxy_pool
CMD [ "python3","run.py"]

