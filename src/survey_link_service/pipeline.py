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
        print(json.loads(response_token.text))
        i_token = json.loads(response_token.text)['access_token']

        # Create new record
        response_create_record = requests.post(
            i_base_url + i_api_request_path + "/study/" + environ["STUDY_ID"] + "/record",
            headers={
                'Authorization': 'Bearer ' + i_token,
                "accept": "application/hal+json",
                "Content-Type": 'application/json'
            },
            data=json.dumps({"institute_id": environ['INSTITUTE_ID']})
        )
        print(json.loads(response_create_record.text))
        i_record_id = json.loads(response_create_record.text)['id']

        # Request survey link for record
        response_request_link = requests.post(
            i_base_url + i_api_request_path + "/study/" + environ["STUDY_ID"] + "/surveypackageinstance",
            headers={
                'Authorization': 'Bearer ' + i_token,
                "accept": "application/hal+json",
                "Content-Type": 'application/json'
            },
            data=json.dumps({
                "institute_id": environ['INSTITUTE_ID'],
                "survey_package_id": environ['SURVEY_PACKAGE_ID'],
                "record_id": i_record_id,
                "email_address": "a.l.depla@umcutrecht.nl",
                "auto_send": False,
                "auto_lock_on_finish": True
            })
        )
        print(json.loads(response_request_link.text))
        i_link = "https://data.castoredc.com/survey/" + json.loads(response_request_link.text)["survey_url_string"]

        return 200, "Produced a link", i_link
    except Exception as e:
        print(e)
        return 500, "Pipeline error occurred: " + str(e), None
