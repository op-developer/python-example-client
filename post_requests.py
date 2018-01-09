# coding=utf-8
import requests
import json
# This example uses Requests HTTP Library

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

API = config['API']['baseUrl']


def payment_initiate(payer_iban, receiver_iban, amount, headers):
    '''
    Initiate payment
    '''
    body = {
        "amount": amount,
        "subject": "Client Test",
        "currency": "EUR",
        "payerIban": payer_iban,
        "valueDate": "2017-11-14T22:59:34Z",
        "receiverBic": "string",
        "receiverIban": receiver_iban,
        "receiverName": "string"
    }

    url = API + '/api/payments/initiate'

    # Make post request to API with headers and request body
    response = requests.post(url, headers=headers, json=body)
    return response.json()


def payment_confirm(payment_id, headers):
    '''
    Confirm payment using paymentId
    '''
    body = {
        'paymentId': payment_id
    }

    url = API + '/api/payments/confirm'

    # Make post request to API with headers and request body
    response = requests.post(url, headers=headers, json=body)
    return response.json()


def funds_subscriptions(fund_id, amount, iban, headers):

    body = {
        "amount": amount,
        "accountNumber": iban
    }
    url = API + '/api/funds/{}/subscriptions'.format(fund_id)

    # Make post request to API with headers and request body
    response = requests.post(url, headers=headers, json=body)
    return response.json()


def funds_redemptions(fund_id, amount, iban, headers):

    body = {
        "amount": amount,
        "accountNumber": iban
    }
    url = API + '/api/funds/{}/redemptions'.format(fund_id)

    # Make post request to API with headers and request body
    response = requests.post(url, headers=headers, json=body)
    return response.json()
