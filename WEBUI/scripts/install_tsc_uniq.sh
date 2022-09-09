#!/bin/bash

export MICROMDM_ENV_PATH="$(pwd)/env"

manifest_url=https://yourdomain.com//repo/munkitools-4.1.4.3949.plist
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

# Function to install profile
function install_application {
source $MICROMDM_ENV_PATH
endpoint="v1/commands"
jq -n \
  --arg request_type "InstallApplication" \
  --arg udid "$1" \
  --arg manifest_url "$2" \
  '.udid = $udid
  |.request_type = $request_type
  |.manifest_url = $manifest_url
  '|\
  curl $CURL_OPTS \
    -H "Content-Type: application/json" \
    -u "micromdm:$API_TOKEN" "$SERVER_URL/$endpoint" -d@-
}



    udid=$(getUdidForSerial $serial $hostname $apiKey)
    if [ "$udid" != "null" ]; then
        # Send the install_profile command
        install_application $udid $manifest_url #$hostname $apiKey
fi
