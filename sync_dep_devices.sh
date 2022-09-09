#!/bin/bash

################ Login.sh #############################
#sync_dep_devices  


export MICROMDM_ENV_PATH="$(pwd)/env"


sleep 1


./api/commands/sync_dep_devices

exit 0