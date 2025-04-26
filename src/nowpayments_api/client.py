import requests
import json
from typing import Dict, List, Optional, Union, Any

from .exceptions import NowPaymentsAPIError, AuthenticationError, RequestError
from .utils import verify_ipn_signature
from . import endpoints
from . import consts

class NowPaymentsClient:
    '''
    Client for the NOWPayments API
    
    This client handles all interactions with the NOWPayments API
    including authentication, request formation, and response handling.
    '''
    
    BASE_URL    = consts.BASE_URL
    SANDBOX_URL = consts.SANDBOX_URL
    
    def __init__(
        self, 
        api_key: str, 
        sandbox: bool = False,
        ipn_secret_key: Optional[str] = None,
        ipn_callback_url: Optional[str] = None
    ):
        '''
        Initialize the NOWPayments API client.
        
        Args:
            api_key(str): Your NOWPayments API key
            sandbox(bool): Whether to use the sandbox environment
            ipn_secret_key(str): Your IPN secret key for verifying callbacks
            ipn_callback_url(str): Your callback URL for payment notifications
        '''
        self.api_key          = api_key
        self.base_url         = self.SANDBOX_URL if sandbox else self.BASE_URL
        self.ipn_secret_key   = ipn_secret_key
        self.ipn_callback_url = ipn_callback_url
    
    def _request(
        self, 
        method: str, 
        endpoint: str, 
        params: Optional[Dict] = None, 
        data: Optional[Dict] = None
    ) -> Dict:
        '''
        Make a request to the NOWPayments API.
        
        Args:
            method: HTTP method (get, post, etc.)
            endpoint: API endpoint to call
            params: URL parameters
            data: Body data for POST requests
            
        Returns:
            API response as a dictionary
        '''
        url = f"{self.base_url}{endpoint}"
        
        headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json"
        }
        
        try:
            if method.lower() == "get":
                response = requests.get(url, headers=headers, params=params)
            elif method.lower() == "post":
                response = requests.post(url, headers=headers, json=data)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            
            if response.status_code == 401:
                raise AuthenticationError("API key is invalid or missing")
            
            if response.status_code >= 400:
                error_msg = "Unknown error"
                try:
                    error_data = response.json()
                    error_msg = error_data.get("message", "Unknown error")
                except:
                    error_msg = response.text or "Unknown error"
                
                raise NowPaymentsAPIError(
                    status_code=response.status_code,
                    error_message=error_msg,
                    response_data=response.text
                )
            
            return response.json()
            
        except requests.RequestException as e:
            raise RequestError(f"Request failed: {str(e)}")
    
    
    def get_currencies(self, fixed_rate: bool = False) -> Dict:
        '''
        Get the list of available cryptocurrencies
        
        Args:
            fixed_rate (optional: bool): Whether to return only currencies available for fixed rate exchanges
            
        Returns:
            Dictionary with available currencies
        '''
        return self._request("get", # request type
                             endpoints.CURRENCIES, # url 
                             params={"fixed_rate": "true" if fixed_rate else "false"})
    

    def get_estimate(self, amount: float, currency_from: str, currency_to: str) -> Dict:
        '''
        Get an estimated price for a cryptocurrency pair
        
        Args:
            amount: Amount of currency_from to convert
            currency_from: Source currency code
            currency_to: Target currency code
            
        Returns:
            Dictionary with estimated amount
        '''
        params = {
            "amount": amount,
            "currency_from": currency_from,
            "currency_to": currency_to
        }
        return self._request("get", endpoints.ESTIMATE, params=params)
    
    def create_payment(
        self, 
        price_amount: float, 
        price_currency: str, 
        pay_currency: Optional[str] = None,
        **kwargs
    ) -> Dict:
        '''
        Create a new payment
        
        Args:
            price_amount: Amount in fiat or crypto to be paid
            price_currency: Currency of the price amount
            pay_currency: Currency to pay with (optional)
            **kwargs: Additional parameters (ipn_callback_url, order_id, etc.)
            
        Returns:
            Dictionary with payment details
        '''
        data = {
            "price_amount": price_amount,
            "price_currency": price_currency,
            **kwargs
        }
        
        if pay_currency:
            data["pay_currency"] = pay_currency
            
        if self.ipn_callback_url and "ipn_callback_url" not in kwargs:
            data["ipn_callback_url"] = self.ipn_callback_url
            
        return self._request("post", endpoints.CREATE_PAYMENT, data=data)
    
    def get_payment_status(self, payment_id: str) -> Dict:
        '''
        Get the status of a payment
        
        Args:
            payment_id: Payment ID to check
            
        Returns:
            Dictionary with payment status and details
        '''
        endpoint = endpoints.GET_PAYMENT.format(payment_id)
        return self._request("get", endpoint)
    
    
    def create_invoice(
        self, 
        price_amount: float, 
        price_currency: str,
        order_id: Optional[str] = None,
        **kwargs
    ) -> Dict:
        '''
        Create a new invoice
        
        Args:
            price_amount: Amount in fiat or crypto to be paid
            price_currency: Currency of the price amount
            order_id: Your internal order ID (optional)
            **kwargs: Additional parameters
            
        Returns:
            Dictionary with invoice details
        '''
        data = {
            "price_amount": price_amount,
            "price_currency": price_currency,
            **kwargs
        }
        
        if order_id:
            data["order_id"] = order_id
            
        if self.ipn_callback_url and "ipn_callback_url" not in kwargs:
            data["ipn_callback_url"] = self.ipn_callback_url
            
        return self._request("post", endpoints.CREATE_INVOICE, data=data)
    
    
    def get_minimum_payment_amount(self, currency_from: str, currency_to: str) -> Dict:
        '''
        Get minimum payment amount for a given currency pair
        
        Args:
            currency_from: Source currency code
            currency_to: Target currency code
            
        Returns:
            Dictionary with minimum amount
        '''
        params = {
            "currency_from": currency_from,
            "currency_to": currency_to
        }
        return self._request("get", endpoints.MINIMUM_AMOUNT, params=params)
    
    def verify_ipn_signature(self, x_signature: str, payload: Dict) -> bool:
        '''
        Verify the signature from an IPN callback
        
        Args:
            x_signature: The X-Nowpayments-Sig header value
            payload: The callback JSON payload
            
        Returns:
            True if signature is valid, False otherwise
        '''

        if not self.ipn_secret_key:
            raise ValueError("IPN secret key is not set")
        
        return verify_ipn_signature(self.ipn_secret_key, x_signature, payload)
