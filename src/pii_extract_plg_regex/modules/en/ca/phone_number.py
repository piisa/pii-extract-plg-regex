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
   (?: 1[- \xa0] )?                     # country code
   (?: \( \d{3} \) | \d{3} )            # area code
   [- \xa0/]?
   \d{3}                                # central office code/exchange code
   [- \xa0]?
   \d{4}                                # station code
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


def CA_phone_number(text: str) -> Iterable[Tuple[str, int]]:
    """
    Canadian phone number, using regex + number pattern validation + context
    """
    # Compile regex if needed
    global _REGEX
    if _REGEX is None:
        _REGEX = re.compile(PHONE_REGEX, flags=re.X)

    # Find all instances
    for match in _REGEX.finditer(text):
        item_value = match.group()
        try:
            ph = phonenumbers.parse(item_value, "CA")
        except phonenumbers.NumberParseException:
            continue
        if phonenumbers.is_valid_number_for_region(ph, "CA"):
            yield item_value, match.start()

# ---------------------------------------------------------------------


PII_TASKS = {
    "class": "callable",
    "task": CA_phone_number,
    "pii": {
        "type": PiiEnum.PHONE_NUMBER,
        "method": "soft-regex,pattern-validation,context",
        "context": {
            "type": "regex",
            "value": CONTEXT_REGEX,
            "width": [64, 64]
        }
    }
}
