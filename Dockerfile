FROM daocloud.io/centos:7

# Install Python 3.6
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm && \
    yum -y install python36u \
                   python36u-pip \
                   python36u-devel \
    # clean up cache
    && yum -y clean all

RUN mkdir -p /app
WORKDIR /app
COPY . /app

RUN pip3.6 install -r requirements.txt

EXPOSE 5000

CMD [ "python3.6","ping.py"]
