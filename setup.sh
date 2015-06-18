#!/bin/bash

mkdir ~/Podcasts
mkdir ~/.dirapa
sudo cp -f ./setup/dirapa.service /etc/systemd/system/dirapa.service
sudo cp -f ./setup/dirapa.timer /etc/systemd/system/dirapa.timer
sudo cp -f ./setup/dirapa.target /etc/systemd/system/dirapa.target
cp -f ./setup/dirapa.py ~/.dirapa/dirapa.py
sudo systemctl start dirapa.timer
sudo systemctl enable dirapa.timer
sudo systemctl enable dirapa.service