"""
Argentinian phone numbers, using only libphonenumbers
"""

from typing import Iterable

import phonenumbers

from pii_data.types import PiiEnum


# Context that must be found around the phone number
CONTEXT_REGEX = r"""
 \b
 (?:
   tel[ée]fonos? |
   (?: tf | tel | tel[éf] | tfno ) \. |        # abbreviations
   celular (?: es )? |                         # mobile
   ll[aá]m[aeoáéó][bdilmrs]?\w*                # conjugation for "llamar"
 )
 (?! \w )
"""

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
            "value": CONTEXT_REGEX,
            "width": [64, 64]
        }
    }
}
