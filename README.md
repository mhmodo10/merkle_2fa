# merkle_2fa
simple python script to demonstrate 2fa (hotp, totp) without saving the secret.

# Prerequisites
python 3.11
# Setup & Run
use the following commands to setup the project:
* `python -m venv venv`
* `venv\Scripts\activate`
* `pip install -r requirements.txt`
* `python ./src/__init__.py` or run the `__init__.py` file from vscode

# Usage
When you run the script, an image with google auth qrcode will be created. you can scan it to add the account to your google authenticator account.