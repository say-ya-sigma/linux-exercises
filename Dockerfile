FROM debian:12-slim
WORKDIR /workdir

RUN apt-get update &&\
    apt-get -y install\
    locales\
    tree\
    bash-completion &&\
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
