import getpass
import unittest
from unittest.mock import patch, MagicMock

from macaddress_io_client.client import query_for_address


@patch("macaddress_io_client.client.requests.get")
class ClientUnitTests(unittest.TestCase):
    def test_found_value(self, mock_get: MagicMock):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "bob"
        response = query_for_address("key", "not_used")
        self.assertEqual(("bob", None), response)

    def test_empty_response_passed_up_with_note(self, mock_get: MagicMock):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = ""
        response = query_for_address("key", "not_used")
        self.assertEqual(("", "An empty value is still a valid response"), response)

    def test_http_code_not_200_passes_error_message_up(self, mock_get: MagicMock):
        mock_get.return_value.status_code = 404
        mock_get.return_value.text = ""
        mock_get.return_value.raise_for_status = MagicMock(
            side_effect=ValueError("unit test")
        )
        response = query_for_address("key", "not_used")
        self.assertEqual((None, "unit test"), response)


if __name__ == "__main__":
    unittest.main()
