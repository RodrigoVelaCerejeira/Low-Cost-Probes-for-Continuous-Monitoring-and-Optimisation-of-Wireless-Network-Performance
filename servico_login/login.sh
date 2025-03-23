#!/bin/bash

# Get the currently connected Wi-Fi network
CURRENT_SSID=$(nmcli -t -f active,ssid dev wifi | grep '^yes' | cut -d: -f2)
SSH_ADDRESS="ubuntu@192.92.147.85"
LOG_FILE="/home/ubuntu/CHANGETHIS!"
PRIVATE_KEY="CHANGETHIS!"

if [[ -z "$CURRENT_SSID" ]]; then
    exit 1
fi

ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null $SSH_ADDRESS -i $PRIVATE_KEY "echo '$(date): Connected' > $LOG_FILE"

IP_ADDRESS=$(ip -4 addr show wlan0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}')

if [[ -n "$IP_ADDRESS" ]]; then
    ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null $SSH_ADDRESS -i $PRIVATE_KEY "echo 'IPv4 address: $IP_ADDRESS' >> $LOG_FILE"
else
    ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null $SSH_ADDRESS -i $PRIVATE_KEY "echo 'Could not retrieve IPv4 adress.' >> $LOG_FILE"
fi
exit 0
