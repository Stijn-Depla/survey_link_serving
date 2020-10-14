"""
Pipeline calling Castor API and requesting new survey link when activated
"""

from typing import Tuple


def pipeline_serve_link() -> Tuple[int, str, str]:
    return 401, "Dummy version", "www.success.com"
