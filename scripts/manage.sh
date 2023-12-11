#!/bin/bash -xv
for file in tmp/images/*.jpg; do   ls -la | sha1sum "$file" ; done