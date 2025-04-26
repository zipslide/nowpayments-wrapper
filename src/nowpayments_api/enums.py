from enum import Enum, auto

class PaymentStatus(str, Enum):
    '''
    Payment status values returned by the API
    '''
    WAITING        = 'waiting'
    CONFIRMING     = 'confirming'
    CONFIRMED      = 'confirmed'
    SENDING        = 'sending'
    PARTIALLY_PAID = 'partially_paid'
    FINISHED       = 'finished'
    FAILED         = 'failed'
    REFUNDED       = 'refunded'
    EXPIRED        = 'expired'


class InvoiceStatus(str, Enum):
    '''
    Invoice status values returned by the API
    '''
    NEW       = 'new'
    PENDING   = 'pending' 
    CONFIRMED = 'confirmed'
    EXPIRED   = 'expired'
    FAILED    = 'failed'
    PAID      = 'paid'


class CurrencyCoins(str, Enum):
    '''
    Cryptocurrency coins
    '''
    BTC  = 'btc'
    ETH  = 'eth' 
    LTC  = 'ltc'
    XRP  = 'xrp'
    DOGE = 'doge'
    BCH  = 'bch'
    USDT = 'usdt'
    USDC = 'usdc'
    #... todo


class FiatCurrencyCodes(str, Enum):
    '''
    Common fiat currency codes for price_currency
    '''
    USD = 'usd'
    EUR = 'eur'
    GBP = 'gbp'
    #... todo

class CallbackURLType(str, Enum):
    '''
    Types of callback URL that can be specified
    '''
    SUCCESS_URL = 'success_url'
    CANCEL_URL = 'cancel_url'
    IPN_CALLBACK_URL = 'ipn_callback_url'
