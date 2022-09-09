#!/bin/bash

################ schedule_os_update #############################
#INSTALL iOS updates  

export MICROMDM_ENV_PATH="$(pwd)/env"


sleep 1

/home/youraccount/DEP_tool/api/commands/schedule_os_update_scan $UUID true

sleep 20

/home/youraccount/DEP_tool/api/commands/schedule_os_update $UUID iOSUpdate16G102 InstallASAP

exit 0
