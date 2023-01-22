"""
Test Australian Business Number
"""

from taux.taskproc import check_tasks

# Import the task descriptor
from pii_extract_plg_regex.modules.en.au.abn import PII_TASKS

TESTCASES = [
    # A valid ABN
    ("business number: 83 914 571 673.",
     "business number: <GOV_ID:83 914 571 673>."),
    # ABN without spaces
    ("business number: 83914571673.",
     "business number: <GOV_ID:83914571673>."),
    # An invalid ABN
    ("not an ABN: 83 914 571 679", "not an ABN: 83 914 571 679"),
]


def test10_abn():
    """
    Test task processing, directly instantiating the task
    """
    defaults = {"lang": "any", "country": "au"}
    for e, g in check_tasks(PII_TASKS, defaults, TESTCASES):
        assert e == g
