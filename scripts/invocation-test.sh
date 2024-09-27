#!/usr/bin/env bash

set -a

ARGV0="$0"
CMD_GIVEN=$(basename "${ARGV0}")
CMD_ARGS="$@"
SELF=$(readlink -f -- "$0")

set | grep -v ^_
