#!/bin/bash 

APP=wayshot
EXTENSION=png
FORMAT=$(date +"%y-%m-%d_%H:%M:%S_$APP.$EXTENSION")
MONITOR1=DP-2
MONITOR2=DP-1
options=("screenshot full" "screenshot monitor 1" "screenshot select (slurp)" "screenshot monitor 2")
num_options=${#options[@]}

if [[ -z "$1" ]] || [[ $# -gt 1 ]]; then
   echo "invalid number of arguments"
   exit 1
fi 

if [[ ! $1 =~ ^[0-9]+$ ]] || (( $1 < 0 || $1 >= num_options)); then 
    echo "argument must be an integer between 0 and $((num_options-1))"
    for i in ${!options[@]}; do 
        echo "$i: ${options[$i]}"
    done
    exit 1
fi

case $1 in

    0)
        $APP -f $screenshot_path/$FORMAT
        ;;
    
    1)
        $APP -o $MONITOR1 -f $screenshot_path/$FORMAT
        ;;
    
    2)
        $APP -s "$(slurp)" -f $screenshot_path/$FORMAT
        ;;
    
    3)
        $APP -o $MONITOR2 -f $screenshot_path/$FORMAT 
        ;;
    
    *)
        echo -n "unknown"
        ;;
esac

