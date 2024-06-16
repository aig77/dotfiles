#!/bin/sh

if [ -f "/usr/bin/swayidle" ]; then
    echo "swayidle is installed."
    swayidle -w \
        timeout $((60*10)) 'swaylock -f' \
        timeout $((60*15)) 'hyprctl dispatch dpms off' \
        resume 'hyprctl dispatch dpms on'
else
    echo "swayidle not installed"
fi;
