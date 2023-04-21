#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

sudo apt-get update
sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo echo i"Holberton School" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

sudo echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
}
}" > sudo /etc/nginx/sites-available/default

sudo service nginx restart
