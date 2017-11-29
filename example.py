# coding=utf-8
import os
import get_requests
import post_requests

HEADERS = {
    'x-api-key': os.environ.get('X_API_KEY'),
    'x-request-id': "12345",
    'x-session-id': "12345",
    'x-authorization': "fdb6c7c24bbc3a2c4144c1848825ab7d3a4ccb43",
}

# Returns all accounts from owner
accounts = get_requests.account_get_all(HEADERS)

# Returns account with id 'bb729060d23d0edf8de9abdcf7906bb183f2582f'
account_by_id = get_requests.account_get_by_id(
    'bb729060d23d0edf8de9abdcf7906bb183f2582f', HEADERS)

# Initiate 10 EUR payment from iban 'FI8359986950002741' to iban 'FI4859986920215738'
# Returns payment info
payment = post_requests.payment_initiate(
    'FI8359986950002741', 'FI4859986920215738', 10, HEADERS)

# Confirm payment with paymentId returned in initiation
# Returns payment info
confirm = post_requests.payment_confirm(payment['paymentId'], HEADERS)
