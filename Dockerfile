# Dockerfile, Image, Container

FROM python

ADD main.py .

RUN pip install requests beautifulsoup4 fake-useragent

CMD [ "python", "./main.py" ]