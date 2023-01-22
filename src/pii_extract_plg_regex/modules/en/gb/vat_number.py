"""
Detection of UK VAT number.

"""

from pii_data.types import PiiEnum


_VAT_PATTERN = r"""
  \w{2} \s? \d{2} \s? \d{2} \s? \w
  |
  GB \s? \d{6} \s? \w
  |
  GB \d{3} \s \d{3} \s \d{2} \s \d{3}
  |
  GB \d{3} \s \d{4} \s \d{2} (?:\s\d{3})?
  |
  GB(?:GD|HA)\d{3}"""


PII_TASKS = [
    (PiiEnum.GOV_ID, _VAT_PATTERN, "UK VAT number")
]
