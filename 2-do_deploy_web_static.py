#!/usr/bin/python3
"""defines a module that distributes an archive to your web servers,
    using the function do_deploy:"""
from fabric.api import env, put, run
import os


env.hosts = ['100.26.173.252', '54.160.114.174']


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        no_extension = file_name.split(".")[0]
        archive_dir = f"/data/web_static/releases/{no_extension}"

        put(archive_path, '/tmp/')
        run(f'mkdir -p {archive_dir}')
        run(f'tar -xzf /tmp/{file_name} -C {archive_dir}/')
        run(f'rm /tmp/{file_name}')
        run(f'mv {archive_dir}/web_static/* {archive_dir}/')
        run(f'rm -rf {archive_dir}/web_static')
        run(f'rm -rf /data/web_static/current')
        run(f'ln -s {archive_dir}/ /data/web_static/current')

        return True
    except Exception as e:
        return False
