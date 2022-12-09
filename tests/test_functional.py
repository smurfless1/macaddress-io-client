import unittest

from macaddress_io_client.cli import return_key_or_prompt_user
from macaddress_io_client.client import query_for_address


class ClientFunctionalTests(unittest.TestCase):
    def test_basic_query(self):
        key = return_key_or_prompt_user()
        response = query_for_address(key, "44:38:39:ff:ef:57")
        self.assertEqual(("Cumulus Networks, Inc", None), response)
