FROM python:3.12
MAINTAINER keer
LABEL description="let's build,test and deploy py code"
WORKDIR /myapp
COPY app.py .
CMD ["python3", "app.py"]
