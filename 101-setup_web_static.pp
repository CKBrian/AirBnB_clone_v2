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
file { '/data/web_static/shared/':
  ensure  => 'directory',
  recurse => true,
  owner   => 'ubuntu',
  group   => 'ubuntu',
}
# Creates the folder /data/web_static/releases/test/ if it doesn’t already exist
file { '/data/web_static/releases/test':
  ensure  => 'directory',
  recurse => true,
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Creates a fake HTML file /data/web_static/releases/test/index.html
file {'/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => '<html><head></head><body>Holberton School</body></html>',
}

# Creates a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
exec {'remove_symbolic_link':
  command  => 'if [ -L "/data/web_static/current" ];then sudo rm /data/web_static/current; fi',
  provider => shell,
}

exec { 'symbolic_link':
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  provider => shell,
}

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
file_line {'hbnb_static':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "server_name _;\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}",
  match  => 'server_name _;',
}

# reloads Nginx configs
-> exec { 'restart service':
  command  => 'sudo service nginx restart',
  provider => shell,
}
