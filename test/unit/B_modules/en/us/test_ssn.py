"""
Test US Social Security Number
"""

from taux.taskproc import check_tasks

# Import the task descriptor
from pii_extract_plg_regex.modules.en.us.social_security_number import PII_TASKS

TESTCASES = [
    # A valid SSN
    ("SSN: 536-90-4399", "SSN: <GOV_ID:536-90-4399>"),
    # SSN with spaces
    ("SSN: 536 90 4399", "SSN: <GOV_ID:536 90 4399>"),
    # An invalid SSN
    ("not a SSN: 666-90-4399", "not a SSN: 666-90-4399"),
]


def test10_ssn():
    """
    Test task processing, directly instantiating the task
    """
    defaults = {"lang": "en", "country": "us"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
