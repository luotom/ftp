#!/bin/sh

BASEDIR=$(cd "$(dirname "$0")";pwd)
APPDIR=$(dirname "$BASEDIR")

PIDFILE="$APPDIR/run/app.pid"
SOCKFILE="$APPDIR/run/app.sock"

if [ -e "$PIDFILE" ]; then
    kill -TERM $(cat "$PIDFILE")
fi

if [ -e "$PIDFILE" ]; then
    rm -f "$PIDFILE"
fi

if [ -e "$SOCKFILE" ]; then
    rm -f "$SOCKFILE"
fi
