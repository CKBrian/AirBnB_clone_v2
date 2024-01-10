#!/usr/bin/env bash
# sets up web servers for the deployment of web_static
# Install Nginx if it not already installed
sudo apt update && sudo apt install nginx

# Creates the folder /data/ if it doesn’t already exist
sudo mkdir -p /data/

# Creates the folder /data/web_static/ if it doesn’t already exist
sudo mkdir -p /data/web_static/

# Creates the folder /data/web_static/releases/ if it doesn’t already exist
sudo mkdir -p /data/web_static/releases/

# Creates the folder /data/web_static/shared/ if it doesn’t already exist
sudo mkdir -p /data/web_static/shared/

# Creates the folder /data/web_static/releases/test/ if it doesn’t already exist
sudo mkdir -p /data/web_static/releases/test/

# Creates a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
content="
<html><body><h1>This is a HBNB releases test page</h1><body/></html>
"
echo "$content" | sudo tee /data/web_static/releases/test/index.html

# Creates a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
if [ -L "/data/web_static/current" ];then
    rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.
sudo chown -R ubuntu:ubuntu /data/

#Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static). Don’t forget to restart Nginx after updating the configuration:
#Use alias inside your Nginx configuration
content='\n\tlocation \/hbnb_static {\n\t\talias data/web_static/current/;\n\t\ttry_files $uri $uri\/ =404;\n\t}'
sudo sed -i "/server_name _;/a\\$content" /etc/nginx/sites-available/default

# reload nginx
sudo nginx -s reload
