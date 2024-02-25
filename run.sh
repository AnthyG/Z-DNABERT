#!/bin/bash
set -euxo pipefail

if ! type "virtualenv" > /dev/null; then
	pyvenv="python3.10 -m venv"
else
	pyvenv="virtualenv"
fi

unset SOURCE_DATE_EPOCH
$pyvenv venv/
source venv/bin/activate
TMPDIR=~/tmp python3.10 -m pip install -r requirements.txt
jupyter lab

