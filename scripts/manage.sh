#!/bin/bash -xv
alpr -c gb  -n 1 tmp/images | sed 's|public|"http://localhost|g;s|plate0|{|g;s/.$/"]/;/: 1 result/d;s/^\s*./["/g; s/confidence:/","/g   '
