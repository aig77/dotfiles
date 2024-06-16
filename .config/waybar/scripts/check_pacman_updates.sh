#!/bin/bash

num_updates=$(checkupdates | wc -l)

last_upgrade=$(tac /var/log/pacman.log | 
    grep -m 1 'full system upgrade' |
    cut -d ' ' -f 1 | tr -d '[]')
t1=$(date +%s -d $last_upgrade)
t2=$(date +%s) 
days_since_last_upgrade="$(((t2 - t1) / 86400)) days since last upgrade"

echo "{\"text\": \"󰇚 ${num_updates}\", \"tooltip\": \"${days_since_last_upgrade}\"}"
