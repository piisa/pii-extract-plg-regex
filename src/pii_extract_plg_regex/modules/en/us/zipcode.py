"""
US zipcodes (with state abbreviation)
"""
import re

from typing import Iterable, Tuple

from pii_data.types import PiiEnum


USPS_STATE_ABBR = [
    "AK",
    "AL",
    "AR",
    "AZ",
    "CA",
    "CO",
    "CT",
    "DC",
    "DE",
    "FL",
    "GA",
    "HI",
    "IA",
    "ID",
    "IL",
    "IN",
    "KS",
    "KY",
    "LA",
    "MA",
    "MD",
    "ME",
    "MI",
    "MN",
    "MS",
    "MO",
    "MT",
    "NC",
    "NE",
    "NH",
    "NJ",
    "NM",
    "NV",
    "NY",
    "ND",
    "OH",
    "OK",
    "OR",
    "PA",
    "RI",
    "SC",
    "SD",
    "TN",
    "TX",
    "UT",
    "VT",
    "VA",
    "WA",
    "WV",
    "WI",
    "WY"
]


# Regex for phone numbers
ZIPCODE = r"""
   (?<! \w )
   (?: 1[- ] )?
   (?: \( \d{3} \) | \d{3} )
   [- ]?
   \d{3} [- ]? \d{4}
   (?! [-\w] )
"""

# ----------------------------------------------------------------------------

# compiled regex
_REGEX = None


def _zipcode_regex():
    state = "(?:" + "|".join(USPS_STATE_ABBR) + ")"
    regex = r"(?<! \w )" + state + r"\s+" + r"\d{5}" + r"(?! \w )"
    return re.compile(regex, re.X)


def US_zipcode(text: str) -> Iterable[Tuple[str, int]]:
    """
    US zip codes
    """
    # Compile regex if needed
    global _REGEX
    if _REGEX is None:
        _REGEX = _zipcode_regex()

    # Find all instances
    for match in _REGEX.finditer(text):
        yield match.group(), match.start()


# ---------------------------------------------------------------------


PII_TASKS = {
    "class": "callable",
    "task": US_zipcode,
    "pii": {
        "type": PiiEnum.LOCATION,
        "subtype": "zipcode",
        "method": "soft-regex"
    }
}
