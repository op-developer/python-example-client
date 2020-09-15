# coding=utf-8
import requests
import json

# This example uses Requests HTTP Library

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

API = config['API']['baseUrl']


def accounts_all(headers):
    '''
    Returns all accounts from owner
    '''
    url = API + '/accounts/v3/accounts'

    # Make get request to API with headers
    response = requests.get(url, headers=headers)
    return response.json()


def account_by_id(account_id, headers):
    '''
    Returns one account by id from owner
    '''
    url = API + '/accounts/v3/accounts/{}'.format(account_id)

    # Makes get request to API with headers
    response = requests.get(url, headers=headers)
    return response.json()


def account_transactions(account_id, headers):
    url = API + '/accounts/v3/accounts/{}/transactions'.format(account_id)
    response = requests.get(url, headers=headers)
    return response.json()


def account_transaction_by_id(account_id, transaction_id, headers):
    url = API + \
        '/accounts/v3/accounts/{}/transactions/{}'.format(
            account_id, transaction_id)
    response = requests.get(url, headers=headers)
    return response.json()
