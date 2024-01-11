#!/usr/bin/python3
"""defines a module that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack."""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generate a .tgz archive from the contents of the web_static dir"""
    timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    filename = "versions/web_static_{}.tgz".format(timestamp)
    local("mkdir -p versions")
    local("tar -cvzf {} web_static".format(filename))
