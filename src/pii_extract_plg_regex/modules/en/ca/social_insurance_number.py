"""
Detection and validation of Canadian Social Insurance Number

Since it contains a check digit, it can be validated.
"""

import re

from stdnum.ca import sin

from typing import Iterable

from pii_data.types import PiiEnum


_SIN_REGEX = re.compile(r"\b \d{3} [-\ ] \d{3} [-\ ] \d{3} \b", flags=re.X)


def social_insurance_number(doc: str) -> Iterable[str]:
    """
    Canadian Social Insurance Number (detect and validate)
    """
    for candidate in _SIN_REGEX.findall(doc):
        if sin.is_valid(candidate):
            yield candidate


PII_TASKS = {
    "class": "callable",
    "task": social_insurance_number,
    "method": "regex,checksum",
    "pii": {
        "type": PiiEnum.GOV_ID,
        "subtype": "Canadian Social Insurance Number"
    }
}
