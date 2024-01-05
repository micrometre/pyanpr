#!/bin/bash
# for i in static/tmp/*.jpg;  do  alpr -c gb   -n 1 $i done
alpr -c gb  -n 1 static/upload/ |  grep 'static\|conf' | awk '{print$1 $2}' | sed 's/-/Reg-/g;s|static/upload//|http://172.187.216.226:5000/upload/|g '
#alpr -c gb  -n 1 static/tmp/ |  grep 'static\|conf' | awk '{print$1 $2}' | sed 's/-/plate-/g; /s/sta/htt'g