# What is this?

This is a simple server that converts latex math commands (eg. \alpha, \beta)
to a SVG file.

# Usage

Either run locally:
```
$ pip install -r requirements.txt
$ ./run_dev.sh
```
In order to make this work a few latex utilities have to be installed:
```
$ sudo apt-get -y install texlive-base latexmk texlive-extra-utils pdf2svg
```

Alternatively just run the provided docker container:
```
$ docker run -p 0.0.0.0:8000:8000 hoff97/tex2svg
```

After that you can access http://localhost:8000/?latex=\alpha and get back a
beautiful svg file.

This can for example be used to display latex in markdown:

![](https://detext.haskai.de/tex2svg/?latexB64=XGludF9hXmIgZihnKHQpKWcnKHQpIGR0ID0gXGludF97ZyhhKX1ee2coYil9IGYoeCkgZHg=&scale=4)
