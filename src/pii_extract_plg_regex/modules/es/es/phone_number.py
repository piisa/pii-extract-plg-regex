"""
Spanish phone numbers, fixed and mobile
"""

import re

from typing import Iterable

import phonenumbers

from pii_data.types import PiiEnum

# ----------------------------------------------------------------------------

# Regex for mobile & landline phone numbers.
# Also includes the 016 Domestic abuse helpline, which by law cannot appear in phone bills
PHONE_REGEX = r'''(?<!\w)
                     (?: \d{3} \s? \d{3} \s? \d{3}
                     |
                     (?: \d{3} \s? \d{2} | \d{2} \s? \d{3}) \s? \d{2} \s? \d{2}
                     |
                     016
                     ) \b'''


# compiled regex
_REGEX_CCC = None


def spanish_phone_number(text: str) -> Iterable[str]:
    """
    Spanish Phone Numbers, mobile & landline
    """
    # Compile regex if needed
    global _REGEX_CCC
    if _REGEX_CCC is None:
        _REGEX_CCC = re.compile(PHONE_REGEX, flags=re.X)
    # Find all CCCs
    for item in _REGEX_CCC.findall(text):
        ph = phonenumbers.parse(item, "ES")
        if item == "016" or phonenumbers.is_valid_number(ph):
            yield item


# ---------------------------------------------------------------------

PII_TASKS = {
    "class": "callable",
    "task": spanish_phone_number,
    "pii": PiiEnum.PHONE_NUMBER,
    "method": "weak-regex,validation,context",
    "context": {
        "value": r"\b (?: tf | tel[ée]fonos? | llam[aeoáéó][bdimrs]?\w* ) \b",
        "width": [64, 64],
        "type": "regex"
    }
}
