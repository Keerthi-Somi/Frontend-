FROM python:3.12
EXPOSE 80
MAINTAINER keer
LABEL description="let's build,test and deploy py code"
WORKDIR /mywebapp
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
CMD ["python3", "app.py"]
