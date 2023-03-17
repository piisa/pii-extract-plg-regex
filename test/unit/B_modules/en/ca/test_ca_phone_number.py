"""
Test Canadian phone numbers
"""

from pii_extract_plg_regex.modules.en.ca.phone_number import PII_TASKS
from taux.taskproc import check_tasks


TESTCASES = [
    # Valid phone number
    (
        "The phone numbers are (204) 435-4311 and (236) 423 4567",
        "The phone numbers are <PHONE_NUMBER:(204) 435-4311> and <PHONE_NUMBER:(236) 423 4567>"
    ),
    (
        "Call me at 418 8764312",
        "Call me at <PHONE_NUMBER:418 8764312>",
    ),
    (
        "Mobile 506/312-4312",
        "Mobile <PHONE_NUMBER:506/312-4312>"
    ),
    # No spaces
    (
        "The phone numbers are 9024354311 and 3684234567",
        "The phone numbers are <PHONE_NUMBER:9024354311> and <PHONE_NUMBER:3684234567>"
    ),
    # Missing context
    (
        "The numbers are 9024354311 and 3684234567",
        "The numbers are 9024354311 and 3684234567"
    ),
    # Invalid numbers
    (
        "Telephone (333) 123 4567",
        "Telephone (333) 123 4567"
    ),
    (
        "Telephone (945) 435-4311",     # US number
        "Telephone (945) 435-4311"
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
