#!/bin/bash

USER="jleland"
OPTION="Y"
NODE="1"

if [ $# -ge 1 ]; then NODE=$1; fi
if [ $# -ge 2 ]; then USER=$2; fi
if [ $# -ge 3 ]; then OPTION=$3; fi


ssh $USER@login$NODE.cumulus.hpc.l -$OPTION


