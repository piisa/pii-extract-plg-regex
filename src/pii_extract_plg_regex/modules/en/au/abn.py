"""
Detection and validation of Australian business number (ABN).

"""
import re

from stdnum.au import abn

from typing import Iterable, Tuple

from pii_data.types import PiiEnum


# ----------------------------------------------------------------------------

_ABN_PATTERN = r"\b (?: \d{2} \s \d{3} \s \d{3} \s \d{3} | \d{11} ) \b"
_REGEX = None


def australian_business_number(text: str) -> Iterable[Tuple[str, int]]:
    """
    Australian Business Number (detect and validate)
    """
    # Compile regex if needed
    global _REGEX
    if _REGEX is None:
        _REGEX = re.compile(_ABN_PATTERN, flags=re.X)

    # Find all matches
    for match in _REGEX.finditer(text):
        item = match.group()
        if abn.is_valid(item):
            yield item, match.start()


# ---------------------------------------------------------------------

PII_TASKS = {
    "class": "callable",
    "task": australian_business_number,
    "pii": {
        "type": PiiEnum.GOV_ID,
        "subtype": "Australian Business Number",
        "method": "weak-regex,checksum"
    }
}
