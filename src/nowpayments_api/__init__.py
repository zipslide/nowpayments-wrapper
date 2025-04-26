# src/nowpayments_api/__init__.py
from .exceptions import NowPaymentsAPIError, AuthenticationError, RequestError
from .utils import verify_ipn_signature, format_decimal
from .client import NowPaymentsClient
from . import endpoints
from .enums import (
    PaymentStatus, 
    InvoiceStatus, 
    CurrencyCoins, 
    FiatCurrencyCodes,
    CallbackURLType
)

__version__ = '0.1.0'

__all__ = [
    # client
    'NowPaymentsClient',
    
    # exceptions
    'NowPaymentsAPIError',
    'AuthenticationError',
    'RequestError',
    
    # enums
    'PaymentStatus',
    'InvoiceStatus',
    'CurrencyCoins',
    'FiatCurrencyCodes',
    'CallbackURLType',
    
    # utils
    'verify_ipn_signature',
    'format_decimal',
    
    # modules
    'endpoints',
    
    # version
    '__version__',
]