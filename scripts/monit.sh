#!/bin/bash
# for i in static/tmp/*.jpg;  do  alpr -c gb   -n 1 $i done
alpr -c gb  -n 1 static/tmp/ |  grep 'static\|conf' | awk '{print$1 $2}' | sed 's/-/plate-/g;s|static/tmp//|http://localhost:5000/tmp/|g '
#alpr -c gb  -n 1 static/tmp/ |  grep 'static\|conf' | awk '{print$1 $2}' | sed 's/-/plate-/g; /s/sta/htt'g