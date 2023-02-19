"""
Indian phone numbers, in English context
"""
import re

from typing import Iterable, Tuple

import phonenumbers

from pii_data.types import PiiEnum

# Regex for Indian phone numbers
PHONE_REGEX = r"""
   (?<! [\(\w] )
   (?:
      [6-9]\d{3} -? \d{6} |                                   # mobile
      \d{3} [- ] \d{8} | \d{4} [- ]\d{7} | \d{5} [- ]\d{6} |  # just dashes
      (?P<p1>\()? 0\d{2} (?(p1)\)) \s? \d{4} \s? \d{4} |  # 3-digit area code
      (?P<p2>\()? 0\d{3} (?(p2)\)) \s? \d{3} \s? \d{4} |  # 4-digit area code
      (?P<p3>\()? 0\d{4} (?(p3)\)) \s? \d{2} \s? \d{4}    # 5-digit area code
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


def Indian_phone_number(text: str) -> Iterable[Tuple[str, int]]:
    """
    Indian Phone Numbers
    """
    # Compile regex if needed
    global _REGEX
    if _REGEX is None:
        _REGEX = re.compile(PHONE_REGEX, flags=re.X)

    # Find all instances
    for match in _REGEX.finditer(text):
        item_value = match.group()
        ph = phonenumbers.parse(item_value, "IN")
        if phonenumbers.is_valid_number_for_region(ph, "IN"):
            yield item_value, match.start()

# ---------------------------------------------------------------------


PII_TASKS = {
    "class": "callable",
    "task": Indian_phone_number,
    "pii": {
        "type": PiiEnum.PHONE_NUMBER,
        "subtype": "Indian phone number",
        "method": "soft-regex,context",
        "context": {
            "type": "regex",
            "value": CONTEXT_REGEX,
            "width": [64, 64]
        }
    }
}
