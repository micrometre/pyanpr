#!/bin/bash
vlc -vvv v4l2:///dev/video0 --sout '#transcode{vcodec=mp4v,acodec=none}:duplicate{dst=http{mux=ts,dst=:8082/},dst=display}' 
vlc -vvv --daemon --syslog v4l2:///dev/video0 --sout '#transcode{vcodec=mp4v,acodec=none}:duplicate{dst=http{mux=ts,dst=:8082/},dst=display}'
