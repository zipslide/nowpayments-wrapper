# src/nowpayments_api/exceptions.py

class NowPaymentsError(Exception):
    '''Base exception for this library'''
    pass

class AuthenticationError(NowPaymentsError):
    '''Raised for API key issues'''
    pass

class NowPaymentsAPIError(NowPaymentsError):
    '''Raised for errors returned by the NowPayments API.'''
    def __init__(self, status_code, error_message, response_data=None):

        self.status_code   = status_code
        self.error_message = error_message
        self.response_data = response_data
        
        super().__init__(f"API Error {status_code}: {error_message}")

class RequestError(NowPaymentsError):
    '''Raised for network or request configuration issues.'''
    pass