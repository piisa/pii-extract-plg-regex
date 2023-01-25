"""
Test US phone numbers
"""

from pii_extract_plg_regex.modules.en.gb.phone_number import PII_TASKS
from taux.taskproc import check_tasks


TESTCASES = [
    # Valid phone numbers
    (
        "The phone numbers are (020) 8231 7777 and (01792) 23 5231",
        "The phone numbers are <PHONE_NUMBER:(020) 8231 7777> and <PHONE_NUMBER:(01792) 23 5231>"
    ),
    (
        "Call me at (0131) 776 4312",
        "Call me at <PHONE_NUMBER:(0131) 776 4312>",
    ),
    (
        "Mobile 07556 612 312",
        "Mobile <PHONE_NUMBER:07556 612 312>"
    ),
    # No spaces
    (
        "The phone numbers are 02082317777 and 07834231231",
        "The phone numbers are <PHONE_NUMBER:02082317777> and <PHONE_NUMBER:07834231231>"
    ),
    # Missing context
    (
        "The numbers are 02082317777 and 07834231231",
        "The numbers are 02082317777 and 07834231231"
    ),
    #Invalid parenthesis
    (
        "Telephone (020 8231 7777)",
        "Telephone (020 8231 7777)",
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
