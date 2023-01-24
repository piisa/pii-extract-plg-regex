"""
Test US phone numbers
"""

from pii_extract_plg_regex.modules.en.us.phone_number import PII_TASKS
from taux.taskproc import check_tasks


TESTCASES = [
    # Valid phone number
    (
        "The phone numbers are (945) 435-4311 and (207) 423 4567",
        "The phone numbers are <PHONE_NUMBER:(945) 435-4311> and <PHONE_NUMBER:(207) 423 4567>"
    ),
    (
        "Call me at 575 8764312",
        "Call me at <PHONE_NUMBER:575 8764312>",
    ),
    (
        "Mobile 656 3124312",
        "Mobile <PHONE_NUMBER:656 3124312>"
    ),
    # No spaces
    (
        "The phone numbers are 9454354311 and 2074234567",
        "The phone numbers are <PHONE_NUMBER:9454354311> and <PHONE_NUMBER:2074234567>"
    ),
    # Missing context
    (
        "The numbers are 9454354311 and 2074234567",
        "The numbers are 9454354311 and 2074234567"
    ),
    # Invalid numbers
    (
        "Telephone (333) 123 4567",
        "Telephone (333) 123 4567"
    ),
    (
        "Phone 656 31243121",
        "Phone 656 31243121"
    ),
    (
        "Call me at +34983453999",
        "Call me at +34983453999"
    )
]


def test10_phone_number():
    defaults = {"lang": "en", "country": "us"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
