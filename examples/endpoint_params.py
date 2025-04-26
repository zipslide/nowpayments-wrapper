import os
from nowpayments_api import NowPaymentsClient, endpoints

# initialize the client
API_KEY = os.environ.get('NOWPAYMENTS_API_KEY', 'your-api-key')
client = NowPaymentsClient(api_key=API_KEY, sandbox=True)

# Example 1: Get currencies with fixed rate parameter
def get_fixed_rate_currencies():
    '''Get currencies with fixed rate parameter'''
    print('Getting currencies with fixed_rate=true')
    currencies = client.get_currencies(fixed_rate=True)
    print(f'Found {len(currencies.get('currencies', []))} fixed-rate currencies')
    
    # direct access to endpoint with the parameter
    print('\nShowing how this maps to the endpoint URL:')
    endpoint_url = f'{client.base_url}{endpoints.CURRENCIES}?fixed_rate=true'
    print(f'Endpoint URL: {endpoint_url}')

# Example 2: Get custom date range payments
def get_date_range_payments():
    '''Get payments from a date range'''
    # NOTE: This would be implemented as a method in the client class
    # Just showing the endpoint construction here
    params = {
        'limit': 10,
        'dateFrom': '2023-01-01',
        'dateTo': '2023-12-31'
    }
    
    # in actual implementation:
    # payments = client._request('get', endpoints.GET_PAYMENTS, params=params)
    
    # show the URL that would be constructed:
    param_str = '&'.join([f'{k}={v}' for k, v in params.items()])
    endpoint_url = f'{client.base_url}{endpoints.GET_PAYMENTS}?{param_str}'
    print(f'Payments endpoint URL: {endpoint_url}')

# Example 3: Get payment by ID (path parameter)
def get_payment_by_id():
    '''Get a specific payment by ID'''
    payment_id = '12345'
    
    # in the client, this is handled by:
    # client.get_payment_status(payment_id)
    
    # this formats the URL path parameter:
    endpoint = endpoints.GET_PAYMENT.format(payment_id)
    endpoint_url = f'{client.base_url}{endpoint}'
    print(f'Payment status endpoint URL: {endpoint_url}')


if __name__ == '__main__':
    print('NOWPayments Endpoint Examples\n' + '-' * 30)
    get_fixed_rate_currencies()
    print('\n' + '-' * 30)
    get_date_range_payments()
    print('\n' + '-' * 30)
    get_payment_by_id() 