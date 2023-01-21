"""
Detection and validation of Canadian Social Insurance Number

Since it contains a check digit, it can be validated.
"""

import re

from stdnum.ca import sin

from typing import Iterable, Tuple

from pii_data.types import PiiEnum


_SIN_PATTERN = r"\b \d{3} [-\ ] \d{3} [-\ ] \d{3} \b"

# -----------------------------------------------------------------

# compiled regex
_REGEX = None

def Canadian_social_insurance_number(text: str) -> Iterable[Tuple[str, int]]:
    """
    Canadian Social Insurance Number (detect and validate)
    """
    # Compile regex if needed
    global _REGEX
    if _REGEX is None:
        _REGEX = re.compile(_SIN_PATTERN, flags=re.X)

    # Find all instances
    for match in _REGEX.finditer(text):
        item_value = match.group()
        if sin.is_valid(item_value):
            yield item_value, match.start()


# -----------------------------------------------------------------

PII_TASKS = {
    "class": "callable",
    "task": Canadian_social_insurance_number,
    "method": "soft-regex,checksum",
    "pii": {
        "type": PiiEnum.GOV_ID,
        "subtype": "Canadian Social Insurance Number"
    }
}
