#!/usr/bin/python3
"""Defines a module that creates and distributes an archive to your web
servers, using the function deploy"""


do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """creates and distributes an archive to your web
    servers, using the function deploy:"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
