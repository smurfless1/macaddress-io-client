from typing import Optional, Tuple

from furl import furl
import requests


def query_for_address(
    api_key: str, address: str
) -> Tuple[Optional[str], Optional[str]]:
    """
    Return the response from macaddress.io

    :param api_key:
    :param address:
    :return: Tuple of API response, error message. Either can be None.
    """
    # let furl handle the url encoding
    furl_url = furl("https://api.macaddress.io/v1")
    furl_url.args = {
        # 'output': 'vendor',  # default - test without later
        "search": address,
    }
    final_url = str(furl_url)
    headers = {"X-Authentication-Token": api_key}

    try:
        resp = requests.get(final_url, headers=headers)
        resp.raise_for_status()
        return (
            resp.text,
            None if resp.text != "" else "An empty value is still a valid response",
        )
    except (requests.exceptions.RequestException,) as any_exception:
        return None, (str(any_exception))
    except BaseException as any_exception:
        return None, (str(any_exception))
