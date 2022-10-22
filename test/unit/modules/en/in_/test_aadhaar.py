"""
Test Indian Aadhaar Number
"""

from pii_extract_plg_regex.modules.en.in_.aadhaar import PII_TASKS
from taux.taskproc import check_tasks


TESTCASES = [
    # A valid aadhaar
    ("aadhaar number 234123412346",
     "aadhaar number <GOV_ID:234123412346>"),
    # aadhaar with spaces
    ("aadhaar number 2341 2341 2346",
     "aadhaar number <GOV_ID:2341 2341 2346>"),
    # An invalid aadhaar
    (
        "not a real aadhaar number: 2341 2341 2347",
        "not a real aadhaar number: 2341 2341 2347",
    ),
]


def test10_aadhaar():
    defaults = {"lang": "any", "country": "in_"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
