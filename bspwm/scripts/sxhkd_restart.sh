#!/bin/sh

pkill sxhkd
pgrep -x sxhkd > /dev/null || sxhkd &

echo 'OK...'
