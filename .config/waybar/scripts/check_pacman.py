#!/usr/bin/python

import subprocess

#command = sys.argv[1:]
#subprocess.run(command[0], shell=True, executable="/bin/bash")


num_updates_command = "checkupdates | wc -l"
days_since_last_update_command = "last_upgrade=$(tac /var/log/pacman.log |" \
    "grep -m 1 'full system upgrade' |" \
    "cut -d ' ' -f 1 | tr -d '[]') ;" \
    "t1=$(date +%s -d $last_upgrade) ;" \
    "t2=$(date +%s) ;" \
    "echo \"$(((t2 - t1) / 86400)) days since last upgrade\""

#print(num_updates_command, days_since_last_update_command)

def run_command(command):
    try:
        result = subprocess.check_output(command, shell=True, executable="/bin/bash", stderr=subprocess.STDOUT)

    except subprocess.CalledProcessError as cpe:
        result = cpe.output

    finally:
        for line in result.splitlines():
            print(line.decode())

run_command(num_updates_command)
run_command(days_since_last_update_command)

output = '󰇚 '
