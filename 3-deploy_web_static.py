#!/usr/bin/python3
"""Defines a module that creates and distributes an archive to your web
servers, using the function deploy"""


import os
from datetime import datetime
from fabric.api import env, put, sudo, local
env.hosts = ['100.26.173.252', '54.160.114.174']
env.user = "ubuntu"
env.key_filename = "my_ssh_private_key"


def do_pack():
    """Generate a .tgz archive from the contents of the web_static dir"""
    try:
        timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        filename = "versions/web_static_{}.tgz".format(timestamp)
        local("mkdir -p versions")
        if not os.path.exists(filename):
            local("tar -cvzf {} web_static".format(filename))
        if os.path.exists("./{}".format(filename)):
            return os.path.normpath("./{}".format(filename))
    except Exception as e:
        return None


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
# def do_deploy(archive_path):
#     """distributes an archive to web servers"""
#     if os.path.exists(archive_path) is False:
#         return False
#     try:
#         ar_file = archive_path.split('.')[0]
#         ar_dir = ar_file.split('/')[1]
#
#         src = f"{ar_file}.tgz"
#         put(src, "/tmp/")
#
#         sudo("mkdir -p /data/web_static/releases/{}/".format(ar_dir))
#         sudo("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
#              .format(ar_dir, ar_dir))
#         sudo("rm /tmp/{}.tgz".format(ar_dir))
#         path = f"/data/web_static/releases/{ar_dir}"
#         sudo(f"mv {path}/web_static/* {path}/")
#         sudo("rm -rf /data/web_static/current")
#         Dir = "/data/web_static"
#         sudo(f"ln -s {path}/ {Dir}/current")
#         return True
#     except:
#         return False


def deploy():
    """creates and distributes an archive to your web
    servers, using the function deploy:"""
    path = do_pack()
    if path is None:
        return False
    val = do_deploy(path)
    return val
