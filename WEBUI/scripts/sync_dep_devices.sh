#!/bin/bash

################ Login.sh #############################
#sync_dep_devices  

export MICROMDM_ENV_PATH="$(pwd)/env"


source $MICROMDM_ENV_PATH
endpoint="v1/dep/syncnow"
curl $CURL_OPTS -u "micromdm:$API_TOKEN" -X POST "$SERVER_URL/$endpoint"

exit 0
