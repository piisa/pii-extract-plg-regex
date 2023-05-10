"""
Test AU phone numbers
"""

from pii_extract_plg_regex.modules.en.au.phone_number import PII_TASKS
from taux.taskproc import check_tasks


TESTCASES = [
    # Valid phone number
    (
        "The phone numbers are 07 4354 4311 and (03) 7010 5678",
        "The phone numbers are <PHONE_NUMBER:07 4354 4311> and <PHONE_NUMBER:(03) 7010 5678>"
    ),
    (
        "Call me at 0491 570 159",
        "Call me at <PHONE_NUMBER:0491 570 159>",
    ),
    # No spaces
    (
        "The phone numbers are 0743544311 and 0370105678",
        "The phone numbers are <PHONE_NUMBER:0743544311> and <PHONE_NUMBER:0370105678>"
    ),
    # Missing context
    (
        "The numbers are 07 4354 4311 and (03) 7010 5678",
        "The numbers are 07 4354 4311 and (03) 7010 5678"
    ),
    # Invalid numbers
    (
        "Telephone (03) 12 4567",
        "Telephone (03) 12 4567"
    ),
    (
        "Phone 0431 341 2215",
        "Phone 0431 341 2215"
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
