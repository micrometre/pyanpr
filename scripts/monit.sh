#!/bin/bash
# for i in static/tmp/*.jpg;  do  alpr -c gb   -n 1 $i done
alpr -c gb  -n 1 static/tmp/ |  grep 'static\|conf' | awk '{print$1 $2}' | sed 's/-/plate-/g'
#alpr -c gb  -n 1 static/tmp/ |  grep 'static\|conf' | awk '{print$1 $2}' | sed 's/-/:/g'

#alpr -c gb  -n 1 static/tmp/ |  grep 'static\|conf' | awk '{print$2 $1}'

#alpr -c gb  -n 1 static/tmp/ | sed 's/-/],[plate:/g; /plate0: 1 results/d; s/static/[img : /g; s/confidence:/]/g' | awk '{print $1 $2 $3 }' | tr -d 'n\'
#alpr -c gb  -n 1 static/tmp/ | sed 's/-/","plate":"/g; /plate0: 1 results/d; s/static/"img" : "/g; s/confidence:/"/g' | awk '{print $1 $2 $3 }'

#alpr -c gb   -n 1 static/tmp/ 

#|  grep 'static\|conf' | awk '{print$2 $1}'
#alpr -c gb  -n 1 static/tmp/ |  grep 'static\|conf' | awk '{print$2 $1}'
#sed '/plate0/d;'
#alpr -c gb  -n 1 static/tmp/ | awk '{print$2 $1 $3}' | sed '/1plate0/d;  s/-conf.*/")]/; s/static/[("img","/g;/1plate0/d; s/\jpg\b/& "),("plate"," /;  '   |  tr -d '\n'

#alpr -c gb   -n 1 static/tmp/ 

#dict
#alpr -c gb  -n 1 static/tmp/ | awk '{print$2 $1 $3}' | sed '/1plate0/d;  s/-conf.*/)"]/; s/static/[("img","/g;/1plate0/d;
# alpr -c gb  -n 1 static/tmp/ | awk '{print$2 $1 $3}' | sed '/1plate0/d; s/\jpg\b/& ", /; s/-conf.*//; s/static/"/g; s/$/"/ '   

#alpr -c gb  -n 1 static/tmp/ | sed 's/\jpg\b/& , reg /;s/conf.*//;/^$/d; /plate/d; s|static/tmp//|"img - |g; s/$/"/'
#alpr -c gb  -n 1 static/tmp/ | sed 's/\jpg\b/& , reg /;s/conf.*//;/^$/d; /plate/d; s|static/tmp//|"img - |g; '
#alpr -c gb  -n 1 static/tmp/ | sed 's/-/","plate":"/g; /plate0: 1 results/d; s/static/'\''{"img" : "/g; s/confidence:/"}'\''/g' | awk '{print $1 $2 $3 }' | tr -d '\n'
#alpr -c gb  -n 1 static/tmp/ | sed 's/-/","plate":"/g; /plate0: 1 results/d; s/static/'\''{"img" : "/g; s/confidence:/"}'\''/g' | awk '{print $1 $2 $3 }'
#alpr -c gb  -n 1 static/tmp/ | sed 's/-/","plate":"/g; /plate0: 1 results/d; s/static/{"img" : "/g; s/confidence:/"}/g' | awk '{print $1 $2 $3 }' | tr -d '\n' 
#alpr -c gb  -n 1 static/tmp/ | sed 's/-/","plate":"/g; /plate0: 1 results/d; s/static/{"img" : "/g; s/confidence:/"}/g' | awk '{print $1 $2 $3 }' | tr -d '\n' | jq
#alpr -c gb  -n 1 static/tmp/ | sed 's/-/","plate":"/g; /plate0: 1 results/d; s/static/{"img" : "/g; s/confidence:/"}/g' | awk '{print $1 $2 $3 }' | tr -d '\n' 
#alpr -c gb  -n 1 static/tmp/ | grep 'tmp\|-' | tr -d '\n' | awk {'print $1" "$2" "$3'}  | sed 's/^/{"img":"/;s/-/","plate":"/g;s/$/"}/g; s|static/tmp//|http://localhost:5000/images/|g'  | jq

