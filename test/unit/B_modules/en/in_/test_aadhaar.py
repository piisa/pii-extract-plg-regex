"""
Test Indian Aadhaar Number
"""

from taux.taskproc import check_tasks

# Import the task descriptor
from pii_extract_plg_regex.modules.en.in_.aadhaar import PII_TASKS

TESTCASES = [
    # A valid aadhaar
    (
        "aadhaar number 234123412346",
        "aadhaar number <GOV_ID:234123412346>"),
    # aadhaar with spaces
    (
        "aadhaar number 2341 2341 2346",
        "aadhaar number <GOV_ID:2341 2341 2346>"),
    # An invalid aadhaar (fails checksum)
    (
        "not a real aadhaar number: 2341 2341 2347",
        "not a real aadhaar number: 2341 2341 2347",
    ),
]


def test10_aadhaar():
    """
    Test task processing, directly instantiating the task
    """
    defaults = {"lang": "any", "country": "in_"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
