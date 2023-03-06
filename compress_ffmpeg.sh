#!/bin/bash

# OPTARG=1.0

# mkdir -p $WORK_DIR/${OPTARG}x_compressed/
# echo "mkdir ${ARG}x_compressed/"
# for f in *.mp4; do
#     mv $f $WORK_DIR/original/
#     ffmpeg -i $WORK_DIR/original/$f -vf setpts=PTS/${OPTARG} scale=-1:1080 -r 30 -crf 20 -an $WORK_DIR/${OPTARG}x_compressed/${f%.mp4}_${OPTARG}x_compressed.mp4; 
# done

# while getopts "v:h" OPT
# do
#   case $OPT in
#     v)
#       echo "select -v";;
#       # KEY="v"
#       # python3 $SCRIPT_DIR/python_for_sh/compress_ffmpeg.py --work_dir ${WORK_DIR} --velocity ${OPTARG};;
#     h)
#       python3 $SCRIPT_DIR/python_for_sh/compress_ffmpeg.py --help
#       ;;
#     esac
# done


WORK_DIR="`pwd`"
SCRIPT_DIR="$(cd $(dirname $0); pwd)"

echo $WORK_DIR
echo $SCRIPT_DIR

# mkdir -p $WORK_DIR/original/
# echo "mkdir original/"
# echo "------------"

if [ $# = 0 ]; then
  python3 $SCRIPT_DIR/python_for_sh/compress_ffmpeg.py --work_dir ${WORK_DIR}
else

  while getopts v:h OPT
  do
      case $OPT in
        v) 
            # echo selected a
            # echo $OPTARG
            python3 $SCRIPT_DIR/python_for_sh/compress_ffmpeg.py --work_dir ${WORK_DIR} --velocity ${OPTARG}
            ;;
        h) 
            # echo selected b
            python3 $SCRIPT_DIR/python_for_sh/compress_ffmpeg.py --help
            ;;
        \?) 
            echo "error"
            echo "you can see help by -h"
            # python3 $SCRIPT_DIR/python_for_sh/compress_ffmpeg.py --work_dir ${WORK_DIR}
            ;;
      esac
  done

fi