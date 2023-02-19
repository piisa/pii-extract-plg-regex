"""
Test Indian phone numbers
"""

from pii_extract_plg_regex.modules.en.in_.phone_number import PII_TASKS
from taux.taskproc import check_tasks


TESTCASES = [
    # Valid phone numbers
    (
        "The phone numbers are (022) 6231 7777 and 01792-235231",
        "The phone numbers are <PHONE_NUMBER:(022) 6231 7777> and <PHONE_NUMBER:01792-235231>"
    ),
    (
        "Call me at (0131) 776 4312",
        "Call me at <PHONE_NUMBER:(0131) 776 4312>",
    ),
    (
        "Mobile 7556-612312",
        "Mobile <PHONE_NUMBER:7556-612312>"
    ),
    # No spaces
    (
        "The phone numbers are 02262317777 and 07834231231",
        "The phone numbers are <PHONE_NUMBER:02262317777> and <PHONE_NUMBER:07834231231>"
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
    defaults = {"lang": "en", "country": "in"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
