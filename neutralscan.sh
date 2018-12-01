#!/bin/bash

ssh -L 10011:magdat.differ.nl:10011 leland@gate.differ.nl
source ~/Coding/Environments/python3.6_magopter/bin/activate
python ~/Coding/Projects/flopter/analysis/magnumrun.py
deactivate


