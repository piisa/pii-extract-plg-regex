"""
Detection of email addresses
"""

from pii_data.types import PiiEnum


_EMAIL_PATTERN_SIMPLE = r"""
    [\w\.=-]+
    @
    [\w\.-]+ \. [\w]{2,4}
"""

_EMAIL_PATTERN_FULL = r"""
    (?<= ^ | [\b\s@,?!;:)('".\p{Han}<] )
    (
      [^\b\s@?!;,:)('"<]+
      @
      [^\b\s@!?;,/]*
      [^\b\s@?!;,/:)('">.]
      \.
      \p{L} \w{1,}
    )
    (?= $ | [\b\s@,?!;:)('".\p{Han}>] )
"""

PII_TASKS = [(PiiEnum.EMAIL_ADDRESS, _EMAIL_PATTERN_FULL)]
