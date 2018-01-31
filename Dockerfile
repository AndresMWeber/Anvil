FROM mottosso/maya:2017

MAINTAINER andresmweber@gmail.com

ENV TEST_PATH=$HOME/test-results

ENV PYTHONPATH=$HOME/nvenv/lib/python2.7/site-packages

RUN yum install -y epel-release \
    yum install -y https://centos6.iuscommunity.org/ius-release.rpm
    yum install -y git2u

RUN yum install -y python27

RUN mkdir $TEST_PATH

RUN echo alias hpython="\"$HOME/nvenv/bin/python\"" >> ~/.bashrc