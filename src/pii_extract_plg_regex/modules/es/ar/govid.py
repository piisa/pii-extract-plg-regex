"""
Argentinian Government-issued DNI (Documento Nacional de Identidad)
"""

from pii_data.types import PiiEnum


# Regex for DNI
_DNI_PATTERN = r"""
   (?: \b | (?<= DNI) )
   (?: \d{7,8}
       |
       (?: \d{1,2} \. \d{3} \. \d{3} )
   )
  \b
"""


# ---------------------------------------------------------------------

# Task descriptor
PII_TASKS = {
    "class": "regex",
    "task": _DNI_PATTERN,
    "name": "Argentinian DNI",
    "pii": {
        "type": PiiEnum.GOV_ID,
        "subtype": "Argentinian DNI",
        "method": "weak-regex,context",
        "context": {
            "type": "word",
            "value": ["dni", "documento nacional de identidad",
                      "documento de identidad"],
            "width": [64, 32]
        }
    }
}
