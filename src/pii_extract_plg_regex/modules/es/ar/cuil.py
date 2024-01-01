"""
Argentinian Government-issued CUIL (Código Único de Identificación Laboral), an
identifier for the Social Security services

Note that for physical persons the CUIL is the same as the CUIT (Clave Única de
Identificación Tributaria), but there are CUIT numbers for company as well

See:

* https://es.wikipedia.org/wiki/Código_Único_de_Identificación_Laboral
* https://es.wikipedia.org/wiki/Clave_Única_de_Identificación_Tributaria
"""

import re

from typing import Iterable

from stdnum.ar import cuit

from pii_data.types import PiiEnum


# Regex for CUIL
_CUIL_PATTERN = r"""
   \b
   \d{2}
   -
   \d{7,8}
   -
   \d
   \b
"""

# ----------------------------------------------------------------------------

# compiled regex
_REGEX = None

def AR_CUIL(text: str) -> Iterable[str]:
    """
    Argentinian Código Único de Identificación Laboral (CUIL), using regex + checksum validation
    """
    # Compile regex if needed
    global _REGEX
    if _REGEX is None:
        _REGEX = re.compile(_CUIL_PATTERN, flags=re.X)

    # Find all instances
    for match in _REGEX.finditer(text):
        item = match.group()
        if cuit.is_valid(item):
            yield item, match.start()


# ---------------------------------------------------------------------

# Task descriptor
PII_TASKS = {
    "class": "callable",
    "task": AR_CUIL,
    "pii": {
        "type": PiiEnum.GOV_ID,
        "subtype": "CUIL",
        "method": "soft-regex,checksum"
    }
}
