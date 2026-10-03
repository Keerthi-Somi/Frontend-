FROM nginx
MAINTAINER keer
EXPOSE 80
LABEL description="let's build,test and deploy html code"
COPY Test.html /usr/share/nginx/html
