#!/bin/bash

export MICROMDM_ENV_PATH="$(pwd)/env"

# The serial to associate and lookup assets
serial="$1"

# Function to get the udid of a device from a serial
function getUdidForSerial {
    endpoint="v1/devices"
    serverURL="$2"
    apiKey="$3"
    response=$(jq -n \
      --arg filter_serial "$1" \
      '.filter_serial = '"["'$filter_serial'"]"'
      '|\
      curl -s -H "Content-Type: application/json" -u "micromdm:$apiKey" "$serverURL/$endpoint" -d@-\
    )
    echo $response | jq .devices[0].udid | sed 's/"//g'
}

# Function to restart device
function restartDevice {
  source $MICROMDM_ENV_PATH
    endpoint="v1/commands"
    serverURL="$3"
    apiKey="$4"
    jq -n \
      --arg request_type "RestartDevice" \
      --arg udid "$1" \
      '.udid = $udid 
      |.request_type = $request_type
      '|\
      curl $CURL_OPTS -u "micromdm:$API_TOKEN" "$SERVER_URL/$endpoint" -d@-
}



    udid=$(getUdidForSerial $serial $hostname $apiKey)
    if [ "$udid" != "null" ]; then
        # Send the restartDevice command
        restartDevice $udid $hostname $apiKey
fi

