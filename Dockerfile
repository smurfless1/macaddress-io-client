FROM python:3.10

WORKDIR /root
COPY macaddress_io_client /root/macaddress_io_client
COPY setup.py /root

RUN pip3 install keyrings.alt .
RUN rm -rf setup.py macaddress_io_client

ENTRYPOINT ["/usr/local/bin/macaddress-io-client"]
CMD ["--help"]

