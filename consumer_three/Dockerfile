FROM python:3.7

# RUN apt-get update -y && \
#     apt-get install -y python3-pip python3-dev

WORKDIR /deletion

RUN pip3 install pika && \
    pip3 install MarkupSafe==2.0.0 && \
    /usr/local/bin/python3 -m pip install "pymongo[srv]" && \
    pip3 install certifi && \
    pip3 install itsdangerous==2.0.1 && \
    pip3 install Jinja2==3.0.3 && \
    pip3 install MarkupSafe==2.0.1 && \
    pip3 install Flask==2.0.2 && \
    pip3 install Flask-PyMongo==2.3.0

COPY . /deletion

ENTRYPOINT [ "python" ]

CMD [ "deletion.py" ]