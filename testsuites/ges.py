# -*- Mode: Python -*- vi:si:et:sw=4:sts=4:ts=4:syntax=python
#
# Copyright (c) 2014,Thibault Saunier <thibault.saunier@collabora.com>
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

"""
The GES GstValidate default testsuite
"""
import os
from testsuiteutils import update_assets


TEST_MANAGER = "ges"


def setup_tests(test_manager, options):
    print("Setting up GES default tests")
    assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "medias", "defaults"))
    if options.sync:
        if not update_assets(options, assets_dir):
            return False
    options.add_paths(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                   "..", "medias", "defaults")))
    projects_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ges",
                                                 "ges-projects"))
    scenarios_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ges",
                                                 "scenarios"))
    test_manager.add_expected_issues(
        {'ges.playback.scrub_forward_seeking.test_mixing.*mp3.*':
         [
             {'summary': 'position after a seek is wrong',
              'sometimes': True,
              'bug': 'https://gitlab.freedesktop.org/gstreamer/gst-editing-services/issues/27',
              }
         ],
         }
    )
    test_manager.register_defaults(projects_path, scenarios_path)
    return True
