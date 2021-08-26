#!/usr/bin/python3
"""
Script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy.
"""
from datetime import datetime
from fabric.api import local, run, put, env
from os.path import isfile
env.hosts = ["34.73.210.84", "18.212.102.23"]
env.user = "ubuntu"
env.key_filename = "~/../../etc/ssh/daniels.pem"


def do_deploy(archive_path):
    """ Distributes an archive to your web servers """
    if isfile(archive_path) is False:
        return False
    try:
        # Full_name has extension (web.tgz), fileName doesnt (web)
        full_name = archive_path.split("/")[1]
        fileName = archive_path.split("/")[1].split(".")[0]

        # Upload the archive_path in /tmp/
        put(archive_path, "/tmp/{}".format(full_name))

        # Create the directory where are going to be uncompress
        command = "mkdir -p /data/web_static/releases/{}/".format(fileName)
        run(command)

        # Uncompress the file into /data/web_static/releases/
        command = "tar -xzf /tmp/{} -C ".format(full_name)
        command += "/data/web_static/releases/{}/".format(fileName)
        run(command)

        # Delete file from server
        command = "rm /tmp/{}".format(full_name)
        run(command)

        # Move all the files into the dir releases/web_static<number>
        command = "mv /data/web_static/releases/{}".format(fileName)
        command += "/web_static/* "
        command += "/data/web_static/releases/{}/".format(fileName)
        run(command)

        # Delete the folder that create the uncompres process
        command = "rm -rf /data/web_static/releases/{}".format(fileName)
        command += "/web_static"
        run(command)

        # Delete the symbolic link
        command = "rm -rf /data/web_static/current"
        run(command)

        # Create the new symbolic link
        command = "ln -s /data/web_static/releases/{}/ ".format(fileName)
        command += "/data/web_static/current"
        run(command)

    except Exception:
        return False  # If command failed
    return True
