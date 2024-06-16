#!/bin/bash
#
# Runs pywal and updates themes in pywal linked apps

if [[ $# -ne 1 ]]; then
    echo "Usage:
    $0 <image path>"
    exit 1
fi

wal -i $1 -n
~/.config/waybar/scripts/launch.sh
pywalfox update
pywal-discord -t default

exit 1
