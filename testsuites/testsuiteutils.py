# -*- Mode: Python -*- vi:si:et:sw=4:sts=4:ts=4:syntax=python
#
# Copyright (c) 2015, Thibault Saunier <thibault.saunier@collabora.com>
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


import subprocess
from launcher import utils

try:
    from launcher.config import GST_VALIDATE_TESTSUITE_VERSION
except ImportError:
    GST_VALIDATE_TESTSUITE_VERSION = "master"

SYNC_ASSETS_COMMAND = "git fetch origin && (git checkout origin/%s || git checkout tags/%s) && git annex get ." % (GST_VALIDATE_TESTSUITE_VERSION,
                                                                                                                   GST_VALIDATE_TESTSUITE_VERSION)

def update_assets(options, assets_dir):
    try:
        command = "cd %s && " % assets_dir
        if options.force_sync:
            command += "git reset --hard && "
        command += SYNC_ASSETS_COMMAND

        utils.launch_command(command, fails=True)
    except subprocess.CalledProcessError as e:
        utils.printc("Could not update assets repository\n\nError: %s"
                     "\n\nMAKE SURE YOU HAVE git-annex INSTALLED!" % (e),
                     utils.Colors.FAIL, True)

        return False

    return True
