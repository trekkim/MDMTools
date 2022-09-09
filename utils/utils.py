import re
import json
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HTTP_POST_DATA = os.path.join(BASE_DIR, 'configs/HTTP_POST_DATA.json')   # Filepaths to the.json you are working with
TRAFIC_DATA = os.path.join(BASE_DIR, 'configs/TRAFIC_DATA.json')       #developer side
#TRAFIC_DATA = os.path.join(BASE_DIR, '/var/json/TRAFIC_DATA.json')      #server side
#TEMP_TRAFIC = '/root/PLAYGROUND/TEMP_TRAFIC.json'         # Just a new .json file that will be always overwritten
post_data = ''
UUID_STATUS_PAIRS = {}

with open(HTTP_POST_DATA, 'r') as post_file:              # Load HTTP POST DATA
    while True:
        line = post_file.readline()
        if not line.startswith('['):                      # Skipping the first line
            if line == '':
                break
            post_data += line
    post_file.close()

post_obj = json.loads(post_data)                          # Parse Json style

GOLDEN_UUID = str(post_obj['payload']['command_uuid'])    # Reference UUID

#HTTP_TRAFIC_re_str = r'\w+\s*:'                           # Regex for JSON-incompatible TRAFIC

HTTP_TRAFIC_re_str = r'\}}\s+'

with open(TRAFIC_DATA, 'r') as trafic_file:               # Load TRAFIC DATA
    #trafic_data=trafic_file.readlines()
    trafic_data=trafic_file.read()
    trafic_file.close()

TRAFIC_DATA_TEMP = ''

trafic_data = '[' + trafic_data + ']'
trafic_counter = len(re.findall(HTTP_TRAFIC_re_str, trafic_data))     # NEW LOGIC
trafic_need = trafic_counter - 1
trafic_data = trafic_data.replace('}}', '}},', trafic_need)

 

trafic_obj = json.loads(trafic_data)

trafic_num = int(len(trafic_obj))
#functional_n = int(trafic_num - 1)

for n in range(trafic_num):                            # iterating through the TRAFIC ARRAY ... TADY BYL SPATNEJ RANGE 
    try:
        TRAFIC_UUID = str(trafic_obj[n]['acknowledge_event']['command_uuid'])      # Getting the required TRAFIC UUID and STATUS
        TRAFIC_STATUS = str(trafic_obj[n]['acknowledge_event']['status'])   
        UUID_STATUS_PAIRS[n] = {TRAFIC_UUID:TRAFIC_STATUS}
    except:
        continue

for key in UUID_STATUS_PAIRS.keys():  
    try:
       TESTING_UUID = UUID_STATUS_PAIRS[key]
    except Exception as e:
        continue
    try:
       if GOLDEN_UUID in TESTING_UUID.keys():                                    # Check if Reference UUID matches TRAFIC UUID
           print('Approved Command UUID: ', GOLDEN_UUID)
           print('Approved Status: ', TESTING_UUID[GOLDEN_UUID])
    except:
        pass
    



