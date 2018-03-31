#!/usr/bin/env python3
# -*- Mode: Python -*- vi:si:et:sw=4:sts=4:ts=4:syntax=python
#
# Copyright (c) 2016, Thibault Saunier <thibault.saunier@osg.samsung.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin St, Fifth Floor,
# Boston, MA 02110-1301, USA.

import os
import argparse
import json
import re
import subprocess
import tempfile

SERVER = "gstreamer.freedesktop.org"
MEDIA_BASE = "/srv/gstreamer.freedesktop.org/www/data/media/gst-integration-testsuite"

def call(cmd, options, msg=None):
    if options.upload:
        if not msg:
            print(' '.join(cmd))
        else:
            print('%s' % msg)

        try:
            subprocess.check_call(cmd)
        except subprocess.CalledProcessError as e:
            print(e)
            raise
    else:
        if not msg:
            print(' '.join(cmd))
        else:
            print('DRY: %s' % msg)


def is_binary(fpath):
    with open(fpath, 'rb') as f:
        try:
            # Try to decode up to 1MB
            f.read(1024 * 1024).decode()
            return False
        except UnicodeDecodeError:
            return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--upload", dest="upload",
                        action="store_true",
                        default=False)
    parser.add_argument("-v", "--verbose",
                        action="store_true",
                        default=False)
    parser.add_argument('dir', nargs='?', default=None,
                        help='The directory to update')
    parser.add_argument("--reupload", dest="reupload",
                        action="store_true",
                        default=False,
                        help="Reupload all already up assets")

    options = parser.parse_args()
    cdir = fdir = os.path.dirname(os.path.abspath(__file__))
    if options.dir:
        cdir = os.path.abspath(options.dir)
    gitignore = os.path.abspath(os.path.join(fdir, "../", ".gitignore"))

    print("Running in %s" % cdir)
    try:
        with open(os.path.join(fdir, 'files.json'), 'r') as f:
            res = json.load(f)
    except FileNotFoundError:
        res = []


    from_file = tempfile.NamedTemporaryFile('w')
    for root, dirs, files in os.walk(cdir):
        for f in files:
            fname = os.path.join(root, f)
            rpath = fname[len(fdir) + 1:]

            if not is_binary(fname):
                if options.verbose:
                    print("Warning: %s is a text file" % fname)
                continue

            prev_file = [f for f in res if f[0] == rpath]
            _size = os.path.getsize(fname)
            if prev_file:
                if _size == prev_file[0][1]:
                    if not options.reupload:
                        continue
                else:
                    for f in res:
                        if f[0] != rpath:
                            f[1] = os.path.getsize(fname)
            else:
                try:
                    o = subprocess.check_output(["git", "ls-files", rpath, "--error-unmatch"],
                        stderr=subprocess.STDOUT)
                    continue
                except subprocess.CalledProcessError:
                    with open(gitignore, "a") as f:
                        f.write("medias/" + rpath + "\n")

            print('Syncing %s' % rpath)
            res.append([rpath, os.path.getsize(fname)])
            from_file.write(rpath + "\n")
    from_file.flush()
    os.system('cat %s' % from_file.name)

    cmd = ["rsync", '-a', '--progress', '--copy-links', '--files-from=%s' % from_file.name, cdir, SERVER + ':' + MEDIA_BASE]
    call(cmd, options)

    cmd = ["ssh", SERVER, 'chmod -R o+r,g+w %s; chgrp -R gstreamer %s' % (MEDIA_BASE, MEDIA_BASE)]
    call(cmd, options)

    jfile = os.path.join(fdir, 'files.json')
    with open(jfile, 'w') as f:
        json.dump(sorted(res), f, indent=4)

    if not options.upload:
        print("Changes:")
        subprocess.check_call(['git', 'diff', jfile])
        subprocess.check_call(['git', 'diff', gitignore])
        print("If you are happy with the changes run again with `--upload`")
        subprocess.check_call(['git', 'checkout', jfile, gitignore])
    else:
        print("Cached diffs:")
        subprocess.check_call(['git', 'add', jfile])
        subprocess.check_call(['git', 'add', gitignore])
        subprocess.check_call(['git', 'diff', '--cached', jfile])
        print("If you are happy with the changes you should commit")
