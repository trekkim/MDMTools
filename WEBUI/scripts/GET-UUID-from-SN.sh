#!/bin/bash

#  manageVPP.sh
#  
#  Script to set up and use a VPP Token with MicroMDM.
#  With no parameters, it outputs all assets for the VPP Token.
#  With a serial number parameter, it outputs all licenses to which the serial is assigned
#  With both serial number and appId parameters, it assigns the serial to an app and sends the install command
#
#  Created by Jacob Jensen on 10/11/18.
#  
export MICROMDM_ENV_PATH="$(pwd)/env"


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

exit 0