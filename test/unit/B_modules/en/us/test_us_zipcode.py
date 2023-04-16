"""
Test US phone numbers
"""

from pii_extract_plg_regex.modules.en.us.zipcode import PII_TASKS
from taux.taskproc import check_tasks


TESTCASES = [
    # Valid zip code
    (
        "Zipcode CA 32456", "Zipcode <LOCATION:CA 32456>"
    ),
    (
        "the address is in NY 45123",
        "the address is in <LOCATION:NY 45123>",
    ),
    # Invalid zip codes
    (
        "Zipcode CA 324567", "Zipcode CA 324567"
    ),
    (
        "the address is in RX 45123", "the address is in RX 45123",
    ),
    (
        "the address is in ANY 45123", "the address is in ANY 45123"
    )
]


def test10_zipcode():
    defaults = {"lang": "en", "country": "us"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
