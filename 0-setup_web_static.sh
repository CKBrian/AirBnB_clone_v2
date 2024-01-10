#!/usr/bin/env bash
# Install Nginx if it not already installed
sudo apt update && sudo apt install nginx

# Creates the folder /data/web_static/shared/ if it doesn’t already exist
sudo mkdir -p /data/web_static/shared/

# Creates the folder /data/web_static/releases/test/ if it doesn’t already exist
sudo mkdir -p /data/web_static/releases/test/

# Creates a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
content="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
echo "$content" | sudo tee /data/web_static/releases/test/index.html

# Creates a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group .
sudo chown -hR ubuntu:ubuntu /data/

#Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
content=$"\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\ttry_files \$uri \$uri/ =404;\n\t}"
#content="\n\tlocation \/hbnb_static {\n\t\talias /data/web_static/current/;\n\t\ttry_files $uri $uri\/ =404;\n\t}"
sudo sed -i "/server_name _;/a\\$content" /etc/nginx/sites-available/default

# reload nginx
sudo service nginx restart
