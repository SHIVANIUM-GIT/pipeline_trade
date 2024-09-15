# Pipeline Trade

This is a Python-based trading pipeline that utilizes the Fyers API for executing trades. It also leverages environment variables stored in a `.env` file for secure handling of credentials.

## Requirements

- Python 3.x
- Fyers API v3
- dotenv for managing environment variables

## Installation

To set up the project, install the necessary dependencies by running the following commands:

```bash
pip install fyers-apiv3 python-dotenv
```

## Setup

1. **Fyers API Key**:
   - Sign up on [Fyers](https://www.fyers.in/) and get your API key.
   
2. **Environment Variables**:
   - Create a `.env` file in the root of your project directory.
   - Add your Fyers API key, secret, and other credentials into this file:

   ```bash
    CLIENT_ID="your_fyers_client_id"
    SECRET_KEY="your_fyers_secret_key"
    REDIRECT_URI="your_url"
    USER_ID="your_fyers_user_id"
    PIN="your_account_pin"
    TOTP="your_totp_secret_key"

   ```

## Usage

1. Make sure to activate your Python virtual environment (if using one) before running the pipeline.
2. Run your Python script as follows:

   ```bash
   python fyersacceskey.py
   ```
