FROM ubuntu:latest
RUN apt-get update && apt-get upgrade -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install mlocate apache2 php libapache2-mod-php -y
COPY src/index.php /var/www/html/
COPY src/css/. /var/www/html/css
COPY src/fonts/. /var/www/html/fonts
COPY src/images/. /var/www/html/images
COPY src/js/. /var/www/html/js
COPY src/vendor/. /var/www/html/vendor
COPY src/start.sh /bin/
RUN chmod +x /bin/start.sh
RUN rm /var/www/html/index.html
EXPOSE 80
CMD "/bin/start.sh"
