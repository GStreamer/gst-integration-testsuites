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
            "validate.rtsp.playback.change_state_intensive.test5_mkv",
            "validate.rtsp.playback.change_state_intensive.raw_video_mkv",
            "validate.rtsp.playback.change_state_intensive.vorbis_vp8_0_webm",
            "validate.rtsp.playback.change_state_intensive.vorbis_vp8_1_webm",
            "validate.rtsp.playback.change_state_intensive.raw_video_avi",
            "validate.rtsp.playback.change_state_intensive.samples_multimedia_cx_testsuite_iv31_avi",
            "validate.rtsp.playback.change_state_intensive.bowlerhatdancer_sleepytom_SGP_mjpeg_avi",
            "validate.rtsp.playback.change_state_intensive.mp3_h264_1_mp4",
            "validate.rtsp.playback.change_state_intensive.raw_h264_0_mp4",
            "validate.rtsp.playback.change_state_intensive.raw_h264_1_mp4",
            "validate.rtsp.playback.change_state_intensive.mp3_h264_0_mp4",
            "validate.rtsp.playback.change_state_intensive.raw_video_mov",
            "validate.rtsp.playback.change_state_intensive.fragmented_nonseekable_sink_mp4",
            "validate.rtsp.playback.change_state_intensive.rawaudioS32LE_prores_mov",
            "validate.rtsp.playback.change_state_intensive.tron_en_ge_aac_h264_ts",
            "validate.rtsp.playback.change_state_intensive.GH1_00094_1920x1280_MTS",
            "validate.rtsp.playback.change_state_intensive.samples_multimedia_cx_flac_Yesterday_flac",
            "validate.rtsp.playback.change_state_intensive.samples_multimedia_cx_asf_wmv_low_fps_cheaterlow_wmv",
            "validate.rtsp.playback.change_state_intensive.samples_multimedia_cx_asf_wmv_elephant_asf",
            "validate.rtsp.playback.change_state_intensive.numerated_frames_blue_ogv",
            "validate.rtsp.playback.change_state_intensive.vorbis_theora_0_ogg",
            "validate.rtsp.playback.change_state_intensive.opus_1_ogg",
            "validate.rtsp.playback.change_state_intensive.vorbis_theora_1_ogg"
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