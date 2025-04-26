# NOWPayments API Wrapper

PLEASE NOTE: THIS IS ACTIVELY BEING DEVELOPED, AND WILL NOT WORK FOR YOU!!!

A Python wrapper for the NOWPayments cryptocurrency payment gateway API.

[Documentation](https://google.com/) TODO: replace this with docs site.

## Installation

```bash
pip install nowpayments-api
```

## Basic Usage

```python
from nowpayments_api import NowPaymentsClient, CurrencyCodes

client = NowPaymentsClient(
    api_key="your-api-key",
    sandbox=True  # set to false for prod.
)

currencies = client.get_currencies()

# create a payment.
payment = client.create_payment(
    price_amount=100.0,
    price_currency="usd",
    pay_currency="btc",
    order_id="your-order-id"
)

# get a payment status.
status = client.get_payment_status(payment["payment_id"])
```

## Features

- Complete API coverage for NOWPayments
- Type annotations and enum support
- IPN (Instant Payment Notification) verification
- Error handling with specific exception types
- Sandbox mode for testing


See `examples/ipn_handler.py` for a complete example.


## License

```
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.
```