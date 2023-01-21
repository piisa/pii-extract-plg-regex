"""
Detection and validation of Clave Única de Registro de Población for Mexico

It contains two check digits, so it can be validated.
"""

import re

from stdnum.mx import curp as stdnum_curp

from typing import Iterable, Tuple

from pii_data.types import PiiEnum


_CURP_PATTERN = r"\b [A-Z] [AEIOU] [A-Z]{2} \d{6} [HM] [A-Z]{5} [0-9A-Z] \d \b"

# -------------------------------------------------------------------------

# compiled regex
_REGEX = None

def Mexican_CURP(text: str) -> Iterable[Tuple[str, int]]:
    """
    Mexican Clave Única de Registro de Población
    """
    # Compile regex if needed
    global _REGEX
    if _REGEX is None:
        _REGEX = re.compile(_CURP_PATTERN, flags=re.X)

    # Find all instances
    for match in _REGEX.finditer(text):
        item_value = match.group()
        if stdnum_curp.is_valid(item_value):
            yield item_value, match.start()


# -------------------------------------------------------------------------

PII_TASKS = {
    "class": "callable",
    "task": Mexican_CURP,
    "pii": {
        "type": PiiEnum.GOV_ID,
        "subtype": "Mexican CURP",
        "method": "strong-regex,checksum"
    }
}
