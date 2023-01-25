"""
US phone numbers
"""
import re

from typing import Iterable, Tuple

import phonenumbers

from pii_data.types import PiiEnum

# Regex for phone numbers
PHONE_REGEX = r"""
   (?<! \w )
   (?: 1[- ] )?
   (?: \( \d{3} \) | \d{3} )
   [- ]?
   \d{3} [- ]? \d{4}
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


def US_phone_number(text: str) -> Iterable[Tuple[str, int]]:
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
        ph = phonenumbers.parse(item_value, "US")
        if phonenumbers.is_valid_number_for_region(ph, "US"):
            yield item_value, match.start()

# ---------------------------------------------------------------------


PII_TASKS = {
    "class": "callable",
    "task": US_phone_number,
    "pii": {
        "type": PiiEnum.PHONE_NUMBER,
        "subtype": "US phone number",
        "method": "soft-regex,context",
        "context": {
            "type": "regex",
            "value": CONTEXT_REGEX,
            "width": [64, 64]
        }
    }
}
