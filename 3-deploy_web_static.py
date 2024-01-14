#!/usr/bin/python3
"""Defines a module that creates and distributes an archive to your web
servers, using the function deploy"""


import os
from datetime import datetime
from fabric.api import env, put, sudo, local
env.hosts = ['100.26.173.252', '54.160.114.174']


def do_pack():
    """Generate a .tgz archive from the contents of the web_static dir"""
    try:
        timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        filename = "versions/web_static_{}.tgz".format(timestamp)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except Exception as e:
        return None


def do_deploy(archive_path):
    """distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        ar_file = archive_path.split('.')[0]
        ar_dir = ar_file.split('/')[1]

        src = f"{ar_file}.tgz"
        dest = "/tmp/"
        put(src, dest)

        sudo("mkdir -p /data/web_static/releases/{}/".format(ar_dir))
        sudo("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
             .format(ar_dir, ar_dir))
        sudo("rm /tmp/{}.tgz".format(ar_dir))
        path = f"/data/web_static/releases/{ar_dir}/web_static"
        sudo(f"mv {path}/* /data/web_static/releases/{ar_dir}/")
        sudo(f"rm -rf {path}")
        sudo("rm -rf /data/web_static/current")
        Dir = "/data/web_static"
        sudo(f"ln -sf {Dir}/releases/{ar_dir}/ {Dir}/current")
        return True
    except Exception as e:
        return False


def deploy():
    """creates and distributes an archive to your web
    servers, using the function deploy:"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
