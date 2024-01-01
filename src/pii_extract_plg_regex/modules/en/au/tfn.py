"""
Detection and validation of Australian Tax File Number (TFN).

"""
import re

from stdnum.au import tfn

from typing import Iterable, Tuple

from pii_data.types import PiiEnum


_TFN_PATTERN = r"\b (?: \d{3} \s \d{3} \s \d{3} | \d{8,9} ) \b"
_REGEX = None


def AU_tax_file_number(text: str) -> Iterable[Tuple[str, int]]:
    """
    Australian Tax File Number, using regex + checksum validation
    """
    # Compile regex if needed
    global _REGEX
    if _REGEX is None:
        _REGEX = re.compile(_TFN_PATTERN, flags=re.X)

    # Find all matches
    for match in _REGEX.finditer(text):
        item = match.group()
        if tfn.is_valid(item):
            yield item, match.start()


# ---------------------------------------------------------------------

PII_TASKS = {
    "class": "callable",
    "task": AU_tax_file_number,
    "pii": {
        "type": PiiEnum.GOV_ID,
        "subtype": "Australian Tax File Number",
        "method": "weak-regex,checksum"
    }
}
