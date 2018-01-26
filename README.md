# python-example-client

This example uses [Requests HTTP Library](https://github.com/requests/requests)

To use this example:

* Clone this repository
* install Requests from pip

    ```
    pip install requests
    ```

* Set your enviroment variable X_API_KEY to be your api-key
    * On bash
        ```
        export X_API_KEY=your_api_key
        ```
    * On Windows command prompt
        ```
        set X_API_KEY=your_api_key
        ```
* Or change header from source code
* Run code

```
    python client.py
```

Example should print receiver account information before and after 10€ transaction

For more information about our APIs, visit OP-Developer [website](https://op-developer.fi)
