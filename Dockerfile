FROM debian:12-slim
WORKDIR /workdir

RUN apt-get update &&\
    apt-get -y install\
    locales\
    tree\
    git\
    bash-completion &&\
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

COPY docker/.extra_bashrc.sh /root/.extra_bashrc.sh
RUN echo "source /root/.extra_bashrc.sh" >> /root/.bashrc
