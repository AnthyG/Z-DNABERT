#!/bin/bash
set -euxo pipefail

python='python3.11'

if ! type "virtualenv" > /dev/null; then
	pyvenv="${python} -m venv"
else
	pyvenv="virtualenv"
fi

unset SOURCE_DATE_EPOCH
$pyvenv venv/
source venv/bin/activate
#export NVIDIA_VISIBLE_DEVICES=0
#export CUDA_VISIBLE_DEVICES=0
TMPDIR=~/tmp "${python}" -m pip install -r requirements.txt
jupyter lab
#bash
