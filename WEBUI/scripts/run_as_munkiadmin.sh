#!/bin/bash

if [ $(id -un) != youraccount ]; then
    exec sudo -u youraccount "$0" "$@"
fi

PATH=/home/youraccount/bin:/home/youraccount/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
USER=youraccount
HOME=/home/youraccount

eval $1
