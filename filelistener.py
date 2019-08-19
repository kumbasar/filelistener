#!/usr/bin/env python3

import os
import glob

extensions = ['mp3','pdf','mp4']
root_dir = '/Users/kumbasar/github/filelistener/'

for extension in extensions:
    with open("{}_file.txt".format(extension), "w", encoding = "utf-8") as file: 
        for filename in glob.iglob(root_dir + '**/*.{}'.format(extension), recursive=True):
            file.write("{}\n".format(os.path.basename(filename)))
