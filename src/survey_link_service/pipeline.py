"""
Pipeline calling Castor API and requesting new survey link when activated
"""

from typing import Tuple
import castorapi as ca
from dotenv import load_dotenv
from os import environ


def pipeline_serve_link() -> Tuple[int, str, str]:
    return 401, "Dummy version", "www.success.com"
