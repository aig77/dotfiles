#!/bin/bash

if [[ $# -lt 1 ]] || [[ ! -d $1 ]]; then
    echo "Usage:
    $0 <dir containing images>"
    exit 1
fi

#export SWWW_TRANSITION_FPS=60
#export SWWW_TRANSITION_STEP=2
#export SWWW_TRANSITION=random
WAL_START=2

img=$(find $1 -type f -name "*.jpg" -o -name "*.png" -o -name "*.gif" | shuf -n 1)

swww img "$img" 
cp "$img" ~/.cache/current_wallpaper
#cp "$img" ~/.config/rofi/background
sleep $WAL_START
wal -i "$img" -o ~/.config/wal/wal.sh

exit 1
