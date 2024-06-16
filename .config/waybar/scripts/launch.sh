#!/bin/sh

# Quit running waybar instances
killall waybar

# Loading the configuration based on the username
if [[ $USER = "arturo" ]]
then
    waybar -c ~/.config/waybar/config & -s ~/.config/waybar/style.css
else
    waybar &
fi

exit 1
