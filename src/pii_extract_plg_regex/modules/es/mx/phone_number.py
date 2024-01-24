"""
Argentinian phone numbers, using only libphonenumbers
"""
import re

from typing import Iterable, Tuple

import phonenumbers

from pii_data.types import PiiEnum

# Regex for phone numbers
PHONE_REGEX = r"""
  (?<![\w\+])
  (?:
     \d{2} [ \xa0]? \d{4} [ \xa0]? \d{4}
     |
     \d{3} [ \xa0]? \d{3} [ \xa0]? \d{4}
  )
  \b
"""

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

# compiled regex
_REGEX = None


def MX_phone_number(text: str) -> Iterable[Tuple[str, int]]:
    """
    Mexican phone number, using regex + pattern validation + context
    """
    # Compile regex if needed
    global _REGEX
    if _REGEX is None:
        _REGEX = re.compile(PHONE_REGEX, flags=re.X)

    # Find all instances
    for match in _REGEX.finditer(text):
        item_value = match.group()
        try:
            ph = phonenumbers.parse(item_value, "MX")
        except phonenumbers.NumberParseException:
            continue
        if phonenumbers.is_valid_number_for_region(ph, "MX"):
            yield item_value, match.start()


# ---------------------------------------------------------------------

PII_TASKS = {
    "class": "callable",
    "task": MX_phone_number,
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
