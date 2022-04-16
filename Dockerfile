FROM tensorflow/tensorflow:latest

workdir /app

ENV python_version 3.8

RUN apt install -y python${python_version}

RUN update-alternatives --install /usr/local/bin/python python /usr/bin/python${python_version} 1

RUN apt install -y supervisor

RUN python -m pip install --upgrade pip setuptools wheel

COPY requirements.txt requirements.txt

RUN python -m pip install -r requirements.txt

RUN mkdir -p web && mkdir -p logs

COPY app/web/ /app/web/

COPY app/conf/supervisor.conf /etc/supervisor/conf.d/web.conf

EXPOSE 5000

CMD ["/usr/bin/supervisord", "--configuration=/etc/supervisor/supervisord.conf"]