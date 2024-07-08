#!/bin/bash

if ! [[ $1 =~ ^-?[0-9]+$ ]]; then
    echo "Error: script takes one parameter that must be a non-negative integer representing the lock time in minutes"
    exit 1
fi
     
if [ -f "/usr/bin/swayidle" ]; then
    echo "swayidle is installed."
    swayidle -w \
        timeout $((60*$1)) 'swaylock -f' \
        timeout $((60 * (5 + $1))) 'hyprctl dispatch dpms off' \
        resume 'hyprctl dispatch dpms on'
else
    echo "swayidle not installed"
fi;
