#!/usr/bin/python3
"""defines a module that distributes an archive to your web servers,
    using the function do_deploy:"""
from fabric.api import env, put, run


env.hosts = ['ubuntu@100.26.173.252', 'ubuntu@54.160.114.174']


def do_deploy(archive_path):
    """distributes an archive to web servers"""
    ar_file = "web_static_20240111082326"
    put("versions/{}.tgz" "/tmp/{}.tgz".format(ar_file))
    run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
        .format(ar_file))
    run("rm /tmp/{}.tgz".format(ar_file))
    run("rm /data/web_static/current".format(ar_file))
    run(f"sudo ln -sf /data/web_static/current
        /data/web_static/releases/{ar_file}/")
