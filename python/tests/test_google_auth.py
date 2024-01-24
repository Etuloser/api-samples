import pytest

from google.oauth2 import service_account


def test_cert():
    credentials = service_account.Credentials.from_service_account_file(
        "client_secrets.json"
    )
