"""
Asutralian phone numbers
"""
import re

from typing import Iterable, Tuple

import phonenumbers

from pii_data.types import PiiEnum

# Regex for phone numbers
PHONE_REGEX = r"""
   (?<! \w )
   (?:
      (?: \( 0[2378] \) | 0[2378] ) [ \xa0]?  \d{4}  [ \xa0]?  \d{4}  # landline
      |
      0[45]\d{2}  [ \xa0]?  \d{3}  [ \xa0]?  \d{3}                    # mobile
   )
   (?! [-\w] )
"""

# Context that must be found around the phone number
CONTEXT_REGEX = r"""
 \b
 (?:
   (?: tele )? phone s? |
   mobile s? |
   call |
   tel | cell | mob | ph\.
 )
 \b
"""

# ----------------------------------------------------------------------------

# compiled regex
_REGEX = None


def AU_phone_number(text: str) -> Iterable[Tuple[str, int]]:
    """
    AU Phone Numbers
    """
    # Compile regex if needed
    global _REGEX
    if _REGEX is None:
        _REGEX = re.compile(PHONE_REGEX, flags=re.X)

    # Find all instances
    for match in _REGEX.finditer(text):
        item_value = match.group()
        try:
            ph = phonenumbers.parse(item_value, "AU")
        except phonenumbers.NumberParseException:
            continue
        if phonenumbers.is_valid_number_for_region(ph, "AU"):
            yield item_value, match.start()

# ---------------------------------------------------------------------


PII_TASKS = {
    "class": "callable",
    "task": AU_phone_number,
    "pii": {
        "type": PiiEnum.PHONE_NUMBER,
        "method": "soft-regex,context",
        "context": {
            "type": "regex",
            "value": CONTEXT_REGEX,
            "width": [64, 64]
        }
    }
}
