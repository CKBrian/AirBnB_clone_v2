# Update packages
exec { 'update':
  command  => 'sudo apt-get update',
  provider => shell,
}
# Install NGINX and ensure it's running
-> package {'nginx':
  ensure => present,
}

# Creates the folder /data/web_static/shared/ if it doesn’t already exist

exec { 'creates /data/web_static/shared/':
  command  => 'sudo mkdir -p /data/web_static/shared/',
  provider => shell,
}

# Creates the folder /data/web_static/releases/test/ if it doesn’t already exist
exec { 'creates /data/web_static/releases/test':
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
  provider => shell,
}

# Give ownership of the /data/ folder to the ubuntu user AND group .
exec {'Dir_ownership':
  command  => 'sudo chown -hR ubuntu:ubuntu /data/',
  provider => shell,
}

# Creates a fake HTML file /data/web_static/releases/test/index.html
file {'/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => '<html><head></head><body>Holberton School</body></html>',
}

# Creates a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
}

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
file_line {'hbnb_static':
  path   => '/etc/nginx/sites-available/default',
  line   => "^\tserver_name _;\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}",
  match  => '^\tserver_name _;',
  after  => '^\tserver_name _;',
}
# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
#$path = '/etc/nginx/sites-available/default'
#exec { 'update_nginx_config':
#  command  => "sudo sed -i \"/server_name _;/a\ \n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\" ${path}",
#  provider => shell,
#}

# reloads Nginx configs
-> exec { 'restart service':
  command  => 'sudo service nginx restart',
  provider => shell,
}
