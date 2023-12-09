#!/bin/bash -xv
#alpr -c gb  -n 1 tmp/images | awk '/-/ {print $1 "\t" $2}' 
alpr -c gb  -n 1 tmp/images | sed 's|public|"http://localhost|g;s|plate0|{|g;s/.$/"]/;/: 1 result/d;s/^\s*./["/g; s/confidence:/","/g   '




#awk '{print}'


#awk  '{sub(/public/,"http://localhost/images")   sub(/plate/, "")  } /-/' 

#alpr -c gb  -n 1 images | awk '/-/ {print $1 "\t" $2}' 
#   file="sqlite-data/collection.db"
#   if [ -f "$file" ] ; then
#       rm "$file"
#   fi
#   node -e 'console.log(v8.getHeapStatistics().heap_size_limit/(1024*1024))'
#   export NODE_OPTIONS="--max-old-space-size=5120" # Increase to 5 GB
#   export NODE_OPTIONS="--max-old-space-size=6144" # Increase to 6 GB
#   export NODE_OPTIONS="--max-old-space-size=7168" # Increase to 7 GB
#   export NODE_OPTIONS="--max-old-space-size=8192" # Increase to 8 GB
#   inotifywait -m -r -e  create public/images/

#   inotifywait --monitor --timefmt '%F %T' --format '%T %w%f %e' --recursive $1 public/images/
#   inotifywait --monitor --timefmt '%F %T' --format '%T %f' --recursive   -e create public/images/
#   inotifywait --monitor --timefmt '%F %T' --format '%T %f' --recursive   -e create public/images/
#   inotifywait --monitor --timefmt '%F %T' --format '%T%w%f' --recursive   -e create public/images/
#inotifywait --monitor --timefmt '%F%T' --format '%T%w%f' --recursive   -e create public/images
#alpr -n 1 -c gb images/  | sed 's/^\(.*\)$/echo \1/' 
#!/bin/bash
#alpr -c gb public/images -n 1
file="images"

#for d in $file ; do
   
#   alpr -c gb  -n 1 images | awk '/-/ {print $1 "\t" $2}' 

#   done     