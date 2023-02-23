#!/bin/bash

while true;
do
    mem=$(free -m | awk '/Mem/{print $3}')
    if (( $(echo "$mem > 90" | bc -l) )); then
        curl -X GET http://127.0.0.1:8080/
    fi
    sleep 60
done