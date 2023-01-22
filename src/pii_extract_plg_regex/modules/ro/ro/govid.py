"""
Romanian Government-issued CNP (Cod Numeric Personal)
"""

import re

from pii_data.types import PiiEnum

from stdnum.ro import cnp as stdnum_cnp

from typing import Iterable, Tuple

# Regex for CNP
_CNP_PATTERN = r"\b \d{13} \b"

# -------------------------------------------------------------------------

# compiled regex
_REGEX = None

def Romanian_CNP(text: str) -> Iterable[Tuple[str, int]]:
    """
    Romanian Cod Numeric Personal
    """
    # Compile regex if needed
    global _REGEX
    if _REGEX is None:
        _REGEX = re.compile(_CNP_PATTERN, flags=re.X)

    # Find all instances
    for match in _REGEX.finditer(text):
        item_value = match.group()
        if stdnum_cnp.is_valid(item_value):
            yield item_value, match.start()


# ---------------------------------------------------------------------

# Task descriptor
PII_TASKS = {
    "class": "callable",
    "task": Romanian_CNP,
    "pii": {
        "type": PiiEnum.GOV_ID,
        "subtype": "Romanian CNP",
        "method": "weak-regex,checksum"
    }
}
