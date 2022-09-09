import string
import random
import re
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PASSCODE = os.path.join(BASE_DIR, 'configs/passcode.json')

def passcode_generator(size=6, chars=string.digits):
    
    return ''.join(random.choice(chars) for x in range(size))