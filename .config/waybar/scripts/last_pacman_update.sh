#!/bin/bash


last_upgrade=$(tac /var/log/pacman.log |
  grep -m 1 'full system upgrade' |
  cut -d ' ' -f 1 | tr -d '[]')

t1=$(date +%s -d $last_upgrade)
t2=$(date +%s)

echo "$(((t2 - t1) / 86400)) days since last upgrade"
