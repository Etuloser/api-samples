import sys

import pytest

from google.oauth2.file import Storage
from oauth2client.tools import run_flow

from samples.comment_threads import (
    get_authenticated_service,
    CLIENT_SECRETS_FILE,
    YOUTUBE_READ_WRITE_SSL_SCOPE,
    MISSING_CLIENT_SECRETS_MESSAGE,
)
from oauth2client.client import flow_from_clientsecrets


def test_comment_threads():
    got = get_authenticated_service(args=())
    print(got)


def test_storage():
    storage = Storage("%s-oauth2.json" % sys.argv[0])
    print(storage)


def test_flow():
    flow = flow_from_clientsecrets(
        CLIENT_SECRETS_FILE,
        scope=YOUTUBE_READ_WRITE_SSL_SCOPE,
        message=MISSING_CLIENT_SECRETS_MESSAGE,
    )
    storage = Storage("comment-oauth2.json")
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage)
