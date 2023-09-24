#!/usr/bin/env bash
sudo apt-get update && apt-get -y install --no-install-recommends \
   python3.11-venv
USER="vscode"
VENV_PATH="/home/${USER}/venv"
su $USER -c "/usr/bin/python3 -m venv /home/${USER}/venv" \
source /home/vocode/venv/bin/activate
#append it to bash so every shell launches with it 
echo 'source /home/vscode/venv/bin/activate' >> ~/.bashrc
su $USER -c "pip3 --disable-pip-version-check --no-cache-dir install -r requirements.txt"
