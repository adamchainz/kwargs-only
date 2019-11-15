#!/bin/sh
set -ex
export CUSTOM_COMPILE_COMMAND="./compile.sh"
python2.7 -m piptools compile --generate-hashes "$@" -o py27.txt
python3.4 -m piptools compile --generate-hashes "$@" -o py34.txt
python3.5 -m piptools compile --generate-hashes "$@" -o py35.txt
python3.6 -m piptools compile --generate-hashes "$@" -o py36.txt
python3.7 -m piptools compile --generate-hashes "$@" -o py37.txt
python3.8 -m piptools compile --generate-hashes "$@" -o py38.txt
