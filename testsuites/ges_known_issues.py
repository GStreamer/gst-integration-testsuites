KNOWN_ISSUES = {
    'https://gitlab.freedesktop.org/gstreamer/gst-editing-services/issues/27': {
        'tests': ['ges.playback.scrub_forward_seeking.test_mixing.*mp3.*'],
        'issues': [
            {
                'summary': 'position after a seek is wrong',
                'sometimes': True,
            }
        ]
    },
}