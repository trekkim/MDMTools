#!/bin/bash

export MICROMDM_ENV_PATH="$(pwd)/env"

identifier='your profile identifier'
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

# Function to remove profile
function remove_profile {
source $MICROMDM_ENV_PATH
endpoint="v1/commands"
jq -n \
  --arg request_type "RemoveProfile" \
  --arg udid "$1" \
  --arg identifier $2 \
  '.udid = $udid
  |.identifier = $identifier
  |.request_type = $request_type
  '|\
  curl $CURL_OPTS -u "micromdm:$API_TOKEN" "$SERVER_URL/$endpoint" -d@-
}



    udid=$(getUdidForSerial $serial $hostname $apiKey)
    if [ "$udid" != "null" ]; then
        # Send the install_profile command
        remove_profile $udid $identifier #$hostname $apiKey
fi
