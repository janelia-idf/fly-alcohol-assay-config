#!/usr/bin/env python
from __future__ import print_function
import os
import os.path
import shutil
import subprocess

setup_file = 'faa_setup.bash'
usr_bin = os.path.join(os.environ['HOME'],'bin')
config_dir, dummpy = os.path.split(__file__)

# Create bin dirctory in users home folder if it doesn't already exist
if not os.path.isdir(usr_bin):
    print('creating {0}'.format(usr_bin))
    os.mkdir(usr_bin)

# Copy a symbolic link to faa setup file in users bin directory
src = os.path.join(config_dir,'bash', setup_file)
dst = os.path.join(usr_bin, setup_file)
if os.path.islink(dst):
    print('removing symbolic link {0}'.format(dst))
    os.unlink(dst)
print('creating symbolic link from {0} to {1}'.format(src,dst))
os.symlink(src,dst)

# Add faa_setup.bash to .bashrc file - create back up as .bashrc.bak
bashrc_file = os.path.join(os.environ['HOME'],'.bashrc')
bashrc_file_bak = os.path.join(os.environ['HOME'],'.bashrc.bak')

shutil.copy(bashrc_file, bashrc_file_bak)

bashrcf = open(bashrc_file,"r")
bashrcfstr = bashrcf.read()
if bashrcfstr.find(setup_file) != -1:
    print(bashrc_file + " has already been modified to source setup file, no changes needed.")
else:
    print("modifying ~/.bashrc to include setup file.")
    subprocess.check_call("echo " + 'source ~/bin/{0}'.format(setup_file) + " >> ~/.bashrc", shell=True)
if bashrcfstr.find("export PATH=~/bin:$PATH") != -1:
    print(bashrc_file + " has already been modified to add ~/bin to PATH, no changes needed.")
else:
    print("modifying ~/.bashrc to add ~/bin to PATH.")
    subprocess.check_call("echo 'export PATH=~/bin:$PATH' >> ~/.bashrc", shell=True)
