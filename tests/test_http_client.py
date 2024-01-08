import pytest
import requests
from unittest.mock import patch
from src.http_services.http_client import HttpBinClient

URL = 'https://httpbin.org'


def test_get_ip():
    client = HttpBinClient()
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"ip": "127.0.0.1"}
        result = client.get_ip()
    assert result == {"ip": "127.0.0.1"}
    mock_get.assert_called_once_with(f"{URL}/ip")


def test_delete_request():
    client = HttpBinClient()
    with patch("requests.delete") as mock_delete:
        mock_delete.return_value.json.return_value = {"deleted": True}
        result = client.delete_request(params={"param1": "value1"})

    assert result == {"deleted": True}
    mock_delete.assert_called_once_with(f"{URL}/delete",
                                        params={"param1": "value1"})
