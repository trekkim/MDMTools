#!/bin/bash

export MICROMDM_ENV_PATH="$(pwd)/env"

pin="000000"

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

# Function to erase device
function erase_device {
source $MICROMDM_ENV_PATH
endpoint="v1/commands"
jq -n \
  --arg request_type "EraseDevice" \
  --arg udid "$1" \
  --arg pin $2 \
  '.udid = $udid 
  |.pin = $pin 
  |.request_type = $request_type
  '|\
  curl $CURL_OPTS -u "micromdm:$API_TOKEN" "$SERVER_URL/$endpoint" -d@-
}



    udid=$(getUdidForSerial $serial $hostname $apiKey)
    if [ "$udid" != "null" ]; then
        # Send the eraseDevice command
        erase_device $udid $pin #$apiKey
fi

