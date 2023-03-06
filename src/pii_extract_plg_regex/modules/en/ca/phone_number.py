"""
Canadian phone numbers
"""
import re

from typing import Iterable, Tuple

import phonenumbers

from pii_data.types import PiiEnum

# Regex for phone numbers
PHONE_REGEX = r"""
   (?<! \w )
   (?: 1[- ] )?                         # country code
   (?: \( \d{3} \) | \d{3} )            # area code
   [- /]?
   \d{3}                                # central office code/exchange code
   [- ]?
   \d{4}                                # station code
   (?! [-\w] )
"""

# Context that must be found around the phone number
CONTEXT_REGEX = r"""
 \b
 (?:
   (?: tele )? phone s? |
   mobile s? |
   call
 )
 \b
"""

# ----------------------------------------------------------------------------

# compiled regex
_REGEX = None


def CA_phone_number(text: str) -> Iterable[Tuple[str, int]]:
    """
    US Phone Numbers
    """
    # Compile regex if needed
    global _REGEX
    if _REGEX is None:
        _REGEX = re.compile(PHONE_REGEX, flags=re.X)

    # Find all instances
    for match in _REGEX.finditer(text):
        item_value = match.group()
        ph = phonenumbers.parse(item_value, "CA")
        if phonenumbers.is_valid_number_for_region(ph, "CA"):
            yield item_value, match.start()

# ---------------------------------------------------------------------


PII_TASKS = {
    "class": "callable",
    "task": CA_phone_number,
    "pii": {
        "type": PiiEnum.PHONE_NUMBER,
        "subtype": "Canadian phone number",
        "method": "soft-regex,context",
        "context": {
            "type": "regex",
            "value": CONTEXT_REGEX,
            "width": [64, 64]
        }
    }
}
