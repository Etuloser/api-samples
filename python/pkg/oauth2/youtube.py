import os

import googleapiclient.discovery

from configs.configs import api_service_name, api_version, client_secrets_file, BASE_DIR
from pkg.oauth2.obtaining_credentials import (
    create_credentials_instance,
    obtaining_credentials,
    save_credentials,
)


def get_youtube_api_instance(credentials_name, scopes):
    credentials_path = os.path.join(
        BASE_DIR, "tokens", f"{credentials_name}-oauth2.json"
    )
    if not os.path.isfile(credentials_path):
        credentials = obtaining_credentials(client_secrets_file, scopes)
        save_credentials(credentials, credentials_path)
    credentials = create_credentials_instance(credentials_path)
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials
    )
    return youtube
