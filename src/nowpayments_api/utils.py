import json
import hmac
import hashlib
from typing import Dict, Any

def verify_ipn_signature(secret_key: str, x_signature: str, payload: Dict[str, Any]) -> bool:
    '''
    Verify the HMAC signature from an IPN callback.
    
    Args:
        secret_key: Your NOWPayments IPN secret key
        x_signature: The X-Nowpayments-Sig header value
        payload: The callback JSON payload as a dictionary
        
    Returns:
        bool: True if the signature is valid, False otherwise
    '''
    sorted_payload = json.dumps(payload, separators=(',', ':'), sort_keys=True)
    
    computed_sig = hmac.new(
        str(secret_key).encode(),
        sorted_payload.encode(),
        hashlib.sha512
    ).hexdigest()
    
    return computed_sig == x_signature


def format_decimal(value: float) -> str:
    '''
    Format a decimal value according to API requirements.
    Removes trailing zeros and decimal point if needed.
    
    Args:
        value: The decimal value to format
        
    Returns:
        str: Formatted decimal value as a string
    '''
    formatted = str(value)
    
    # rm trailing zeros.
    if '.' in formatted:
        formatted = formatted.rstrip('0').rstrip('.')
    
    return formatted


def build_query_string(params: Dict[str, Any]) -> str:
    '''
    Build a URL query string from parameters.
    
    Args:
        params: Dictionary of query parameters
        
    Returns:
        str: Formatted query string (without leading '?')
    '''
    return '&'.join([f'{k}={v}' for k, v in {k: v for k, v in params.items() if v is not None}.items()])
