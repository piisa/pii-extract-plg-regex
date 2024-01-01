"""
Detection and validation of Indian Aadhaar identity number

Since it contains a check digit, it can be validated.
"""

import re

from stdnum.in_ import aadhaar

from typing import Iterable

from pii_data.types import PiiEnum


_AADHAAR_REGEX = re.compile(r"[2-9]\d{3}\ ?\d{4}\ ?\d{4}", flags=re.X)


def IN_aadhaar_number(doc: str) -> Iterable[str]:
    """
    Aadhaar identity number from India, using regex + checksum validation
    """
    for candidate in _AADHAAR_REGEX.findall(doc):
        if aadhaar.is_valid(candidate):
            yield candidate


PII_TASKS = {
    "class": "callable",
    "task": IN_aadhaar_number,
    "method": "soft-regex,checksum",
    "pii": {
        "type": PiiEnum.GOV_ID,
        "subtype": "Indian Aadhaar number"
    }
}
