"""
Spanish bank account numbers (CCC - código cuenta cliente)

Note: **NOT** IBAN numbers, those are country (& language) independent
"""

import re

from typing import Iterable, Tuple

from stdnum.es import ccc

from pii_data.types import PiiEnum

# ----------------------------------------------------------------------------

# regex for a Código Cuenta Cliente, with optional spaces separating the pieces
_CCC_PATTERN = r"""
  (?<![\w.,])
  \d{4} [ \xa0]? \d{4} [ \xa0]? \d{2} [ \xa0]? \d{10}
  (?! \w | [.,] \d)
"""


# compiled regex
_REGEX = None


def spanish_bank_ccc(text: str) -> Iterable[Tuple[str, int]]:
    """
    Spanish Bank Accounts (código cuenta cliente, 10-digit code, pre-IBAN)
    """
    # Compile regex if needed
    global _REGEX
    if _REGEX is None:
        _REGEX = re.compile(_CCC_PATTERN, flags=re.X)

    # Find all matches
    for match in _REGEX.finditer(text):
        item = match.group()
        if ccc.is_valid(item):
            yield item, match.start()


# ---------------------------------------------------------------------

PII_TASKS = {
    "class": "callable",
    "task": spanish_bank_ccc,
    "pii": {
        "type": PiiEnum.BANK_ACCOUNT,
        "subtype": "ES Bank CCC",
        "method": "soft-regex,checksum"
    }
}
