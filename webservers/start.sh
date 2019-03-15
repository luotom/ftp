#!/bin/sh

BASEDIR=$(cd "$(dirname "$0")";pwd)
APPDIR=$(dirname "$BASEDIR")
VENV="$APPDIR/venv"


PIDFILE="$APPDIR/run/app.pid"

if [ -e "$PIDFILE" ]; then
    exit 0
fi

source "$VENV/bin/activate"

cd "$APPDIR"

python ftp.py