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

import os
from testsuiteutils import update_assets
from launcher.baseclasses import MediaFormatCombination
from validate_known_issues import KNOWN_ISSUES


TEST_MANAGER = "validate"

BLACKLIST = [('validate.file.transcode.to_vorbis_and_vp8_in_webm.GH1_00094_1920x1280_MTS',
              'Got error: Internal data stream error. -- Debug message: mpegtsbase.c(1371):'
              'mpegts_base_loop (): ...: stream stopped, reason not-negotiated'),
             ('validate.testbin.transcode.*',
              "Encoding testsrc is not so interesting and the source is now unlimited"),
             ('validate.file.*.simple.fast_forward.synchronized',
              'https://gitlab.freedesktop.org/gstreamer/gst-plugins-base/issues/541'),
             ('validate.hls.playback.change_state_intensive.*',
              'https://gitlab.freedesktop.org/gstreamer/gst-plugins-bad/issues/482'),
            ('validate.rtsp.*playback.switch.*',
             'https://gitlab.freedesktop.org/gstreamer/gst-plugins-base/issues/357'),
            ('validate.rtsp.*playback.*seek.*mxf$|validate.rtsp.*playback.*change_state_intensive.*mxf$',
             'Actions on MXF streams with rtsp-server fail in racy ways.'
             ' (Deactivating as it is not very important.)'),
            ('validate.rtsp.*pal-dv25_mxf$',
             'File has decoding issues with rtsp-server.'
             ' (Deactivating as it is not very important.)'),
             ("(?!.*.media_check.qtdemux-test-frag-basic_zero_dur_no_mehd_mp4).*.qtdemux-test-frag-basic_zero_dur_no_mehd_mp4",
              '`qtdemux-test-frag-basic_zero_dur_no_mehd_mp4` is there only for media_check tests.'),
             ('validate.rtsp.*playback.*mp3_h265_0_mp4$',
              'The version of libav shipped by Fedora 29 crashes in various ways with these tests.'),
             (' validate.rtsp.*playback.seek.*GH1_00094_1920x1280_MTS',
              'Do not preroll after pause.'),
             ]


def setup_tests(test_manager, options):
    testsuite_dir = os.path.realpath(os.path.join(os.path.dirname(__file__)))

    assets_dir = os.path.realpath(os.path.join(testsuite_dir, os.path.pardir, "medias", "defaults"))
    if options.sync:
        if not update_assets(options, assets_dir):
            return False

    options.add_paths(assets_dir)
    options.set_http_server_dir(os.path.join(testsuite_dir, os.path.pardir, "medias"))
    test_manager.set_default_blacklist(BLACKLIST)

    pipelines_tests = os.path.join(testsuite_dir, 'pipelines.json')

    test_manager.add_generators(
        test_manager.GstValidatePipelineTestsGenerator.from_json(test_manager, pipelines_tests, extra_data={
            "medias": os.path.join(testsuite_dir, os.path.pardir, "medias"),
            "validate-flow-expectations-dir": os.path.join(testsuite_dir, os.path.pardir, "flow-expectations"),
            "validate-flow-actual-results-dir": test_manager.options.logsdir,
        })
    )

    test_manager.add_expected_issues(KNOWN_ISSUES)
    test_manager.register_defaults()

    test_manager.add_encoding_formats([MediaFormatCombination("quicktime", "rawaudio", "prores")])

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
                                                             "synchronized": {"mixer_props": "sink_1::alpha=0.5 sink_1::xpos=50 sink_1::ypos=50",  # noqa
                                                                              "sources":
                                                                              ("videotestsrc pattern=snow timestamp-offset=3000000000 ! 'video/x-raw,format=AYUV,width=640,height=480,framerate=(fraction)30/1' !  timeoverlay",  # noqa
                                                                               "videotestsrc pattern=smpte ! 'video/x-raw,format=AYUV,width=800,height=600,framerate=(fraction)10/1' ! timeoverlay")},  # noqa
                                                             "bgra": ("videotestsrc ! video/x-raw, framerate=\(fraction\)10/1, width=100, height=100",  # noqa
                                                                      "videotestsrc ! video/x-raw, framerate=\(fraction\)5/1, width=320, height=240")
                                                        },
                                                        valid_scenarios=valid_mixing_scenarios))

    test_manager.add_generators(
        test_manager.GstValidateMixerTestsGenerator("audiomixer.simple", test_manager,
                                                    "audiomixer",
                                                    "audio",
                                                    converter="audioconvert ! audioresample",
                                                    mixed_srcs={"basic": {"mixer_props": "",
                                                                "sources": ("audiotestsrc wave=triangle",
                                                                            "audiotestsrc wave=ticks")}},
                                                    valid_scenarios=valid_mixing_scenarios))

    return True
