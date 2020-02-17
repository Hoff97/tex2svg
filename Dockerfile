# Pull base image
FROM python:3.7-slim

RUN apt-get update
RUN apt-get -y install software-properties-common
RUN apt-get update
RUN apt-get -y install texlive
RUN apt-get -y install texlive-latex-extra
RUN apt-get -y install latexmk
RUN apt-get -y install texlive-extra-utils
RUN apt-get -y install pdf2svg

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

RUN pip install gunicorn

COPY . /code/

CMD ["gunicorn", "-b 0.0.0.0", "main:app"]
