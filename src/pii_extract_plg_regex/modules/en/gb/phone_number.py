"""
UK phone numbers
"""
import re

from typing import Iterable, Tuple

import phonenumbers

from pii_data.types import PiiEnum

# Regex for UK phone numbers
PHONE_REGEX = r"""
   (?<! [\(\w] )
   (?:
      07\d{3} \s? \d{3} \s? \d{3} |                       # mobile
      (?P<p1>\()? 0\d{2} (?(p1)\)) \s? \d{4} \s? \d{4} |  # 3-digit area code
      (?P<p2>\()? 0\d{3} (?(p2)\)) \s? \d{3} \s? \d{4} |  # 4-digit area code
      (?P<p3>\()? 0\d{4} (?(p3)\)) \s? \d{2} \s? \d{4} |  # 5-digit area code
      (?P<p4>\()? 0\d{3} \s? \d{2} (?(p4)\)) \s?          # 6-digit area code
         (?:
            \d{2} \s? \d{3} | \d{4}
         )
   )
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


def UK_phone_number(text: str) -> Iterable[Tuple[str, int]]:
    """
    UK Phone Numbers
    """
    # Compile regex if needed
    global _REGEX
    if _REGEX is None:
        _REGEX = re.compile(PHONE_REGEX, flags=re.X)

    # Find all instances
    for match in _REGEX.finditer(text):
        item_value = match.group()
        ph = phonenumbers.parse(item_value, "GB")
        if phonenumbers.is_valid_number_for_region(ph, "GB"):
            yield item_value, match.start()

# ---------------------------------------------------------------------


PII_TASKS = {
    "class": "callable",
    "task": UK_phone_number,
    "pii": {
        "type": PiiEnum.PHONE_NUMBER,
        "subtype": "UK phone number",
        "method": "soft-regex,context",
        "context": {
            "type": "regex",
            "value": CONTEXT_REGEX,
            "width": [64, 64]
        }
    }
}
