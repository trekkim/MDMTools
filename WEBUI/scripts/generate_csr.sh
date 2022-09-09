#!/bin/bash

################ Generate CSR #############################
#generate CSR 



#test csr
openssl req -nodes -newkey rsa:2048 -keyout /home/youraccount/DEP_tool/upload/VendorCertificateRequest.key -out /home/youraccount/DEP_tool/upload/VendorCertificateRequest.csr -subj "/C=GB/ST=London/L=London/O=Global Security/OU=IT Department/CN=example.com"

sleep 5

cp /home/youraccount/DEP_tool/upload/VendorCertificateRequest.csr /home/youraccount/DEP_tool/DEP/static/DEP/Gen/VendorCertificateRequest.csr
exit 0
