"""
Find valid bitcoin addresses
1. Obtain candidates, by using a generic regex expression
2. Validate candidates by
    - using a more exact regex
    - validating the number through the Luhn algorithm
"""

import re

from typing import Iterable

from stdnum import bitcoin

from pii_data.types import PiiEnum

# ----------------------------------------------------------------------------

# regex for the three types of bitcoin addresses
_BITCOIN_PATTERN = (
    r"\b (?: [13] [" + bitcoin._base58_alphabet + "]{25,34} |"
    + "bc1 [" + bitcoin._bech32_alphabet + r"]{8,87} ) \b"
)


# compiled regex
_REGEX = None


def bitcoin_address(text: str) -> Iterable[str]:
    """
    Bitcoin addresses (P2PKH, P2SH and Bech32), recognize & validate
    """
    # Compile regex if needed
    global _REGEX
    if _REGEX is None:
        _REGEX = re.compile(_BITCOIN_PATTERN, flags=re.X)

    # Find and validate candidates
    # Find all instances
    for match in _REGEX.finditer(text):
        item_value = match.group()
        if bitcoin.is_valid(item_value):
            yield item_value, match.start()


# ---------------------------------------------------------------------

PII_TASKS = [(PiiEnum.BLOCKCHAIN_ADDRESS, bitcoin_address, "bitcoin")]
