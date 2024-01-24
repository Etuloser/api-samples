import json
import os

from datetime import datetime

import google_auth_oauthlib.flow
import google.oauth2.credentials


def obtaining_credentials(client_secrets_file, scopes):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes
    )
    credentials = flow.run_local_server()
    return credentials


def save_credentials(credentials, path):
    with open(path, "w") as f:
        f.write(credentials.to_json())


def create_credentials_instance(credentials_path):
    with open(credentials_path, "r") as f:
        token = json.loads(f.read())
        token["expiry"] = datetime.strptime(token["expiry"], "%Y-%m-%dT%H:%M:%S.%fZ")
        credentials = google.oauth2.credentials.Credentials(**token)
        return credentials
