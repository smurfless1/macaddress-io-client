"""CLI client wrapping the macaddress.io API."""
import os
import sys

import click
import getpass
import keyring

from .client import query_for_address


@click.group
def root():
    """A group to add commands to."""


@root.command
def save_api_key():
    """
    Save the API key securely

    We can safely assume macaddress.io is the service name, but we can't really guess the user name.
    This is never sent anywhere, it's just so we can use keyring to find the right entry.
    """
    user_password = getpass.getpass("Enter your API key for macaddress.io:")
    keyring.set_password(
        service_name="macaddress.io", username=getpass.getuser(), password=user_password
    )


def return_key_or_prompt_user():
    key = os.environ.get("MACADDRESS_IO_KEY")
    if key is None:
        key = keyring.get_password(
            service_name="macaddress.io", username=getpass.getuser()
        )
        if key is None or key == "":
            print(
                "The API Key for macaddress.io is missing or empty. Please use 'macaddress-io-client save-api-key' "
                "to store it, or export MACADDRESS_IO_KEY."
            )
            sys.exit(-1)
    return key


@root.command
def doctor():
    """
    Check if anything needs fixing

    Make sure we are ready to make API requests by checking that we get
    a valid password response keyring.

    Reminds me of 'brew doctor' which fills a similar role.

    :return:
    """
    return_key_or_prompt_user()


@root.command
@click.argument("address")
def get(address: str):
    """
    Get the MAC address response from macaddress.io

    :param address:
    :return:
    """
    key = return_key_or_prompt_user()
    response, error = query_for_address(key, address)
    if response is not None:
        print(response)
    if error is not None:
        print(f"An error or warning was returned with the response: {error}")