#alpr -c gb  -n 1 static/tmp/ | grep 'tmp\|-' | tr -d '\n' | awk {'print $1" "$2" "$3'}  | sed 's/^/{"img":"/;s/-/","plate":"/g;s/$/"}/g; s/staic/tt/g'  | jq
#alpr -c gb  -n 1 static/tmp/ | grep 'tmp\|-' | tr -d '\n' | awk {'print $1" "$2" "$3'}  | sed 's/^/{"img":"/;s/-/","plate":"/g;s/$/"}/g; s|static/tmp//|http://localhost:3000/images/|g'  | jq
#alpr -c gb  -n 1 static/tmp/ | grep 'tmp\|-' | tr -d '\n' | awk {'print $1" "$2" "$3'}  | sed 's/^/{"img":"/;s/-/","plate":"/g;s/$/"}/g; s/tmp//g ' | jq
#alpr -c gb  -n 1 tmp/ | grep 'tmp\|-' | tr -d '\n' | awk {'print $1" "$2" "$3'}  | sed 's/^/{"/;s/-/":"/g;s/$/"}/g; ' | jq
#alpr -c gb  -n 1 tmp/ | grep 'tmp\|-' | tr -d '\n' | awk {'print $1" "$2" "$3'}  | sed "s/^/{\'/; s/-/':'/g; s/$/'}/g"

#alpr -c gb  -n 1 tmp/ | grep 'tmp\|-' | tr -d '\n' | awk {'print $1" "$2" "$3'}  | sed 's/^/{"/;s/-/":"/g;s/$/"}/g; ' 


#alpr -c gb  -n 1 tmp/ | grep 'tmp\|-' | tr -d '\n' | awk '// {print "img" ":" $1","   "plate" ":" $3}'  | sed s/$/}/g 
#alpr -c gb  -n 1 tmp/ | grep 'tmp\|-' | tr -d '\n' | sed 's/confidence://g;s/-//g ' | awk '// {print $1 "\t" $2}' 

#s/[[:digit:]]\+\./}/g
 #| sed 's|tmp| {"img", "http://|g;/: 1 result/d; s/confidence://g; s/-/","plate","/g;s/[0-9]/"}/8 '
 #alpr -c gb  -n 1 tmp/ | sed 's|tmp| {"img", "http://|g;/: 1 result/d; s/confidence://g; s/-/","plate","/g;s/[0-9]/"}/8 '
#alpr -c gb  -n 1 tmp/ | sed 's|tmp| img: http://localhost|g;/: 1 result/d; s/confidence://g; s/-/,plate:/g  '
#alpr -c gb  -n 1 tmp/ | sed 's|tmp| {"img": "http://|g;/: 1 result/d; s/confidence://g; s/-/","plate":"/g;s/[0-9]/"}/8 '
#alpr -c gb  -n 1 tmp/ | sed 's|tmp| {"img": "http://|g;/:1result/d; s/confidence://g; s/-/","plate":"/g;s/[0-9]/"}/8 '
#alpr -c gb  -n 1 tmp/ | sed 's|tmp| img: http://localhost|g;/: 1 result/d; s/confidence://g   '
#alpr -c gb  -n 1 tmp/ | sed 's|tmp|  "http://localhost|g;s|plate0|{|g;s/.$/"}/;/: 1 result/d;s/^\s*./{"plate:/g; s/confidence://g   '
 #for file in tmp/images/*.jpg; do   ls -la | sha1sum "$file" ; done
  #    alpr -c gb  -n 1 tmp/ | sed 's|tmp| {"img": "http://localhost|g;/: 1 result/d; s/confidence://g; s/-/","plate":/g  '
  #alpr -c gb  -n 1 tmp/ | sed 's|tmp| img: http://localhost|g;/: 1 result/d; s/confidence://g; s/-/,plate:/g;s/[A-Z]/\L&/g