#!/bin/bash

# Création et installation de l'environnement anaconda sur la machine utilisée
set -euo pipefail 

conda create -y --name myenv python=3.7 pip pandas openpyxl pip requests
conda activate myenv
conda install -c anaconda openpyxl
conda install -c pandas 
conda install -c sys 
conda install -c json 
conda install -c conda-forge xorg-libx11
conda install -c conda-forge tk
conda install -c conda-forge/label/gcc7 tk
conda install -c conda-forge/label/broken tk
conda install -c conda-forge/label/cf201901 tk
conda install -c conda-forge/label/cf202003 tk