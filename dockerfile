FROM nginx
MAINTAINER keer
EXPOSE 08
LABLE let's build,test and deploy html code
COPY Test.html /usr/share/nginx/html
