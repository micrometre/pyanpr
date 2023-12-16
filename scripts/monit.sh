#!/bin/bash
#dir=public/upload/alprVideo.mp4
 #for file in static/images/*.jpg; do   ls -la | sha1sum "$file" ; done
pwd
#dir=static/images
#inotifywait -m    static/images 
inotifywait --monitor --timefmt '%F%T' --format '%f' --recursive   -e create static/images
 #for file in tmp/images/*.jpg; do   ls -la | sha1sum "$file" ; done
      