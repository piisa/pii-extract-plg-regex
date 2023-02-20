"""
ES phone numbers, fixed and mobile
"""

import re

from typing import Iterable, Tuple

import phonenumbers

from pii_data.types import PiiEnum

# ----------------------------------------------------------------------------

# Regex for mobile & landline phone numbers.
# Also includes the 016 Domestic abuse helpline, which by law cannot appear in phone bills
PHONE_REGEX = r"""
  (?<![\w\+])
  (?:
     \d{3} \s? \d{3} \s? \d{3}
     |
     (?: \d{3} \s? \d{2} | \d{2} \s? \d{3}) \s? \d{2} \s? \d{2}
     |
     016
  )
  \b
"""

# Context that must be found around the phone number
CONTEXT_REGEX = r"""
 \b
 (?:
   tel[ée]fonos? |
   (?: tf | tel | tel[éf] | tfno ) \. |        # abbreviations
   m[óo]vil (?: es )? |                        # mobile
   ll[aá]m[aeoáéó][bdilmrs]?\w*                # conjugation for "llamar"
 )
 (?! \w )
"""

# ---------------------------------------------------------------------

# compiled regex
_REGEX = None


def ES_phone_number(text: str) -> Iterable[Tuple[str, int]]:
    """
    ES Phone Numbers, mobile & landline
    """
    # Compile regex if needed
    global _REGEX
    if _REGEX is None:
        _REGEX = re.compile(PHONE_REGEX, flags=re.X)
    # Find all instances
    for match in _REGEX.finditer(text):
        item_value = match.group()
        if item_value == "016":
            yield item_value, match.start()
        else:
            ph = phonenumbers.parse(item_value, "ES")
            if phonenumbers.is_valid_number(ph):
                yield item_value, match.start()


# ---------------------------------------------------------------------

PII_TASKS = {
    "class": "callable",
    "task": ES_phone_number,
    "pii": {
        "type": PiiEnum.PHONE_NUMBER,
        "subtype": "ES phone number",
        "method": "soft-regex,context",
        "context": {
            "type": "regex",
            "value": CONTEXT_REGEX,
            "width": [64, 64]
        }
    }
}
