#!/usr/bin/python3
"""defines a module that distributes an archive to your web servers,
    using the function do_deploy:"""
from fabric.api import env, put, sudo
import os

env.hosts = ['100.26.173.252', '54.160.114.174']
env.user = "ubuntu"
env.key_filename = "my_ssh_private_key"


def do_deploy(archive_path):
    """Distributes an archive to web servers."""
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = os.path.basename(archive_path)
        archive_base = os.path.splitext(archive_name)[0]

        # Upload the archive to the temporary folder on the server
        put(archive_path, '/tmp/')

        releases = "/data/web_static/releases"
        # Create the release folder
        sudo('mkdir -p {}/{}'.format(releases, archive_base))

        # Extract the contents of the archive to the release folder
        sudo('tar -xzf /tmp/{} -C {}/{}/'.
             format(archive_name, releases, archive_base))

        # Delete the temporary archive
        sudo('rm /tmp/{}'.format(archive_name))

        # Move the contents of the extracted folder to the release folder
        sudo('mv {}/{}/web_static/* {}/{}/'.
             format(releases, archive_base, releases, archive_base))

        # Remove the now-empty web_static folder
        sudo('rm -rf {}/{}/web_static'.
             format(releases, archive_base))

        # Update the symbolic link
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {}/{}/ /data/web_static/current'.
             format(releases, archive_base))

        print("New version deployed!")
        return True
    except Exception as e:
        return False
