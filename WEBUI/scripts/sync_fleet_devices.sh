#!/bin/bash
# The URL and API Key of the MicroMDM Server
export MICROMDM_ENV_PATH="$(pwd)/env"

mobileconfig='/home/youraccount/DEP_tool/profiles/enroll.mobileconfig'
serial="$1"



#if TXT file use this and comment JSON
# filename='serials.txt'

# while read line; do
# echo "Pushing app to : $line"

json='/home/youraccount/DEP_tool/configs/DEP-Profile.json'
cat $json | jq -r '.devices[]' | while read line; do
echo "Pushing to : $line"

# reading each line
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
function install_profile {
source $MICROMDM_ENV_PATH
    endpoint="v1/commands"
    jq -n \
    --arg request_type "InstallProfile" \
    --arg udid "$1" \
    --arg payload "$(cat "$2"|openssl base64 -A)" \
    '.udid = $udid
    |.payload = $payload 
    |.request_type = $request_type
    '|\
    curl $CURL_OPTS -u "micromdm:$API_TOKEN" "$SERVER_URL/$endpoint" -d@-
}



    udid=$(getUdidForSerial $line $hostname $apiKey)
    if [ "$udid" != "null" ]; then
        # Send the install_profile command
        install_profile $udid $mobileconfig #$hostname $apiKey
fi
done # < $filename  #remove "< $filename" if JSON method