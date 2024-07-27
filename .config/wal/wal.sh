#!/bin/bash

# Runs pywal and updates themes in pywal linked apps

~/.config/waybar/scripts/launch.sh
~/.config/dunst/reload_dunst.sh
pywalfox update
pywal-discord -t default

