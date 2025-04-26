import os
from nowpayments_api import (
    NowPaymentsClient, 
    CurrencyCoins, 
    FiatCurrencyCodes,
    PaymentStatus
)

# initialize the client
# in a real application, store API keys in environment variables, refer to .env.example
API_KEY = os.environ.get('NOWPAYMENTS_API_KEY', 'your-api-key')
IPN_SECRET = os.environ.get('NOWPAYMENTS_IPN_SECRET', 'your-ipn-secret')

# create client instance
client = NowPaymentsClient(
    api_key=API_KEY,
    sandbox=True,  # Use sandbox for testing
    ipn_secret_key=IPN_SECRET,
    ipn_callback_url='https://your-website.com/ipn-handler'
)

# Example 1: Get available currencies
def list_currencies():
    currencies = client.get_currencies()
    print('Available currencies:')
    for currency in currencies.get('currencies', []):
        print(f'- {currency}')

# Example 2: Get price estimate
def get_price_estimate():
    # Estimate how much BTC you'll get for 100 USD
    estimate = client.get_estimate(
        amount=100.0,
        currency_from=FiatCurrencyCodes.USD,
        currency_to=CurrencyCoins.BTC
    )
    print(f'Estimated BTC for 100 USD: {estimate.get('estimated_amount', 'N/A')}')

# Example 3: Create a payment
def create_payment():
    payment = client.create_payment(
        price_amount=100.0,
        price_currency=FiatCurrencyCodes.USD,
        pay_currency=CurrencyCoins.BTC,
        order_id='test-order-123',
        order_description='Test payment',
        success_url='https://your-website.com/success',
        cancel_url='https://your-website.com/cancel'
    )
    
    print(f'Created payment with ID: {payment.get('payment_id')}')
    print(f'Pay to address: {payment.get('pay_address')}')
    print(f'Pay amount: {payment.get('pay_amount')} {payment.get('pay_currency')}')
    
    return payment.get('payment_id')

# Example 4: Check payment status
def check_payment_status(payment_id):
    status = client.get_payment_status(payment_id)
    print(f'Payment status: {status.get('payment_status')}')
    
    # handle different payment statuses
    if status.get('payment_status') == PaymentStatus.FINISHED:
        print('Payment completed successfully!')
    elif status.get('payment_status') == PaymentStatus.WAITING:
        print('Waiting for payment...')
    elif status.get('payment_status') == PaymentStatus.EXPIRED:
        print('Payment expired.')

if __name__ == '__main__':
    list_currencies()
    get_price_estimate()
    
    try:
        payment_id = create_payment()
        check_payment_status(payment_id)
    except Exception as e:
        print(f'Error: {e}') 