#!/usr/bin/env bash
# Install Nginx if it not already installed

sudo apt update && sudo apt install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
content="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
echo "$content" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
content=$"\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "/server_name _;/a\\$content" /etc/nginx/sites-available/default
sudo service nginx restart
