"""
FR phone numbers
"""

import re
from typing import Iterable, Tuple

import phonenumbers
from pii_data.types import PiiEnum

# ----------------------------------------------------------------------------

# Regex for mobile & landline phone numbers
PHONE_REGEX = r"""
    \b
    0 [ \xa0]? [1-9]           # 0 + Area code (1-9)
    (?:[ \xa0.-]*\d{2}){4}     # Remaining 8 numbers (all together or by pairs)
    \b
"""

# Context that must be found around the phone number
CONTEXT_REGEX = r"""
    \b
    t[ée]l[ée]phon((es?)|iques?) |                      # Phone & corresponding adjective
    t[eé]l \. |                                         # Abbreviation
    mobiles? |                                          # Mobile
    appell?(er|âm|ât|èr)?a?i?e?o?(s|t|ns|z|nt|é|)? |    # Conjugation of 'to call'
    coups? de fil                                       # Informal synonym of call
    \b
"""

# ---------------------------------------------------------------------

# Compiled regex
_REGEX = None


def FR_phone_number(text: str) -> Iterable[Tuple[str, int]]:
    """
    French phone number, using regex + pattern validation + context
    """
    # Compile regex if needed
    global _REGEX
    if _REGEX is None:
        _REGEX = re.compile(PHONE_REGEX, flags=re.X)

    # Find all instances
    for match in _REGEX.finditer(text):
        item_value = match.group()
        ph = phonenumbers.parse(item_value, "FR")
        if phonenumbers.is_valid_number_for_region(ph, "FR"):
            yield item_value, match.start()


# ---------------------------------------------------------------------

PII_TASKS = {
    "class": "callable",
    "task": FR_phone_number,
    "pii": {
        "type": PiiEnum.PHONE_NUMBER,
        "method": "soft-regex,pattern-validation,context",
        "context": {"type": "regex", "value": CONTEXT_REGEX, "width": [64, 64]},
    },
}
