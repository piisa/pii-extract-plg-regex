"""
Detection of U.S. Social Security Number.

We just match on the number, it cannot be validated using only the number
since it does not carry a checksum
"""

from pii_data.types import PiiEnum


_SSN_PATTERN = r"""
  \b
  (?! 000 | 666 | 333 )
  0*
  (?: [0-6][0-9][0-9] | [0-7][0-6][0-9] | [0-7][0-7][0-2] )
  [-\ ]
  (?! 00)
  [0-9]{2}
  [-\ ]
  (?! 0000)
  [0-9]{4}
  \b
"""


PII_TASKS = {
    "class": "regex",
    "task": _SSN_PATTERN,
    "name": "US Social Security Number",
    "pii": {
        "type": PiiEnum.GOV_ID,
        "subtype": "social security number",
        "method": "soft-regex"
    }
}
