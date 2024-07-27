#!/bin/bash

# This script will randomly go through the files of a directory, setting it
# up as the wallpaper at regular intervals
#
# NOTE: this script is in bash (not posix shell), because the RANDOM variable
# we use is not defined in posix

if [[ $# -lt 1 ]] || [[ ! -d $1 ]]; then
	echo "Usage:
	$0 <dir containing images> <interval length in minutes>
    negative interval length to will cause wallpaper to never change"
	exit 1
fi

# clear swww cache
#rm -rf $HOME/.cache/swww

# restart swww
#swww init

# Edit below to control the images transition
#export SWWW_TRANSITION_FPS=60
#export SWWW_TRANSITION_STEP=2
#export SWWW_TRANSITION=random
WAL_START=2

# This controls (in seconds) when to switch to the next image
INTERVAL=$((60*$2))

while true; do
	find "$1" -type f -name "*.jpg" -o -name "*.png" -o -name "*.gif" \
		| while read -r img; do
			echo "$((RANDOM % 1000)):$img"
		done \
		| sort -n | cut -d':' -f2- \
		| while read -r img; do
			swww img "$img"
            cp "$img" ~/.cache/current_wallpaper
            sleep $WAL_START 
            wal -i "$img" -o ~/.config/wal/wal.sh
            sleep $INTERVAL
		done
done
