KNOWN_ISSUES = {
    'validate.dash.playback.*seek.*|validate.dash.playback.*reverse.*'
    '|validate.dash.playback.*fast.':
    [
        {
            'bug': 'https://bugzilla.gnome.org/show_bug.cgi?id=775266',
            'detected-on': 'playbin',
            'summary': 'We got an ERROR message on the bus',
            'level': 'critical',
            'sometimes': True,
        },
        {
            'bug': 'https://bugzilla.gnome.org/show_bug.cgi?id=775266',
            'summary': "flow return from pad push doesn't match expected value",
            'details': '.*Wrong combined flow return error.*',
            'level': 'critical',
            'sometimes': True,
        },
        {
            'bug': 'https://bugzilla.gnome.org/show_bug.cgi?id=775266',
            'level': 'critical',
            'summary': 'The program stopped before some actions were executed',
            'sometimes': True,
        }
    ],
    'validate.http.*.vorbis_theora_1_ogg':
    [
        {
            'bug': 'https://bugzilla.gnome.org/show_bug.cgi?id=775107',
            'detected-on': 'playbin',
            'summary': 'We got an ERROR message on the bus',
            'details': '.*No valid frames decoded before end of stream.*',
            'level': 'critical',
            'sometimes': True,
        },
        {
            'bug': 'https://gitlab.freedesktop.org/gstreamer/gst-plugins-base/issues/311',
            'level': 'critical',
            'summary': 'We got an ERROR message on the bus',
            'details': '.*Got error: Could not decode stream.*',
            'sometimes': True,
        },
        {
            'bug': 'https://bugzilla.gnome.org/show_bug.cgi?id=775107',
            'level': 'critical',
            'summary': 'The program stopped before some actions were executed',
            'sometimes': True,
        }
    ],
    'validate.rtsp.playback.seek_backward.bowlerhatdancer_sleepytom_SGP_mjpeg_avi':
    [
        {
            'bug': 'https://gitlab.freedesktop.org/gstreamer/gst-plugins-good/issues/563',
            'level': 'critical',
            'summary': 'The program stopped before some actions were executed',
            'sometimes': True,
        },
    ],
    'validate.rtsp.playback.change_state_intensive.*':
    [
        {
            'bug': 'https://gitlab.freedesktop.org/gstreamer/gst-plugins-good/issues/377',
            'timeout': True,
            'sometimes': True,
        },
    ],
    'validate.file.playback.scrub_forward_seeking.op2b-mpeg2-wave_hd_mxf':
    [
        {
            'bug': 'https://bugzilla.gnome.org/show_bug.cgi?id=796746',
            'level': 'critical',
            'summary': 'We got an ERROR message on the bus',
            'details': '.*Got error: No valid frames decoded before end of stream.*',
            "sometimes": True
        },
        {
            'bug': 'https://bugzilla.gnome.org/show_bug.cgi?id=796746',
            'level': 'critical',
            'summary': 'The program stopped before some actions were executed',
            "sometimes": True
        }
    ],
}