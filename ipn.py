import json 
import hmac 
import hashlib

def np_signature_check(np_secret_key, np_x_signature, message):
    
    sorted_msg = json.dumps(message, separators=(',', ':'), sort_keys=True)
    
    digest = hmac.new(
        str(np_secret_key).encode(), 
        f'{sorted_msg}'.encode(),
        hashlib.sha512)
    
    signature = digest.hexdigest()
    
    if signature == np_x_signature:
        return
    else:
        print('HMAC signature does not match')