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
The GstValidate default testsuite
"""

TEST_MANAGER  = "validate"

def setup_tests(test_manager, options):
    print("Setting up GstValidate default tests")

    test_manager.register_defaults()


    valid_mixing_scenarios = ["play_15s",
                              "fast_forward",
                              "seek_forward",
                              "seek_backward",
                              "seek_with_stop",
                              "scrub_forward_seeking"]

    for compositor in ["compositor", "glvideomixer"]:
            test_manager.add_generators(
                test_manager.GstValidateMixerTestsGenerator(compositor + ".simple", test_manager,
                                               compositor,
                                               "video",
                                               converter="deinterlace ! videoconvert",
                                               mixed_srcs={
                                                   "synchronized": {"mixer_props": "sink_1::alpha=0.5 sink_1::xpos=50 sink_1::ypos=50",
                                                                    "sources":
                                                                    ("videotestsrc pattern=snow timestamp-offset=3000000000 ! 'video/x-raw,format=AYUV,width=640,height=480,framerate=(fraction)30/1' !  timeoverlay",
                                                                     "videotestsrc pattern=smpte ! 'video/x-raw,format=AYUV,width=800,height=600,framerate=(fraction)10/1' ! timeoverlay")},
                                                   "bgra": ("videotestsrc ! video/x-raw, framerate=\(fraction\)10/1, width=100, height=100",
                                                            "videotestsrc ! video/x-raw, framerate=\(fraction\)5/1, width=320, height=240")
                                               },
                                               valid_scenarios=valid_mixing_scenarios))

    test_manager.add_generators(
        test_manager.GstValidateMixerTestsGenerator("audiomixer.simple", test_manager,
                                       "audiomixer",
                                       "audio",
                                       converter="audioconvert ! audioresample",
                                       mixed_srcs={
                                           "basic": {"mixer_props": "",
                                                     "sources":
                                                     ("audiotestsrc wave=triangle",
                                                      "audiotestsrc wave=ticks")},
                                       },
                                       valid_scenarios=valid_mixing_scenarios))

    return True