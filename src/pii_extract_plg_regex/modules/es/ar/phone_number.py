"""
Argentinian phone numbers, using only libphonenumbers
"""

from typing import Iterable

import phonenumbers

from pii_data.types import PiiEnum

# ----------------------------------------------------------------------------


def Argentinian_phone_number(text: str) -> Iterable[str]:
    """
    Argentinian Phone Numbers
    """
    # Compile regex if needed
    for match in phonenumbers.PhoneNumberMatcher(text, "AR"):
        yield match.raw_string


# ---------------------------------------------------------------------

PII_TASKS = {
    "class": "callable",
    "task": Argentinian_phone_number,
    "pii": {
        "type": PiiEnum.PHONE_NUMBER,
        "subtype": "Argentinian phone number",
        "method": "soft-regex,context",
        "context": {
            "type": "regex",
            "value": r"\b (?: tf | tel[ée]fonos? | llam[aeoáéó][bdimrs]?\w* ) \b",
            "width": [64, 64]
        }
    }
}
