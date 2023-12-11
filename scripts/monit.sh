#!/bin/bash
#dir=public/upload/alprVideo.mp4
dir=public/images
inotifywait -m "$dir" -e close_write --format '%w%f' |
    while IFS=' ' read -r fname
    do
        [ -f "$fname" ] && ls "$fname"
    done

 #for file in tmp/images/*.jpg; do   ls -la | sha1sum "$file" ; done
   