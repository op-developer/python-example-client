# coding=utf-8
import requests

# This example uses Requests HTTP Library

API = 'https://sandbox.eu-de.mybluemix.net'


def account_get_all(headers):
    '''
    Returns all accounts from owner
    '''
    url = API + '/api/accounts'

    # Make get request to API with headers
    response = requests.get(url, headers=headers)
    return response.json()


def account_get_by_id(account_id, headers):
    '''
    Returns one account by id from owner
    '''
    url = API + '/api/accounts/{}'.format(account_id)

    # Makes get request to API with headers
    response = requests.get(url, headers=headers)
    return response.json()


def account_transactions(account_id, headers):
    url = API + '/api/accounts/{}/transactions'.format(account_id)
    response = requests.get(url, headers=headers)
    return response.json()


def holdings(headers):
    url = API + '/api/holdings'
    response = requests.get(url, headers=headers)
    return response.json()


def holdings_by_id(owner_id, headers):
    url = API + '/api/holdings/{}'.format(owner_id)
    response = requests.get(url, headers=headers)
    return response.json()


def funds(headers):
    url = API + '/api/funds'
    response = requests.get(url, headers=headers)
    return response.json()


def funds_by_id(fund_id, headers):
    url = API + '/api/funds/{}'.format(fund_id)
    response = requests.get(url, headers=headers)
    return response.json()
