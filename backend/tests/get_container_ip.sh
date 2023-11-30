#!/bin/bash

CONTAINER_NAME="pingurl-server"
IP_ADDRESS=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' "$CONTAINER_NAME")

export CONTAINER_IP="$IP_ADDRESS"
