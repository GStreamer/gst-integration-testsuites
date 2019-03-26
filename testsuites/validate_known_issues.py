KNOWN_ISSUES = {
    "https://gitlab.freedesktop.org/gstreamer/gst-plugins-bad/issues/486": {
        "tests": [
            "validate.dash.playback.fast_forward.dash_exMPD_BIP_TC1",
            "validate.dash.playback.reverse_playback.dash_exMPD_BIP_TC1",
            "validate.dash.playback.seek_with_stop.dash_exMPD_BIP_TC1",
            "validate.dash.playback.scrub_forward_seeking.dash_exMPD_BIP_TC1",
            "validate.dash.playback.seek_backward.dash_exMPD_BIP_TC1",
            "validate.dash.playback.seek_forward.dash_exMPD_BIP_TC1"
        ],
        "issues": [
            {
                "detected-on": "playbin",
                "summary": "We got an ERROR message on the bus",
                "level": "critical",
                "sometimes": True,
            },
            {
                "summary": "flow return from pad push doesn't match expected value",
                "details": ".*Wrong combined flow return error.*",
                "level": "critical",
                "sometimes": True,
            },
            {
                "level": "critical",
                "summary": "The program stopped before some actions were executed",
                "sometimes": True,
            }
        ]
    },
    "https://gitlab.freedesktop.org/gstreamer/gst-plugins-base/issues/311": {
        "tests": [
            "validate.http.*.ogg$",
            "validate.http.*.ogv$",
            "validate.rtsp.*.ogg$",
            "validate.rtsp.*.ogv$",
        ],
        "issues": [
            {
                "detected-on": "playbin",
                "summary": "We got an ERROR message on the bus",
                "details": ".*No valid frames decoded before end of stream.*",
                "level": "critical",
                "sometimes": True,
            },
            {
                "level": "critical",
                "summary": "We got an ERROR message on the bus",
                "details": ".*Got error: Could not decode stream.*",
                "sometimes": True,
            },
            {
                "level": "critical",
                "summary": "The program stopped before some actions were executed",
                "sometimes": True,
            },
            {
                "summary": "The program stopped before some actions were executed",
                "issue-id": "scenario::not-ended",
                "sometimes": True,
            },
        ]
    },
    "https://gitlab.freedesktop.org/gstreamer/gst-plugins-good/issues/563": {
        "tests": [
            "validate.rtsp.playback.seek_backward.bowlerhatdancer_sleepytom_SGP_mjpeg_avi"
        ],
        "issues": [
            {
                "level": "critical",
                "summary": "The program stopped before some actions were executed",
                "sometimes": True,
            }
        ]
    },
    "https://gitlab.freedesktop.org/gstreamer/gst-plugins-good/issues/377": {
        "tests": [
            "validate.rtsp.*",
        ],
        "issues": [
            {
                "timeout": True,
                "sometimes": True,
            }
        ]
    },
    "https://gitlab.freedesktop.org/gstreamer/gst-plugins-bad/issues/744": {
        "tests": [
            "validate.file.playback.scrub_forward_seeking.op2b-mpeg2-wave_hd_mxf"
        ],
        "issues": [
            {
                "level": "critical",
                "summary": "We got an ERROR message on the bus",
                "details": ".*Got error: No valid frames decoded before end of stream.*",
                "sometimes": True,
            },
            {
                "level": "critical",
                "summary": "The program stopped before some actions were executed",
                "sometimes": True,
            }
        ]
    },
    "https://gitlab.freedesktop.org/gstreamer/gst-plugins-bad/issues/930": {
        "tests": [
            "validate.hls.playback.reverse_playback.*"
        ],
        "issues": [
            {
                'timeout': True,
                'sometimes': True,
            },
        ],
    },
    "https://gitlab.freedesktop.org/gstreamer/gst-plugins-good/issues/582": {
        "tests": [
            "validate.http.playback.reverse_playback.*"
            "validate.http.playback.*seek.*"
            "validate.http.playback.*change_state.*"
        ],
        "issues": [
            {
                'timeout': True,
                'sometimes': True,
            },
        ],
    },
    "https://gitlab.freedesktop.org/gstreamer/gst-plugins-bad/issues/609": {
        "tests": [
            "validate.hls.playback.*seek.*"
        ],
        "issues": [
            {
                'timeout': True,
                'sometimes': True,
                'stacktrace_symbols': [
                    'g_rec_mutex_lock'
                ]
            },
        ],
    },
    "https://gitlab.freedesktop.org/gstreamer/gst-plugins-good/issues/584": {
        "tests": [
            "validate.rtsp.*playback.*seek.*.samples_multimedia_cx_asf_wmv_low_fps_cheaterlow_wmv",
            "validate.rtsp.*playback.*seek.*.raw_video.*"
        ],
        "issues": [
            {
                "issue-id": "g-log::critical",
                "summary": "We got a g_log critical issue",
                "details": ".*gst_buffer_pool_acquire_buffer.*",
            },
        ],
    },
    "https://gitlab.freedesktop.org/gstreamer/gst-plugins-bad/issues/937": {
        "tests": [
            "validate.hls.playback.fast_forward.*"
        ],
        "issues": [
            {
                'timeout': True,
                'sometimes': True,
            },
        ],
    },
    "https://gitlab.freedesktop.org/gstreamer/gst-plugins-base/issues/578": {
        "tests": [
            "validate.http.playback.change_state_intensive.*ogv"
            "validate.http.playback.change_state_intensive.*ogg"
        ],
        "issues": [
            {
                'timeout': True,
                'sometimes': True,
            },
        ],
    },
    "https://gitlab.freedesktop.org/gstreamer/gst-plugins-good/issues/585": {
        "tests": [
            "validate.rtsp.*playback.*seek.*."
        ],
        "issues": [
            {
                "summary": "We got a g_log critical issue",
                "details": ".*g_hash_table_foreach_remove_or_steal.*",
            },
        ],
    },
}