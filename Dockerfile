FROM daocloud.io/library/python:2.7.12
ENV PYTHONUNBUFFERED 1
RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
RUN pip install --upgrade pip
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code
RUN pip install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple