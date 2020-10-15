"""
Pipeline calling Castor API and requesting new survey link when activated
"""

from typing import Tuple
import castorapi as ca
from os import environ


def pipeline_serve_link() -> Tuple[int, str, str]:
    return 200, "Dummy version", "https://www.success.com/"
