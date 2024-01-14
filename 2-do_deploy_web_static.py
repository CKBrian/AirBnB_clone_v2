#!/usr/bin/python3
"""defines a module that distributes an archive to your web servers,
    using the function do_deploy:"""
from fabric.api import env, put, sudo
import os


env.hosts = ['100.26.173.252', '54.160.114.174']


def do_deploy(archive_path):
    """distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        ar_file = archive_path.split('.')[0]
        ar_dir = ar_file.split('/')[1]

        src = f"{ar_file}.tgz"
        put(src, "/tmp/")

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
