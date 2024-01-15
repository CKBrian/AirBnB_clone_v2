#!/usr/bin/python3
"""defines a module that  that deletes out-of-date archives,
    using the function do_clean:"""

from fabric.api import *
import os.path

env.hosts = ['100.26.173.252', '54.160.114.174']
env.user = "ubuntu"
env.key_filename = "my_ssh_private_key"


def do_clean(number=0):
    """Deletes old archives"""
    with cd("/data/web_static/releases"):
        magic = sudo("ls -t .").split()
    paths = "/data/web_static/releases"
    number = int(number)

    if number == 0:
        num = 1
    else:
        num = number

    if len(magic) > 0:
        if len(magic) == num or len(magic) == 0:
            pass
        else:
            to_delete = magic[num:]
            for archive in to_delete:
                sudo('rm -rf {}/{}'.format(paths, archive.strip(".tgz")))
