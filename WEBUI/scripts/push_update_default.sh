#!/bin/bash

export MICROMDM_ENV_PATH="$(pwd)/env"

product_key="iOSUpdate17E262"
install_action="Default"
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

# Function to iOS Update
function schedule_os_update {
source $MICROMDM_ENV_PATH
endpoint="v1/commands"
jq -n \
  --arg request_type "ScheduleOSUpdate" \
  --arg udid "$1" \
  --arg product_key "$2" \
  --arg install_action "$3" \
  '.udid = $udid 
  |.request_type = $request_type
  |.updates = [
      .product_key = $product_key
      |.install_action = $install_action
      ]
  '|\
  curl $CURL_OPTS -u "micromdm:$API_TOKEN" "$SERVER_URL/$endpoint" -d@-
}



    udid=$(getUdidForSerial $serial $hostname $apiKey)
    if [ "$udid" != "null" ]; then
        # Send the install_profile command
        schedule_os_update $udid $product_key $install_action #$hostname $apiKey
fi