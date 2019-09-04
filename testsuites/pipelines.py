PIPELINES_DESC = {
    "aspectcropratio":
    {
        "pipeline": "videotestsrc !  aspectratiocrop name=cropper ! %(videosink)s",
        "scenarios": [
            {
                "name": "set_aspect_ratio_in_paused",
                "actions": [
                    "description, seek=true, handles-states=true",
                    "pause",
                    "set-property, playback-time=0.0, target-element-name=cropper, property-name=aspect-ratio, property-value=\"16/9\"",
                    "play",
                    "stop, playback-time=1.0"
                ]
            }
        ]
    },
    "flvdemux.audio_only":
    {
        "pipeline": "uridecodebin uri='file://%(medias)s/defaults/flv/819290236.flv' caps=audio/x-raw expose-all-streams=FALSE ! queue ! audioconvert ! audioresample ! %(audiosink)s",
        "scenarios": ["play_15s"]
    },
    "rtpsession_send_simple":
    {
        "pipeline": "rtpsession name=rtpsess   videotestsrc num-buffers=10 ! video/x-raw,format=RGB,width=\"320\",height=\"240\" ! rtpvrawpay ! rtpsess.send_rtp_sink   rtpsess.send_rtp_src   ! rtpvrawdepay ! fakesink",
        "config": [
            "%(validateflow)s, pad=fakesink0:sink, record-buffers=true, caps-properties={ media, clock-rate, encoding-name, sampling, depth, width, height, colorimetry, payload, a-framerate };"
        ]
    },
    "rtpsession_recv_simple":
    {
        "pipeline": "rtpsession name=rtpsess   videotestsrc num-buffers=10 ! video/x-raw,format=RGB,width=\"320\",height=\"240\" ! rtpvrawpay ! rtpsess.recv_rtp_sink   rtpsess.recv_rtp_src   ! rtpvrawdepay ! fakesink",
        "config": [
            "%(validateflow)s, pad=fakesink0:sink, record-buffers=true, caps-properties={ media, clock-rate, encoding-name, sampling, depth, width, height, colorimetry, payload, a-framerate };"
        ]
    },
    "flow_simple_test":
    {
        "pipeline": "videotestsrc num-buffers=3 ! fakesink",
        "config": [
            "%(validateflow)s, pad=fakesink0:sink, record-buffers=true, caps-properties={ width, height };"
        ]
    },
    "appsrc_simple_test":
    {
        "pipeline": "appsrc ! qtdemux name=demux ! video/x-h264 ! fakesink async=false demux. ! audio/x-raw ! fakesink async=false",
        "config": [
            "%(validateflow)s, pad=fakesink0:sink, record-buffers=true"
        ],
        "scenarios": [
            {
                "name": "single_push",
                "actions": [
                    "description, seek=false, handles-states=false",
                    "appsrc-push, target-element-name=appsrc0, file-name=\"%(medias)s/defaults/mp4/raw_h264.0.mp4\""
                ]
            }
        ]
    },
    "appsrc_custom_caps":
    {
        "pipeline": "appsrc ! fakesink async=false",
        "config": [
            "%(validateflow)s, pad=fakesink0:sink, record-buffers=true"
        ],
        "scenarios": [
            {
                "name": "single_push",
                "actions": [
                    "description, seek=false, handles-states=false",
                    "appsrc-push, target-element-name=appsrc0, file-name=\"%(medias)s/defaults/mp4/raw_h264.0.mp4\", caps=(GstCaps)\"video/foo\\,\\ variant\\=\\\"test-custom\\\"\"",
                    "appsrc-eos, target-element-name=appsrc0"
                ]
            }
        ]
    },
    "qtdemux_change_edit_list":
    {
        "pipeline": "appsrc ! qtdemux ! fakesink async=false",
        "config": [
            "%(validateflow)s, pad=fakesink0:sink, record-buffers=false"
        ],
        "scenarios": [
            {
                "name": "default",
                "actions": [
                    "description, seek=false, handles-states=false",
                    "appsrc-push, target-element-name=appsrc0, file-name=\"%(medias)s/fragments/car-20120827-85.mp4/init.mp4\"",
                    "appsrc-push, target-element-name=appsrc0, file-name=\"%(medias)s/fragments/car-20120827-85.mp4/media1.mp4\"",
                    "checkpoint, text=\"A moov with a different edit list is now pushed\"",
                    "appsrc-push, target-element-name=appsrc0, file-name=\"%(medias)s/fragments/car-20120827-86.mp4/init.mp4\"",
                    "appsrc-push, target-element-name=appsrc0, file-name=\"%(medias)s/fragments/car-20120827-86.mp4/media2.mp4\"",
                    "stop"
                ]
            }
        ]
    },
    "matroskademux_flush_within_cluster":
    {
        "pipeline": "appsrc ! matroskademux ! fakesink async=false",
        "config": [
            "%(validateflow)s, pad=fakesink0:sink, record-buffers=true"
        ],
        "scenarios": [
            {
                "name": "default",
                "actions": [
                    "description, seek=false, handles-states=false",
                    "appsrc-push, target-element-name=appsrc0, file-name=\"%(medias)s/fragments/feelings_vp9-20130806-242.webm/init.webm\"",
                    "appsrc-push, target-element-name=appsrc0, file-name=\"%(medias)s/fragments/feelings_vp9-20130806-242.webm/media1.webm\", size=5000",
                    "flush, target-element-name=appsrc0",
                    "checkpoint, text=\"A different cluster is pushed\"",
                    "appsrc-push, target-element-name=appsrc0, file-name=\"%(medias)s/fragments/feelings_vp9-20130806-242.webm/media2.webm\", size=10000",
                    "stop"
                ]
            }
        ]
    },
    "cenc_audio_esds_property_overrides":
    {
        "pipeline": "filesrc location=%(medias)s/encrypted/cenc-encrypted-youtube-aac.mp4 ! qtdemux ! mockdecryptor ! fakesink async=false",
        "config": [
            "%(validateflow)s, pad=fakesink0:sink, record-buffers=true"
        ]
    },
     "scaletempo_playbin_audio_filter":
    {
        "pipeline": "playbin audio-filter=scaletempo video-sink=fakesink uri=file://%(medias)s/defaults/mp4/mp3_h264.0.mp4",
        "scenarios": ["fast_forward"]
    },
    "qtdemux_reverse_playback_full_gop":
    {
        "pipeline": "filesrc location=%(medias)s/defaults/mp4/mp3_h264.0.mp4 ! qtdemux ! h264parse name=parse ! fakesink",
        "config": [
            "%(validateflow)s, pad=parse:src, record-buffers=true"
        ],
        "scenarios": [
          {
              "name": "reverse_playback_full_gop",
              "actions": [
                  "description, reverse-playback=true, seek=true, handles-states=true",
                  "include,location=includes/default-seek-flags.scenario",
                  "pause",
                  "seek, name=Reverse-seek, playback-time=0.0, rate=-1.0, start=5.0, stop=10.0, flags=\"$(default_flags)\"",
                  "play"
              ]
          }
        ]
    },
    "h264parse_trickmode_predicted":
    {
        "pipeline": "filesrc location=%(medias)s/defaults/mp4/mp3_h264.0.mp4 ! qtdemux ! h264parse name=parse ! fakesink",
        "config": [
            "%(validateflow)s, pad=parse:src, record-buffers=true"
        ],
        "scenarios": [
          {
              "name": "seek_trickmode_predicted",
              "actions": [
                  "description, seek=true, handles-states=true",
                  "pause",
                  "seek, name=trickmode-predicted-seek, rate=1.0, start=0.0, stop=\"$(duration)\", flags=\"flush+accurate+trickmode-forward-predicted\"",
                  "play"
              ]
          }
        ]
    },
    "h265parse_trickmode_predicted":
    {
        "pipeline": "filesrc location=%(medias)s/defaults/mp4/mp3_h265.0.mp4 ! qtdemux ! h265parse name=parse disable-passthrough=true ! fakesink",
        "config": [
            "%(validateflow)s, pad=parse:src, record-buffers=true"
        ],
        "scenarios": [
          {
              "name": "seek_trickmode_predicted",
              "actions": [
                  "description, seek=true, handles-states=true",
                  "pause",
                  "seek, name=trickmode-predicted-seek, rate=1.0, start=0.0, stop=\"$(duration)\", flags=\"flush+accurate+trickmode-forward-predicted\"",
                  "play"
              ]
          }
        ]
     },
    "mp4_redirect":
    {
        "pipeline": "playbin uri=pushfile://%(medias)s/defaults/mp4/redirect.mp4 name=playbin video-sink=\"%(videosink)s name=videosink\" audio-sink=\"%(audiosink)s\"",
        "scenarios": [ "play_15s" ],
        "config": [
            "%(validateflow)s, pad=qtdemux0:sink",
            "%(validateflow)s, pad=qtdemux1:sink"
        ]
     },
}

