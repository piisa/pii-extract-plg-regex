"""
Detection of email addresses
"""

from pii_data.types import PiiEnum


# Simple pattern
_EMAIL_PATTERN_SIMPLE = r"""
    [\w\.=-]+
    @
    [\w\.-]+ \. [\w]{2,4}
"""

# Slightly more elaborate pattern
_EMAIL_PATTERN_MED = r"""
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

# A more complex pattern
# Note: to reduce false positives, a number of technically-valid-but-rarely-used
# email address patterns (e.g. with parenthesis or slashes) will not match
_EMAIL_PATTERN_FULL = r'''
    (?<= ^ | [[({<\b\s@,?!;'"\p{Han}¿¡:.] | \\['"] )  # left delimiter
    (
      (?:                                             # local part
        [^][(){}<>\b\s@,?!;'":#/\\=.\-]               # arbitrary character
        |
        (?: [=.\-] (?! [.@]) )                        # ".=-", not before ".@"
      )+
      @
      (?:
        (?:
             \w                                       # single-letter subdomain
           |
             [^.\b\s@?!;,/()>\-:]                     # subdomain (>=2 letter)
             [^.\b\s@?!;,/()>]{0,62}
             [^.\b\s@?!;,/()>\-:'"]
        )
        \.
      ){1,10}
      (?: [\p{L}\p{M}]{2,63} | xn-- \w+ )             # TLD, including IDN
    )
    (?= $ | [])}>\b\s@,?!;'"\p{Han}] | \\['"] | : (?! \d) | \. (?! \S))   # right delim
'''

PII_TASKS = [(PiiEnum.EMAIL_ADDRESS, _EMAIL_PATTERN_FULL)]
