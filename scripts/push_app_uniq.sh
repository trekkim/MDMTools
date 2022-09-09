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

# The path to the downloaded VPP Token
tokenLoc='/home/youraccount/DEP_tool/vpp_token/yourtoken.vpptoken'

# The serial to associate and lookup assets
serial="$1"
# The app id to associate to and install
appId="$2"

# Gets the content of the token
sToken=$(cat $tokenLoc)

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

# Function to install a VPP app
function installVppApplication {
    endpoint="v1/commands"
    serverURL="$3"
    apiKey="$4"
    jq -n \
      --arg request_type "InstallApplication" \
      --arg udid "$1" \
      --arg itunes_store_id "$2" \
      '.udid = $udid
      |.request_type = $request_type
      |.itunes_store_id = ($itunes_store_id|tonumber)
      |.options = '{"purchase_method":1}'
      '|\
      curl -H "Content-Type: application/json" -u "micromdm:$apiKey" "$serverURL/$endpoint" -d@-
}

# Sets the Client Context of the token to your MicroMDM server if needed
configURL=$(curl -s 'https://vpp.itunes.apple.com/WebObjects/MZFinance.woa/wa/VPPServiceConfigSrv' | jq .clientConfigSrvUrl | sed 's/"//g')
context=$(curl $configURL -s -d '{"sToken": "'$sToken'"}' | jq .clientContext | sed 's/\\//g' | sed 's/^"//' | sed 's/"$//' | jq .hostname | sed 's/"//g')
if [ "$hostname" != "$context" ]; then
    curl $configURL -s -d '{"sToken": "'$sToken'", "clientContext": "{\"hostname\":\"'$hostname'\",\"guid\":\"'$(uuidgen)'\"}"}' | jq
fi

if [ "$serial" == "" ]; then
    # Display List of Assets associated with the VPP token
    assetsURL=$(curl -s 'https://vpp.itunes.apple.com/WebObjects/MZFinance.woa/wa/VPPServiceConfigSrv' | jq .getVPPAssetsSrvUrl | sed 's/"//g')
    assets=$(curl $assetsURL -s -d '{"sToken": "'$sToken'"}')

    echo "Assets for Token:"
    echo $assets | jq
elif [ "$appId" == "" ]; then
    # Display List of Licenses associated with Serial
    licensesURL=$(curl -s 'https://vpp.itunes.apple.com/WebObjects/MZFinance.woa/wa/VPPServiceConfigSrv' | jq .getLicensesSrvUrl | sed 's/"//g')
    licenses=$(curl $licensesURL -s -d '{"sToken": "'$sToken'","serialNumber":"'$serial'"}')

    echo "Licenses for: $serial"
    echo $licenses | jq
else
    # Get List of Licenses associated with Serial
    licensesURL=$(curl -s 'https://vpp.itunes.apple.com/WebObjects/MZFinance.woa/wa/VPPServiceConfigSrv' | jq .getLicensesSrvUrl | sed 's/"//g')
    licenses=$(curl $licensesURL -s -d '{"sToken": "'$sToken'","serialNumber":"'$serial'"}')

    # Check if serial is already assigned to app
    assigned=$(echo $licenses | jq .licenses | jq '.[]' | jq '.serialNumber,.adamIdStr' | grep -A 1 $serial | grep $appId)
    if [ "$assigned" == "" ]; then
        # Associate serial to app

        # Get List of Assets associated with the VPP token
        assetsURL=$(curl -s 'https://vpp.itunes.apple.com/WebObjects/MZFinance.woa/wa/VPPServiceConfigSrv' | jq .getVPPAssetsSrvUrl | sed 's/"//g')
        assets=$(curl $assetsURL -s -d '{"sToken": "'$sToken'"}')

        # Get the pricing param for the appId
        pricing=$(echo $assets | jq .assets | jq '.[]' | jq '.adamIdStr,.pricingParam' | grep -A 1 $appId | tail -1 | sed 's/"//g')

        # Assign serial to app
        manageURL=$(curl -s 'https://vpp.itunes.apple.com/WebObjects/MZFinance.woa/wa/VPPServiceConfigSrv' | jq .manageVPPLicensesByAdamIdSrvUrl | sed 's/"//g')
        curl $manageURL -s -d '{"sToken": "'$sToken'","adamIdStr":"'$appId'","pricingParam":"'$pricing'","associateSerialNumbers":["'$serial'"]}' | jq
    fi

    udid=$(getUdidForSerial $serial $hostname $apiKey)
    if [ "$udid" != "null" ]; then
        # Send the InstallApplication command
        installVppApplication $udid $appId $hostname $apiKey
    fi
fi
