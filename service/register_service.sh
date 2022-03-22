#!/bin/bash
set -e

sudo cp raspberry_monitor.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start raspberry_monitor
sudo systemctl status raspberry_monitor
