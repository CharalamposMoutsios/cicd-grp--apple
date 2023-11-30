#!/bin/bash

CONTAINER_NAME="pingurl-server"
IP_ADDRESS=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' "$CONTAINER_NAME")

echo "Container name: $CONTAINER_NAME"
echo "Container IP: $IP_ADDRESS"

export CONTAINER_IP="$IP_ADDRESS"
