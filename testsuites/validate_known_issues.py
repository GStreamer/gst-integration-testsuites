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
            "validate.rtsp.*.ogg$",
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
            }
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
}