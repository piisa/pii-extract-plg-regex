"""
Argentinian phone numbers, using libphonenumbers
"""

import re

from typing import Iterable, Tuple

import phonenumbers

from pii_data.types import PiiEnum


# Regex for phone numbers
# https://es.wikipedia.org/wiki/N%C3%BAmeros_telef%C3%B3nicos_en_Argentina
PHONE_REGEX = r"""
  \b
  (?: 9[ \xa0] )?
  (?:
     11 [ \xa0]? (?: 15 [ \xa0]? )? \d{4} [-\s]? \d{4}            # 2-digit area code
     |
     [23]\d{2} [ \xa0]? (?: 15 [ \xa0]? )? \d{3} [-\s]? \d{4}     # 3-digit area code
     |
     [23]\d{3} [ \xa0]? (?: 15 [ \xa0]? )? \d{2} [-\s]? \d{4}     # 4-digit area code
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


def AR_phone_number(text: str) -> Iterable[Tuple[str, int]]:
    """
    Argentinian phone number, using regex + pattern validation + context
    """
    # Compile regex if needed
    global _REGEX
    if _REGEX is None:
        _REGEX = re.compile(PHONE_REGEX, flags=re.X)

    # Find all instances
    for match in _REGEX.finditer(text):
        item_value = match.group()
        try:
            ph = phonenumbers.parse(item_value, "AR")
        except phonenumbers.NumberParseException:
            continue
        if phonenumbers.is_valid_number_for_region(ph, "AR"):
            yield item_value, match.start()


# ---------------------------------------------------------------------

PII_TASKS = {
    "class": "callable",
    "task": AR_phone_number,
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
