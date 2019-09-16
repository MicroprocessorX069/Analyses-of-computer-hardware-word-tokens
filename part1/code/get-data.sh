#!/bin/sh
echo "file name is $1"

while read line;
do
    ccfiles=("${ccfiles[@]}" "${line}")
done <$1

for ccfile in ${ccfiles[@]}; do
  mkdir -p `dirname $ccfile`
  echo "Downloading `basename $ccfile` ..."
  echo "---"
  curl -O https://commoncrawl.s3.amazonaws.com/$ccfile
  substr=${ccfile##*/}
  echo ${substr}
  gzip -d ${substr}
done
