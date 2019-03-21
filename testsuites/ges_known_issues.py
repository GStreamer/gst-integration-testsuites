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
    "https://gitlab.freedesktop.org/gstreamer/gst-editing-services/issues/65": {
        "tests": [
            "ges.playback.scrub_backward_seeking.test_transition.*"
        ],
        "issues": [
            {
                "issue-id": "event::segment-has-wrong-start",
                "summary": "A segment doesn't have the proper time value after an ACCURATE seek",
                "level": "critical",
                "can-happen-several-times": True,
            },
        ],
    },
}