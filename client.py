# coding=utf-8
import os
import get_requests
import json

HEADERS = {
    'x-api-key': os.environ.get('X_API_KEY'),
    'x-request-id': "12345",
    'x-session-id': "12345",
    'authorization': "Bearer 6c18c234b1b18b1d97c7043e2e41135c293d0da9",
}

# Returns all accounts from owner
all_accounts = get_requests.accounts_all(HEADERS)

if 'accounts' in all_accounts:
    accounts_data = all_accounts.get('accounts')

    # Find account with 'FI3959986920207073' iban
    iban_account = next(account for account in accounts_data if account.get(
        'identifier') == "FI3959986920207073")

    # Returns all transactions on account
    account_transactions = get_requests.account_transactions(
        iban_account.get("accountId"), HEADERS)

    print("Account data:\n", json.dumps(iban_account, indent=2))
    print("")
    print("Account transaction data:\n", json.dumps(
        account_transactions, indent=2))
else:
    print("Failed to fetch account information")
    print(all_accounts)
