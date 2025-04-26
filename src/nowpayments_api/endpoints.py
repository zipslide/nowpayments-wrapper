'''
NOWPayments API endpoints
'''

# Status and Information
CURRENCIES           = '/currencies'
STATUS               = '/status'
ESTIMATE             = '/estimate'
MINIMUM_AMOUNT       = '/min-amount'
AVAILABLE_CURRENCIES = '/merchant/coins' 

# Authentication
AUTHENTICATE         = '/auth'

# Payments
CREATE_PAYMENT       = '/payment'
GET_PAYMENT          = '/payment/{}'  # format with payment_id
GET_PAYMENTS         = '/payment'    # with date_from and date_to as query params

# Invoices
CREATE_INVOICE       = '/invoice'
GET_INVOICE          = '/invoice/{}'  # format with invoice_id

# Payouts
CREATE_PAYOUT        = '/payout'
GET_PAYOUT           = '/payout/{}'    # format with payout_id

# Balance
GET_BALANCE          = '/balance' 