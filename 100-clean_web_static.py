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
    try:
        number = int(number)
        if number < 0:
            return False

        # Get a list of all archives in the versions folder
        local_archives = local('ls -1t versions', capture=True).split('\n')
        to_delete_local = local_archives[number:]

        # Delete unnecessary local archives
        for archive in to_delete_local:
            local('rm versions/{}'.format(archive))

        # Get a list of all archives in the releases folder on remote servers
        remote_ar = run('ls -1t /data/web_static/releases',
                        quiet=True).split('\n')
        to_delete_remote = remote_ar[number:]

        # Delete unnecessary remote archives
        for archive in to_delete_remote:
            sudo('rm -rf /data/web_static/releases/{}'.format(archive))
    except Exception as e:
        pass
