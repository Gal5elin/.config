if pgrep -x "spotify" > /dev/null
        then
                playerctl play-pause -p spotify

        else
                spotify &
                sleep 3
                playerctl play-pause -p spotify
fi

