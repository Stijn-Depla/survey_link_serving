"""
Pipeline calling Castor API and requesting new survey link when activated
"""

from typing import Tuple, Union
from os import environ
import json
import requests


def pipeline_serve_link() -> Tuple[int, str, Union[str, None]]:
    try:
        i_base_url = 'https://data.castoredc.com'
        i_token_path = '/oauth/token'
        i_api_request_path = '/api'

        # Get token
        response_token = requests.post(i_base_url + i_token_path,
                                       data={'client_id': environ["CLIENT_ID"],
                                             'client_secret': environ["CLIENT_SECRET"],
                                             'grant_type': 'client_credentials'})
        i_token = json.loads(response_token.text)['access_token']

        print(i_token)
        return 200, "Produced a response token: " + i_token, "https://www.success.com/"
    except Exception as e:
        print(e)
        return 500, "Pipeline error occurred: " + str(e), None
