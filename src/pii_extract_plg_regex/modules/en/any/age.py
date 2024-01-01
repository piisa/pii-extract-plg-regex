"""
Age, as a regex, covering some (but by no means all) forms of expressing age
"""

from pii_data.types import PiiEnum

# Regex for phone numbers
_AGE_REGEX = r"""
   \b
   (?:
     (?: (1?\d{1,2}) [-\s] years? [-\s] old ) |
     (?: age (?: \s+ is | \s* : )? \s+ (1?\d{1,2}) )
   )
   \b
"""

# ---------------------------------------------------------------------


PII_TASKS = {
    "class": "regex",
    "name": "age regex",
    "task": _AGE_REGEX,
    "pii": {
        "type": PiiEnum.AGE,
        "method": "soft-regex"
    }
}
