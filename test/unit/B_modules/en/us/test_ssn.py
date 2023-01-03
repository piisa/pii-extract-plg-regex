"""
Test US Social Security Number
"""

from pii_extract_plg_regex.modules.en.us.social_security_number import PII_TASKS
from taux.taskproc import check_tasks

TESTCASES = [
    # A valid SSN
    ("SSN: 536-90-4399", "SSN: <GOV_ID:536-90-4399>"),
    # SSN with spaces
    ("SSN: 536 90 4399", "SSN: <GOV_ID:536 90 4399>"),
    # An invalid SSN
    ("not a SSN: 666-90-4399", "not a SSN: 666-90-4399"),
]


def test10_ssn():
    defaults = {"lang": "en", "country": "us"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
