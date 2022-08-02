#!/usr/bin/env bash

qSpotify=$(pulsemixer -l | grep 'spotify' | awk '{print $4}' | grep -o '[0-9]\+')
wSpotify=$(echo $qSpotify | awk '{print $1}')
eSpotify=$(echo $qSpotify | awk '{print $2}')
echo '        '
echo $qSpotify
echo $wSpotify
echo $eSpotify
pactl set-sink-input-volume $wSpotify -5%
pactl set-sink-input-volume $eSpotify -5%

