# python-example-client

This example uses [Requests HTTP Library](https://github.com/requests/requests)

## Prerequisite

- Reqister an account at [OP Developer](https://op-developer.fi/developers/register)
- Create an application in OP Developer with access to OP Accounts V3.0 API product in sandbox environment

## To use this example:

- Clone this repository
- install Requests from pip

  ```
  pip install requests
  ```

- Set your enviroment variable X_API_KEY to be your api-key
  - On bash
    ```
    export X_API_KEY=your_api_key
    ```
  - On Windows command prompt
    ```
    set X_API_KEY=your_api_key
    ```
  - On PowerShell
    ```
    $env:X_API_KEY='your_api_key'
    ```
- Or change header from source code
- Run code

```
    python client.py
```

Example prints account and transaction information from account with 'FI3959986920207073' IBAN

For more information about our APIs, visit OP Developer [website](https://op-developer.fi)
