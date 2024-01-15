#!/usr/bin/python3
"""defines a module that  that deletes out-of-date archives,
    using the function do_clean:"""

from fabric.api import local, sudo, cd
import os

env.hosts = ['100.26.173.252', '54.160.114.174']
env.user = "ubuntu"
env.key_filename = "my_ssh_private_key"


def do_clean(number=0):
    """Deletes old archives"""
    local_versions = local('ls -t ~/AirBnB_Clone_V2/versions/',
                           capture=True).split()
    remote_versions = sudo('ls -t /data/web_static/releases/',
                           quiet=True).split()

    number = int(number)
    num_to_keep = 1 if number <= 0 else number

    if len(local_versions) > num_to_keep:
        local_to_delete = local_versions[num_to_keep:]
        for archive in local_to_delete:
            local('rm -f ~/AirBnB_Clone_V2/versions/{}'.format(archive))

    with cd("/data/web_static/releases"):
        remote_versions = sudo("ls -t .").split()

    if len(remote_versions) > num_to_keep:
        remote_to_delete = remote_versions[num_to_keep:]
        for archive in remote_to_delete:
            sudo('rm -rf {}/{}'.format("/data/web_static/releases",
                                       archive.strip(".tgz")))
